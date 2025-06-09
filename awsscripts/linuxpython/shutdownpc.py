import requests

global apikey
global SID 
global senderID

apikey = "apikey"

def send_sms(number):
    headers_sms={
        "apikey": apikey,
        "Content-Type": "application/json
    }
    
    data_sms={
        "to": number,
        "text": "hello",
        "senderId": "",
        "body": "hello"
    }
    
    response = ec2_client.modify_volume(
    VolumeId=volume_id,
    VolumeType="gp3"
    )