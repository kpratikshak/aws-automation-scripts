from itemadapter import ItemAdapter 
from scrapy.exceptions import DropItem

import mysql.connector 
import psycopg2

wait_for_instance(){
    local instance_id ="$1"
    echo "waiting for instance $instance_id"
    
    while True; do
    state=$(aws ec2 describe-instances --instance-ids $instance_id --query 'Reservations[*].Instances[*].State.Name' --output text)
   echo "Instance  is $instance_id is now running "
   break 
   fi 
   sleep 10
   done
}

create_ec2_instance(){
    local ami_id="$1"
    local instance_type="$2"
    local_key_name="$3"
    local subnet_id="4"
    local security_groupd_ids="$5"
    local instance_name="$6"
    
    instance_id=$(aws ec2 run_instances \
        --image-id "$ami_id" \
        --instance-type "$instance_type" \      
        --key-name "$key_name" \
        --subnet-id "$subnet_id" \
        --security_groupd_ids "$security_groupd_ids" \
        --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$instance_name}]" \
            --query "Instances[0].InstanceId" 
            --output text    
        )
    
    if [[-z "$instance_id"]];
    then 
    echo "Failed to create ec2 instance" >&2
    exit 1
    fi
    
    echo "Instance $instance_id created successfully"
    wait_for_instance "$instance_id"
}


main(){
    check_awscli || installing_awsclie
    echo "creating ec2 instance"
    
    AMI_ID=""
    INSTANCE_TYPE=""
    KEY_NAME=""
    SUBNET_ID=""
    SECURITY_GROUP_ID=""
    INSTANCE_NAME="Shell-script-ec2-demo"
   
   create_ec2_instance ="$AMI_ID" "$INSTANCE_TYPE""" "$KEY_NAME"" "$SUBNET_ID"" "$SECURITY_GROUP_ID"" "$INSTANCE_NAME"
   echo "EC2 instnce creation completed"
   
}

main "$a"