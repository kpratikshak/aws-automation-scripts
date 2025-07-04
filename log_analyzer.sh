echo "Please enter a name of a log file, do not include extension"
read logname 

while [[ -z "$logname"]]
do 
echo "Please re-enter log file name, Not including extension"
read logname
done

if [! -f "$logname".log]
then 
echo "log file does not exist,exiting"
exit 1 

echo "Please enter keyword"
read keyword
while [[ -z "$keyword"]]
do
echo "Please re-enter keyword"
read keyword
done 

#counts the num of times that the keyword appears, displays it screen
grep -o "$keyword "$logname".log | wc -l
#Puts the keyword count in the summary report
grep -o "$keyword" "$logname".log | wc -l > log_summary.txt
grep -oE '[0-9]+\.[0-9]+\.[0-9]+' "$logname".log | sort | uniq -c | sort -nr | head -n 5
 #Displays the top 5 most IP Addresses output in the summary report
grep -oE '[0-9]+\.
grep -oE '[0-9]+\.[0-9]+\.[0-9]+' "$logname".log | sort | uniq -c | sort -nr | head -n 5 >> log_summary.txt
fi 