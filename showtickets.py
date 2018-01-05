import mysql.connector
conn = mysql.connector.connect(user='root', password='', database='ticket')
cursor = conn.cursor()
cursor.execute('select * from ticket')
ticketsinfo=cursor.fetchall()
for ticket in ticketsinfo:
    print(ticket)