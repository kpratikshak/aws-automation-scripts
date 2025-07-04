
#!/bin/sh

uuencode= "/usr/bin/uuencode"
outfile ="/tmp/rb.$$.tgz"
outfname ="backup.$(date +%y%m%d).tgz"
infile="/tmp/rb.$$.in"

trap = "/bin/rm -f $outfile $infile" 0

if [ $# -ne 2 -a $# -ne 3]; then 
    echo "Usage:$(basename $0) backup-file-list remoteaddr {targetdir}">&2 
    exit 1 
fi 

if [! -s "$1"]; then 
    echo "Error: backup list $1
    is empty or missing">&2
    exit 1
fi 

while read entry; do 
    echo "$entry" | sed -e 's/ /\\ /g' >> $infile
done < "$1"

tar czf -$(cat $infile)| \
    $uuencode $outfname | /
    mail -s "${3:-Backup archive for $(date)}}" "$2"

echo "Done.$(basename $0)
     backed up the following file:"
sed 's/^/ /' $infile 
echo -n "and mailed them to $2"
if [ !-z "$3"]; then 
    echo "with requested target directory $3"
else 
    echo ""
fi 

    exit 0
fi 

bytesin="$(awk 'BEGIN{sum=0} $12 =="i" {sum += $8} END{print sum}' $log)

bytesout="$(awk 'BEGIN{sum=0} $12 =="o" {sum += $8} END{print sum}' $log 
)