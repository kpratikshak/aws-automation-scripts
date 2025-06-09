import boto3

def get_volume_id_from_arn(volume_arn):
    arn_parts = volume_arn.split(":")
        tag_values = input_tag_value.split()
        
        ec2_client = boto3.client("ec2")
        response = ec2_client.modify_volume(
            VolumeId=volume_id,
            VolumeType="gpt",
            
        ),
    
    
    