def find_instance_by_id(self,find_instance_by_id):
    response = ec2.describe_instances(InstanceIds=[find_instance_by_id])
    return response