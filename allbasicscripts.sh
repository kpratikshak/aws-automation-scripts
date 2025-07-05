									Shell Scripting for DevOps Engineers by KASTRO
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
													LECTURE 06
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Real-Time Scripts
***************************************************
1️⃣ System Health Monitoring Script
***************************************************
✅ Monitors CPU, Memory, and Disk Usage
✅ Sends alerts if thresholds are exceeded
#!/bin/bash

CPU_THRESHOLD=80
MEM_THRESHOLD=80
DISK_THRESHOLD=90

echo "Checking System Health..."

# Get CPU Usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
CPU_INT=${CPU_USAGE%.*}

# Get Memory Usage
MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
MEM_INT=${MEM_USAGE%.*}

# Get Disk Usage
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

# Check and send alerts
if [ "$CPU_INT" -ge "$CPU_THRESHOLD" ]; then
    echo "⚠️ CPU Usage High: $CPU_INT% | Threshold: $CPU_THRESHOLD%"
fi

if [ "$MEM_INT" -ge "$MEM_THRESHOLD" ]; then
    echo "⚠️ Memory Usage High: $MEM_INT% | Threshold: $MEM_THRESHOLD%"
fi

if [ "$DISK_USAGE" -ge "$DISK_THRESHOLD" ]; then
    echo "⚠️ Disk Usage High: $DISK_USAGE% | Threshold: $DISK_THRESHOLD%"
fi

echo "System Health Check Completed."

***************************************************
2️⃣ Automated Log Cleanup Script
***************************************************
✅ Deletes logs older than X days
✅ Prevents server from filling up
#!/bin/bash

LOG_DIR="/var/log"
DAYS=30

echo "Cleaning logs older than $DAYS days in $LOG_DIR..."
find $LOG_DIR -type f -name "*.log" -mtime +$DAYS -exec rm -f {} \;
echo "Log cleanup completed."

***************************************************
3️⃣ Backup and Restore Script
***************************************************
✅ Backs up important directories
✅ Supports restoration
#!/bin/bash

BACKUP_DIR="/backup"
SOURCE_DIR="/var/www/html"
TIMESTAMP=$(date +"%F-%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/backup-$TIMESTAMP.tar.gz"

# Backup
backup() {
    echo "Starting backup..."
    tar -czf $BACKUP_FILE $SOURCE_DIR
    echo "Backup completed: $BACKUP_FILE"
}
''
# Restore
restore() {
    echo "Available backups:"
    ls -lh $BACKUP_DIR
    read -p "Enter backup file name to restore: " FILE
    tar -xzf "$BACKUP_DIR/$FILE" -C /
    echo "Restore completed."
}

echo "1. Backup"
echo "2. Restore"
read -p "Choose an option: " CHOICE

case $CHOICE in
    1) backup ;;
    2) restore ;;
    *) echo "Invalid option";;
esac

***************************************************
4️⃣ Kubernetes Pod Health Check Script
***************************************************
✅ Checks the status of all pods in a namespace
✅ Alerts if any pod is in a failed state

#!/bin/bash

NAMESPACE="default"

echo "Checking Kubernetes Pod Health..."
kubectl get pods -n $NAMESPACE --no-headers | awk '$3 != "Running" {print "⚠️ Pod "$1" is in state "$3}'

echo "Health Check Completed."

***************************************************
5️⃣ AWS S3 Bucket Sync Script
***************************************************
✅ Syncs local files to an S3 bucket
✅ Helps in automated backups

#!/bin/bash

BUCKET_NAME="my-backup-bucket"
SOURCE_DIR="/backup"

echo "Syncing $SOURCE_DIR to S3 bucket $BUCKET_NAME..."
aws s3 sync $SOURCE_DIR s3://$BUCKET_NAME --delete
echo "Sync Completed!"

***************************************************
6️⃣ Check if a Service is Running
***************************************************
✅ Monitors a service (like Nginx, MySQL)
✅ Restarts if it’s down

#!/bin/bash

SERVICE="nginx"

if systemctl is-active --quiet $SERVICE; then
    echo "✅ $SERVICE is running"
else
    echo "⚠️ $SERVICE is not running, restarting..."
    systemctl restart $SERVICE
fi

***************************************************
7️⃣  Find Top 5 Large Files
***************************************************
✅ Helps identify large files consuming disk space
#!/bin/bash

echo "Top 5 largest files in the system:"
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -n 5

***************************************************
8️⃣ Show Active SSH Sessions
***************************************************
✅ Displays who is logged in via SSH
#!/bin/bash

echo "Active SSH Sessions:"
who | grep "pts"

***************************************************
9️⃣ Check Disk Space and Alert
***************************************************
✅ Alerts if disk usage is above 80%
#!/bin/bash

THRESHOLD=80
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$DISK_USAGE" -ge "$THRESHOLD" ]; then
    echo "⚠️ Disk usage is high: $DISK_USAGE%"
else
    echo "✅ Disk usage is normal: $DISK_USAGE%"
fi

***************************************************
🔟 Simple User Creation Script
***************************************************
✅ Creates a user and sets a default password
#!/bin/bash

read -p "Enter username: " USERNAME
PASSWORD="Password@123"

sudo useradd -m -s /bin/bash $USERNAME
echo "$USERNAME:$PASSWORD" | sudo chpasswd

echo "✅ User $USERNAME created with password: $PASSWORD"

***************************************************
1️⃣1️⃣  Find All Running Docker Containers
***************************************************
✅ Lists active Docker containers
#!/bin/bash

echo "Running Docker containers:"
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}"

***************************************************
1️⃣2️⃣ Delete Old Docker Images
***************************************************
✅ Frees up space by deleting unused images
#!/bin/bash

echo "Deleting unused Docker images..."
docker image prune -a -f
echo "✅ Cleanup done!"

***************************************************
1️⃣3️⃣  Find All Running Docker Containers
***************************************************
✅ Lists active Docker containers
#!/bin/bash

echo "Running Docker containers:"
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}"

***************************************************
1️⃣4️⃣ Check Kubernetes Node Status
***************************************************
✅ Ensures all nodes are Ready
#!/bin/bash

echo "Checking Kubernetes Nodes..."
kubectl get nodes | grep -v "Ready"

***************************************************
1️⃣5️⃣ Trigger a Jenkins Job via CLI
***************************************************
✅ Triggers a Jenkins job without opening the UI
#!/bin/bash

JENKINS_URL="http://localhost:8080"
JOB_NAME="MyJob"
USER="admin"
API_TOKEN="your-api-token"

echo "Triggering Jenkins job: $JOB_NAME..."
curl -X POST "$JENKINS_URL/job/$JOB_NAME/build" --user "$USER:$API_TOKEN"
echo "✅ Job triggered successfully!"

***************************************************
1️⃣6️⃣ Check Jenkins Job Status
***************************************************
✅ Fetches the last build status of a Jenkins job
#!/bin/bash

JENKINS_URL="http://localhost:8080"
JOB_NAME="MyJob"
USER="admin"
API_TOKEN="your-api-token"

echo "Fetching status of last build..."
curl -s "$JENKINS_URL/job/$JOB_NAME/lastBuild/api/json" --user "$USER:$API_TOKEN" | jq -r '.result'

***************************************************
1️⃣7️⃣ Restart All Pods in a Namespace
***************************************************
✅ Restarts all pods in a given namespace
#!/bin/bash

NAMESPACE="default"

echo "Restarting all pods in $NAMESPACE..."
kubectl delete pods --all -n $NAMESPACE --grace-period=0 --force
echo "✅ All pods restarted!"

***************************************************
1️⃣8️⃣ Monitor Kubernetes Pod Status
***************************************************
✅ Continuously watches for pod status changes
#!/bin/bash

NAMESPACE="default"

echo "Monitoring pods in namespace: $NAMESPACE..."
kubectl get pods -n $NAMESPACE --watch

***************************************************
1️⃣9️⃣ Check System Uptime
***************************************************
✅ Displays how long the system has been running
#!/bin/bash

echo "System Uptime:"
uptime

***************************************************
2️⃣0️⃣ Check Disk Space Usage
***************************************************
✅ Shows available and used disk space
#!/bin/bash

echo "Disk Space Usage:"
df -h

***************************************************
2️⃣1️⃣Check CPU & Memory Usage
***************************************************
✅ Displays CPU and RAM usage
#!/bin/bash

echo "CPU Usage:"
top -b -n1 | grep "Cpu(s)"

echo "Memory Usage:"
free -m

***************************************************
2️⃣2️⃣Backup a Directory
***************************************************
✅ Creates a tar backup of a specified directory
#!/bin/bash

SRC_DIR="/home/user/data"
BACKUP_DIR="/home/user/backup"
BACKUP_FILE="$BACKUP_DIR/backup-$(date +%F).tar.gz"

mkdir -p $BACKUP_DIR
tar -czvf $BACKUP_FILE $SRC_DIR

echo "Backup completed: $BACKUP_FILE"

***************************************************
2️⃣3️⃣ Create User with required permissions
***************************************************
#!/bin/bash

# Function to set permissions
set_permissions() {
    local username=$1
    local user_perms=$2
    local group_perms=$3
    local others_perms=$4
    local user_home=$(eval echo ~$username)

    # Set permissions for the user's home directory
    chmod u=$user_perms,g=$group_perms,o=$others_perms $user_home

    echo "Permissions set for $username:"
    echo "User: $user_perms, Group: $group_perms, Others: $others_perms"
    echo "Home directory: $user_home"
}

# Prompt for username
read -p "Enter the username to create: " username

# Check if the user already exists
if id "$username" &>/dev/null; then
    echo "User $username already exists."
    exit 1
fi

# Create the user
sudo useradd -m "$username"
if [ $? -eq 0 ]; then
    echo "User $username created successfully."
else
    echo "Failed to create user $username."
    exit 1
fi

# Prompt for permissions
echo "Set permissions for the user's home directory."
read -p "Enter permissions for the user (e.g., rwx): " user_perms
read -p "Enter permissions for the group (e.g., r-x): " group_perms
read -p "Enter permissions for others (e.g., r--): " others_perms

# Validate permissions input
if [[ ! $user_perms =~ ^[r-][w-][x-]$ ]] || [[ ! $group_perms =~ ^[r-][w-][x-]$ ]] || [[ ! $others_perms =~ ^[r-][w-][x-]$ ]]; then
    echo "Invalid permissions format. Use 'rwx', 'r-x', 'r--', etc."
    exit 1
fi

# Set permissions
set_permissions "$username" "$user_perms" "$group_perms" "$others_perms"

echo "User $username setup completed."

***************************************************
2️⃣4️⃣List AWS EC2 Instances with Their Public IPs
***************************************************
✅Uses AWS CLI to fetch all running EC2 instances.
✅Displays Instance ID and Public IP.

#!/bin/bash

echo "🔎 Fetching EC2 Instances..."
aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId, PublicIpAddress]" --output table

***************************************************
2️⃣5️⃣ Backup Docker Containers and Images
***************************************************
✅Backs up all running containers and saves all Docker images as tar files.

#!/bin/bash

BACKUP_DIR="/backup/docker"
mkdir -p "$BACKUP_DIR"

# Backup all running containers
echo "🔄 Backing up running containers..."
for container in $(docker ps -q); do
    docker commit "$container" "$container-backup"
    docker save -o "$BACKUP_DIR/$container.tar" "$container-backup"
done

# Backup all images
echo "🔄 Saving all Docker images..."
docker images -q | xargs -I {} docker save -o "$BACKUP_DIR/{}.tar" {}

echo "✅ Docker backup completed. Files saved in $BACKUP_DIR"