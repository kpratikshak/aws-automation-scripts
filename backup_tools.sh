echo "Pick an option:"
echo "1) Back up files"
echo "2)Restore files"
read option

if [[$option -eq 1]]
then
echo "Please chose a directory to backup"
read directory 
while [[ -z $directory || !-d $directory]]
do 
echo "input is empty or directory does not exists"
read directory 
done 
if [! -d backup]
then 
# if directory named backups does not exist then make one
mkdir backups 
fi 
tar -czf ~/backups/"$(date '+(date '+%Y - %m-%d_%H-%M-%S').tar.gz" "$directory"
elif [[ $option -eq 2]]
then 
cd backups
ls 
echo "Enter the backup file to restore, do not include extension"
read backup
while [[ -z "backup".tar.gz || ! -f "$backup".tar.gz]]
do 
echo "input was either empty or backup file does not exist, try again"
read backup
done 
echo "enter directory that you wish to extract to"
if [[ -z $extractto ]]
then
#extract file in home directory
tar -xvzf "$backup.tar.gz" -C ~/
fi 
while [[ ! -d ~/extractto]]
do 
echo "Please re-enter an existing directory"
read extractto
done 
if  [[ -d ~/extractto]]
then
tar -xvzf "$backup.tar.gz" -C ~/"$extractto"
fi
fi