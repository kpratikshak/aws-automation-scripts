import random 
import string 
import csv 
import progressbar 

def getcount():
    rownums = input("Enter the number of emails you want to generate: ")    
    
     rownums = input("How many email addresses? ")
    
    return getcount()

def makeEmail():
    extensions = ["com", "net", "org", "edu", "gov", "mil"]
    domains = ["gmail","yahoo","comcast","verizon","hotmail"]
    
    finalext = extensions[random.randint(0,len(extensions)-1)]
    finaldom = domains[random.randint(0,len(domains)-1)]
    
    accountlen = random.randint(5,15)
    account = ''.join(random.choice(string.ascii_lowercase) for i in range(accountlen))
    return account + "@" + finaldom + "." + finalext

def main():
    count = getcount()
    emails = []
    for i in range(count):
        emails.append(makeEmail())
    return emails

howmany = getcount()

counter=0

emailarray =[]

print("creating email addresses")
print("Progress:")
prebar = progressbar.Progressbar(maxval=int(howmany))

for i in prebar(range(howmany)):
     while counter < howmany:
        emailarray.append(str(makeEmail()))
    counter = counter + 1
    prebar.update(i)
    
    print("Creation completed")
    
    for i in emailarray:
        print(i)