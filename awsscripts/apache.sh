
#!/bin/bash
sudo yum install httpd -y 
 sudo systemctl start httpd
 sudo systemctl enable httpd

echo "html><h1>Welcome to apache server</h1>" /var/www/html/index.html
