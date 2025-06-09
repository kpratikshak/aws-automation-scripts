import sqlite3
import json
import random
import codecs 

conn = sqlite3.connect("geodata.sqlite")
cur = conn.cursor()
cur.execute("SELCT * FROM Locations")
fhand = codecs.open("where.js","w","utf-8")
fhand.write("mydata= [\n")

count = 0
for row in sur:
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except:continue
    
    