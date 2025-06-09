from flask import Flask, request 
app = Flask(__name__)
import dynamodb_handler as dynamodb

@app.route("/")
def root_route():
    dynamodb.CreateTableBook()
    return "Hello World"

@app.route('/book',methods=['POST'])
def addBook():
    
    data = request.get_json()
    response = dynamodb.addItemBook(data['id'],
      data['title'],data['author'])
methods=[]