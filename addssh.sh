
#!/bin/bash

#!
OpenPort="22"
IP=$(curl -s http://checkip.amazonaws.com)
security_group_id=$(aws ec2 describe-security-groups --filters "Name=group-name,Values=default" --query "SecurityGroups[0].GroupId" --output text)  
aws ec2 authorize-security-group-ingress --group-id $security_group_id --protocol tcp --port $OpenPort --cidr $IP/32
--output text | awk '{print $2}' | grep -q "authorized"
if [ $? -eq 0 ]; then
    echo "SSH port $OpenPort opened successfully for IP $IP."
else
    echo "Failed to open SSH port $OpenPort for IP $IP."
    exit 1
fi

for security_group in $security_group_id; do
    aws ec2 authorize-security-groups-ingress "
    "$IP" "$OpenPort" --protocol tcp --port $OpenPort \
    ${security_group} --output text
    print "\n"
    aws ec2 authorize-security-group-ingress --group-id $security_group_id \

    $security_name --protocol tcp --port $OpenPort --cidr $IP/32 --output text
    --group-name $security_group --query "SecurityGroups[0].IpPermissions" --output text | grep -q "$OpenPort"
    if [ $? -eq 0 ]; then
        echo "SSH port $OpenPort is open in security group $security_group.
    else
        echo "SSH port $OpenPort is not open in security group $security_group."
    fi
done