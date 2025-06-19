#!/bin/bash
#Prepeare Environment(Update & Flyway:download -> unzip)
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install wget -y
sudo wget -q0- https:download.red-gate.com/maven/release/com/redgate/flyway/flyway-commandline/10.13.0/
flyway-commandline-10.13.0-linux-x64.tar.gz | tar -xvz 

#Configure symbolic link for flyway to use globally
sudo ln -s `pwd`/flyway-10.13.0/flyway /usr/local/bin
#retrieve variable value: RDS
source .env

#create 'migration' directory on ec2 and store DB Object
sudo mkdir -p migration
sudo chmod 777 migration
aws s3 cp "s3://soo-dynamicweb-bucket/V1_shopwise_db.sql" migration/
#sudo mv migration/shopwise_db.sql migration/V1__shopwise_db.sql

# sql -> DATA migration by Flywire -> RDS 
#configure migrate process: Destination[RDS info], Source Directory[EC2]

.env 
cat <<EOF >flyway.conf

flyway.url=jdbc:mysql://$RDS_ENDPOINT:3306/
flyway.user=$RDS_DB_USERNAME
flyway.password=$RDS_DB_PASSWORD
flyway.locations=filesystem:migration
flyway.defaultSchema=$RDS_DB_NAME
EOF

#Command Migrate process
flyway migrate
