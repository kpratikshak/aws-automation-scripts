import re 
from collections import Counter
import csv 
import argparse 

my_parser = argparse.ArgumentParser()
description = "Reading the log file"
my_parser.add_argument("--l","--logfile",help="Please enter the logfile to parse",type=argparse.FileType('r'),
                       required=True)
args = my_parser.parse_args()

logreg ="\d{1.3}\.\d{1.3}\.\d{1.3}\.\d{1.3}"
with args.logfile as f:
    fread =f.read()
    ip_list = re.findall(logreg,fread)
    with open("ipnewcount.csv","w") as f:
        ftwittercsv = csv.writer(f)
        ftwittercsv.writerow(["ip","w") as f:
            ftwittercsv.writerow(["IP_Addresses","Count"])
        for k, v in Counter(ip_list).items():
            ftwittercsv.writerow([k,v])
   
   