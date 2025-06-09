from flask import Flask 
from flask_ngrok import run_with_ngrok
import awstesting.awsTester as aws_testing

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def welcome():
    message = 'Welcome to create your own test api for AWS for EC2 just use your URl/ec2 and your 100 ec2'\''

@app route('/ec2',methods=['POST','GET'])
def ec2():
    client = aws_testing.add_service('ec2','us-east-1')
    return aws_testing.test_create_ec2(client)

if __name__ == '__main__':
    app.run()
    
    