import boto3, os
from botocore.exceptions import ClientError

vpc_id ="vpc-0a2e0a0a0a0a0a0a0ff",
subnet_id="subnet-00b5ede5e160caa59"
ami_id= "ami-0ddf424f81ddb0720"
instance_type="t2.micro"
app_name = "flask"

create_key = True
key_name = "key_name"
key_location = "/Users/bibinwilson/.ssh/devops-class/"

ec2 = boto3.resource('ec2')

try:
    response = ec2.create_instances(
        (GroupName=app_name + "-sg",
    Description=app_name + "-sg",
    VpcId=vpc_id,
    TagSpecifications=[
        {
            'ResourceType': 'security-group',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': app_name + "-sg"
                },
            ]
        },
    ]
)
 security_groupd_id= response['GroupId']
print('Security Group created %s in vpc %s' % (
    ingress = ec2.authorize_security_group_id, vpc_id))
    GroupId=security_groupd_id
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IPRanges':[
                'Cirdp':'0.0.0.0/0           
        }
    ]
    },
    {
        'IpProtocol': 'tcp',
        'FromPort': 22,
        'ToPort': 22,
        'IPRanges':[
            'Cirdp':'0.0.0.0/0'
    }
    ]
    },
    {
        'IpProtocol': 'tcp',
        'FromPort': 8080,
        'ToPort': 8080,
        'IPRanges':[
        
    ]}
    print('Security Group created %s in vpc %s' % (
    except ClientError as e:
    print(e)
    
def createKeyPair():
    try:
        keypair = ec2.create_key_pair(KeyName= key_name)
        ssh_private_k = keypair["KeyMaterial"]
       
       with os.fdopen(os.open(key_location, ".pem",os.O_WRONLY | os._O_CREAT, 0o400), "w+") as handle:
       handle.write(ssh_private_k)

      except ClientError as e:
          print(e)

    def createInstance():
        blockDeviceMappings=[
            {
                'DeviceName':"/dev/sda1",
                'Ebs':{
                    'DeleteOnTermination':True,
                    'VolumeSize':20,
                    'VolumeType':'gp2'
            }
        },
    ]
    
    instances = ec2.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name,
        SubnetId=subnet_id, 
        SecurityGroupIds=[security_groupd_id],
        BlockDeviceMappings=blockDeviceMappings,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': app_name + "-server"
                    },
                ]
            },
             {
      'ResourceType': 'volume',
      'Tags': [
          {
              'Key': 'Name',
              'Value': app_name + "-root-disk"
          },
      ]
  },
        ]
)

print(instances["Instances"][0]["InstanceId"])

if __name__ =="__main__":
    if create_key ==True 
        createKeyPair()
        
    createInstance()