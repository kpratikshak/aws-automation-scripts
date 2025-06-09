#!/bin/bash 
yum install httpd-y
echo  "welcome to server"
systemctl start httpd
systemctl enable httpd
echo "test" > /var/www/html/index.html