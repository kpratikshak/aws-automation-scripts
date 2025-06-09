import boto3
from botocore.exceptions import ClientError 

def check_ec2_and_s3_instances():
    tag_key ="env"
    input_tag_value = input("Enter tag values seperated by commas:\n\n")
    tag_values = input_tag_value.split(",")
    check_ec2_and_s3_instances(tag_key,tag_values)
    check_s3_instances(tag_key,tag_values)
    
    def check_ec2_instances(tag_key,tag_values):
        ec2 = boto3.resource("ec2")
        
        all_instances = ec2.instances.all()
        print("\n\n\nChecking EC2 instances:\n\n\n")
        
        for tag_value in tag_values:
            instances = ec2.instances.filter(
                Filters=[{"Name":"tag:" + tag_key,"Values":[tag_value]}])
            
            instances_not_match = [not_match.id for not_match in all_instances if not
                                   .id not in [instance.id for instance in instances]]
            
            print("EC2  Instances that do not match with tag values:\n\n",instances_not_match]]
            
            print("EC2 instances that do not match with Tag Values:\n\n",instances_not_match)
            
            def check_s3_instances(tag_key,tag_values):
                print("\n\n\nChecking S3 Buckets:\n\n\n")
                s3 = boto3.client("s3")
                
                matching_buckets =[]
                notmatchmaking_buckets=[]
                nottagged_buckets=[]
                
                for bucket in s3.list_buckets()["Buckets"]:
                    bucketName = bucket["Name"]
                    location = s3.get_bucket_location(Bucket=bucketName)["LocationConstraint"]
                    if location == None:
                        try:
                            tags = s3.get_bucket_tagging(Bucket=bucket_name)["LocationConstraint"]
                            for tag in tags:
                                for tag_value in tag_values:
                                    if tag["Key"] == tag_key and tag["Value"] == tag_value:
                                        if bucketName not in matching_buckets:
                                            matching_buckets.append(bucketName)
                                            
                                            notmatchmaking_buckets.remove(bucketName)
                                            elif tag["Key"] == tag_key and tag["Value"] 
                != tag_value and bucketName not in matching_buckets:
                    
                    notmatchmaking_buckets.append(bucketName)
                        except ClientError:
                            nottagged_buckets.append(bucketName
                                                     print("s3 buckets that match to tag values"))
                            
                    print("s3 buckets that do not have tags are:",nottagged_buckets)
                    
                    check_ec2_and_s3_instances()