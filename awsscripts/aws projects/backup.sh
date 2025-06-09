<<info

src/home/ubuntu/scripts
dest /home/ubuntu/backups
info

src=$1
dest=$2

timestamp=$(date +%Y%m%d%H%M%S)

zip -r "$dest/backup-$timestamp.zip" "$src>

aws s3 sync "$dest" s3://tws-backups-d

echo "backup completed & uploaded to s3"