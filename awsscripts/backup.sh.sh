
#!/bin/bash
timestamp=""$(date +%d-%m-%Y-%H-%M-%S)
backup_dir="/home/ubuntu/Scripts"



zip -r "backup_dir" "$1"

echo "BACKUP_COMPLETE"

crontab -e 
*/1 * * * * /home/ubuntu/Scripts/backup.sh /home/ubuntu
and you watch using watch ls command