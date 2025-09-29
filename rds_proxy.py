
# Lambda RDS Proxy Integration (MariaDB)
 
# Python-based AWS Lambda function integrated with Amazon RDS Proxy and MariaDB, designed for stateless CRUD operations via API Gateway.
# It demonstrates secure, scalable access to a managed relational database using best practices such as AWS Secrets Manager for credential storage.

import os
import json
import pymysql
import boto3
import logging
from datetime import datetime
from botocore.exceptions import ClientError

# --- Global Scope: Initialization and Caching ---
# Initialize clients and logger once to be reused across invocations.
logger = logging.getLogger()
logger.setLevel(logging.INFO)
secrets_manager_client = boto3.client("secretsmanager")

# Environment variables
DB_SECRET_NAME = os.environ.get("DB_SECRET_NAME")
DB_PROXY_ENDPOINT = os.environ.get("DB_PROXY_ENDPOINT")
DB_NAME = os.environ.get("DB_NAME", "customerdb")
DB_TABLE = os.environ.get("DB_TABLE", "users")

# Cache for database credentials and connection
db_credentials = None
db_connection = None

def get_db_credentials():
    """Fetches DB credentials from Secrets Manager and caches them globally."""
    global db_credentials
    if db_credentials:
        return db_credentials

    try:
        response = secrets_manager_client.get_secret_value(SecretId=DB_SECRET_NAME)
        secret = json.loads(response["SecretString"])
        db_credentials = {"username": secret["username"], "password": secret["password"]}
        return db_credentials
    except ClientError as e:
        logger.error(f"Unable to retrieve secret '{DB_SECRET_NAME}': {e}")
        raise

def get_db_connection():
    """Establishes or reuses a database connection."""
    global db_connection
    # Check if the connection is alive, if not, reconnect.
    if db_connection and db_connection.open:
        return db_connection

    try:
        creds = get_db_credentials()
        db_connection = pymysql.connect(
            host=DB_PROXY_ENDPOINT,
            user=creds["username"],
            password=creds["password"],
            db=DB_NAME,
            connect_timeout=5,
            cursorclass=pymysql.cursors.DictCursor,
        )
        logger.info("Successfully established a new database connection.")
        return db_connection
    except pymysql.MySQLError as e:
        logger.error(f"Error connecting to the database: {e}")
        raise

def build_response(status_code, body):
    """Builds a standard API Gateway proxy response."""
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(body, default=lambda o: o.isoformat() if isinstance(o, datetime) else str(o))
    }

# --- HTTP Method Handlers ---

def handle_get(conn, user_id):
    """Handles GET requests to fetch a user."""
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM `{DB_TABLE}` WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if user:
            return build_response(200, user)
        return build_response(404, {"error": "User not found"})

def handle_post(conn, body):
    """Handles POST requests to create a user."""
    name = body.get("name")
    email = body.get("email")
    if not name or not email:
        return build_response(400, {"error": "Missing 'name' or 'email' in request body"})
    
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO `{DB_TABLE}` (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
    return build_response(201, {"id": conn.insert_id(), "message": "User created successfully"})

def handle_put(conn, user_id, body):
    """Handles PUT requests to update a user."""
    name = body.get("name")
    email = body.get("email")
    if not name or not email:
        return build_response(400, {"error": "Missing 'name' or 'email' in request body"})
    
    with conn.cursor() as cursor:
        rows_affected = cursor.execute(f"UPDATE `{DB_TABLE}` SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
        conn.commit()
    
    if rows_affected == 0:
        return build_response(404, {"error": "User not found"})
    return build_response(200, {"message": f"User {user_id} updated successfully"})

def handle_delete(conn, user_id):
    """Handles DELETE requests to remove a user."""
    with conn.cursor() as cursor:
        rows_affected = cursor.execute(f"DELETE FROM `{DB_TABLE}` WHERE id = %s", (user_id,))
        conn.commit()

    if rows_affected == 0:
        return build_response(404, {"error": "User not found"})
    return build_response(200, {"message": f"User {user_id} deleted successfully"})

# --- Main Lambda Handler (Router) ---

def lambda_handler(event, context):
    try:
        # Get a database connection from the connection pool
        conn = get_db_connection()

        http_method = event.get("httpMethod", "")
        path_params = event.get("pathParameters") or {}
        user_id = path_params.get("id")

        if http_method == "GET" and user_id:
            return handle_get(conn, user_id)
        
        # For methods requiring a body, parse it here.
        body = json.loads(event.get("body") or "{}")

        if http_method == "POST":
            return handle_post(conn, body)
        elif http_method == "PUT" and user_id:
            return handle_put(conn, user_id, body)
        elif http_method == "DELETE" and user_id:
            return handle_delete(conn, user_id)
        else:
            return build_response(405, {"error": f"Method '{http_method}' not allowed or missing 'id'"})

    except (pymysql.MySQLError, ClientError) as e:
        logger.exception("A database or AWS client error occurred.")
        return build_response(500, {"error": "Internal server error."})
    except json.JSONDecodeError:
        return build_response(400, {"error": "Invalid JSON in request body"})
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        return build_response(500, {"error": "An unexpected error occurred."})
