import boto3
import boto.sqs

def add_service(service_name,region_name):
    aws.client = boto3.client(service_name, region_name=region_name)
    return aws_client


@mock_ec2
def test_create_ec2(aws_client):
    ami_id = 'ami-0c2b8ca1dad456f8a'
    count = 100
    aws.create_ec2(aws_client,ami_id,count)
    instances = aws.client.describe.instances()['reservations'][0]['instances']
    for i in instances:
        
        print(i['InstanceId'])
    if len(instances) == count:
        return  "ec2 created Successfully Instance Id ="+ instances[0]['InstanceId']+  ""
    else:
        return "ec2 not created"
    
    @mock_s3
    def test_create_s3():
        print('Testing moto s3')
        
        bucket_name = 'test-bucket'
        print('Testing moto )
       conn = boto.connect_s3()
       print('creating bucket',format(bucket_name)
       
       k = Key(bucket)
       key_name = 'file1'
       k.key = key_name
       k.set_contents_from_string('hello world')
       
       for key in bucket.list():
       print('{}/{}'.format(key.bucket.name, key.name))
       
       k2 = Key(bucket)
       k2.key= key_name
       data = k2.get_contents_as_string()
       print('fetched object {}/{}with content:{}'.format(key.bucket.name, key.name, data))
       
       key.name,data))
       
       if __name__ == 'main':
       client = add_service('s3','us-east-1')
       test.create_ec2(client)
