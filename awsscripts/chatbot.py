import boto3

def run():
    response_to_return  = list()
    list_of_instances  =list()
    
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            list_of_instances.append(instance['InstanceId'])
    
    for instance in list_of_instances:
        response = ec2.describe_instances(InstanceIds=[instance])
        for reservation in response['Reservations']:
            response_to_return.append(reservation)
    return response_to_return
