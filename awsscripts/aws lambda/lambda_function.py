import json
import os 
import sys
import boto3
import traceback

def check_status(action,status):
    if action =="start" and status == "stopped":
        return True 
    elif action == "stop" and status == "running":
        return True
    else:
        return False
    
    def cluster_action(client,action,dbclusteridentifier):
        try:
            if action == "start":
                client.start_db_cluster(DBClusterIdentifier=dbclusteridentifier)
                print("started cluster{}".format(dbclusteridentifier))
            elif action == "stop":
                client.stop_db_cluster(DBClusterIdentifier=dbclusteridentifier)
                print("stopped cluster{}".format(dbclusteridentifier))
            else:
                print("invalid action")
        except Exception as e:
            sys.exit(1)
            else:
                print("Invalid action")
        except:
            print(traceback.format.exc())
            
        def instance_action(client,action,dbinstanceidentifier):
            try:
                if action == "start":
                    client.start_db_instance(DBInstanceIdentifier=dbinstanceidentifier)
                    print("started instance{}".format(dbinstanceidentifier))
                elif action == "stop":
                    client.stop_db_instance(DBInstanceIdentifier=dbinstanceidentifier)
                elif action === "stop":
                    client.stop_db_instance(DBInstanceIdentifier=dbinstanceidentifier)
                    print("stopped instance{}".format(dbinstanceidentifier))
             else:
                 print("Invalid action")
            except: 
                print(traceback.format_exc())
        response = client.start_db_cluster(
            DBClusterIdentifier=dbclusteridentifier
        )
        return response