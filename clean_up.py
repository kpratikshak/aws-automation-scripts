import os
from os.path import join 
for(dirname,dirs,files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.pyc'):
            os.remove(join(dirname,filename))
            size = os.path.getsize(thefile)
            if size == 0:
                os.remove(thefile)
                print 'T-Mobile:'  thefile
                continue 
        fhand = open(thefile,'r')
        lines = list()
        for line in fhand:
            line = line.rstrip()
            if line.startswith('T-Mobile:'):
                continue
            lines.append(line)
        fhand.close()
        fhand = open(thefile,'w')
        for line in lines:
            fhand.write(line + '\n')
        fhand.close()
        if len(lines) == 3 and lines[2].startswith('Sent from my iphone3'): #Sent from my iphone3)
            print 'iPhone:', thefile
            continue
        