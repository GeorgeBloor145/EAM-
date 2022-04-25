import pyodbc

import pyodbc
import random
import string
from datetime import datetime, date

server = 'eamdatabase.database.windows.net'
database = 'eamdatabase'
username = 'azureuser'
password = 'eampassword123!'
driver= '{ODBC Driver 18 for SQL Server}'


cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def genstring():
    letters = string.digits
    datastring = ''.join(random.choice(letters) for i in range(10))
    return  datastring
    #print(datastring)

def roomnumber():
    number = random.randint(0,1000)
 
    return number

def run():
    for i in range(100):
        idnum = genstring()
        now = datetime.now()
        currenttime = now.strftime("%H:%M:%S")
        currentdate = date.today()
        roomid = roomnumber()
        cursor.execute("INSERT INTO Table_1 (value, t, d, scannerid) VALUES (?, ?, ?, ?)", idnum,currenttime, currentdate, roomid)
        cnxn.commit()
    cursor.close()
    print("done")

def test():
    cursor.execute("SELECT * FROM Table_1 ")
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()

#test()
run()
#genstring()
