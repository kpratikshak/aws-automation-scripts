import yaml
import boto3
import os
import stat
import sys 
import time
import paramiko
from botocore.exceptions import ClientError

ec2_client =boto3.client('ec2')

def tag_instance(instance_ids):
    i = 1
    for instance_id in instance_ids:
        response = ec2_client.create_tags(
            Resource=[
                instance_id,
            ],
            Tags=[
                {
                    'Key':'Name',
                    'Value':'instance-'+str(i)
                },
            ]
        )
        i+=1
        
    def get_instance_ids():
        resp = ec2_client.describe_instances()
        isinstance_response = resp['']