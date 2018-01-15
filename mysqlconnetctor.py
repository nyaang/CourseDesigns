import mysql.connector,time,random
password=''#在此输入密码
def closedatabse(cursor,conn):
    cursor.close()
    conn.close()
def showtickets():
    conn = mysql.connector.connect(user='root', password=password, database='ticket')
    cursor = conn.cursor()
    cursor.execute('select * from ticket')
    ticketsinfo=cursor.fetchall()
    closedatabse(cursor,conn)
    return ticketsinfo
def jugelogin(username,passwdvalue):
    conn = mysql.connector.connect(user='root', password=password, database='ticket')
    cursor = conn.cursor()
    cursor.execute('select Password from user WHERE Username=%s',(username,))
    userinfos = cursor.fetchall()
    closedatabse(cursor,conn)
    try:
        if(userinfos[0][0]==passwdvalue):
            return True
    except:
        return False
def signup(username,passwdvalue):
    conn = mysql.connector.connect(user='root', password=password, database='ticket')
    cursor = conn.cursor()
    try:
        cursor.execute('insert into user (username,password) VALUES (%s,%s)',(username,passwdvalue))
        conn.commit()
        cursor.fetchall()
    except mysql.connector.errors.InterfaceError as success:  #注册成功
        closedatabse(cursor, conn)
        if str(success)=='No result set to fetch from.':
            return True
    except mysql.connector.errors.IntegrityError:  #主键重复
        closedatabse(cursor, conn)
        return 'keyerror'
    except mysql.connector.errors.DataError as dataerror:
        closedatabse(cursor, conn)
        if(str(dataerror)=="1406 (22001): Data too long for column 'Username' at row 1"):
            return 'nameerror'
        elif(str(dataerror)=="1406 (22001): Data too long for column 'Password' at row 1"):
            return "passerror"
def getseatnum(ticket_num):    #获取一个未重复的座位号
    seatnums=[]
    i=1
    while i<=10000:
        seatnums.append(i)
        i=i+1
    conn = mysql.connector.connect(user='root', password=password, database='ticket')
    cursor = conn.cursor()
    cursor.execute('select Snumber from orders where Tnum=%s',(ticket_num,))
    seats_info=cursor.fetchall()
    closedatabse(cursor, conn)
    for seat in seats_info:
        seatnums.remove(seat[0])    #除去已被分配的座位号
    seatnum=random.choice(seatnums)
    return seatnum
def addorder(ticket_num,username):
    conn = mysql.connector.connect(user='root', password=password, database='ticket')
    cursor = conn.cursor()
    cursor.execute('select * from ticket where Tnum=%s',(ticket_num,))
    ticket_info=cursor.fetchall()[0]
    ticket_sleft=ticket_info[6]
    if ticket_sleft==0:
        return False    #余票数为0
    orderid=str(int(time.time() * 1000))   #用当前时间戳生成订单号，精确到千分之一秒
    seatnum=getseatnum(ticket_num)
    try:
        cursor.execute('insert into orders (Tnum,Username,Orderid,Dtime,Snumber,Tprice) VALUES (%s,%s,%s,%s,%s,%s)',(ticket_num,username,orderid,ticket_info[3],seatnum,ticket_info[5]))
        conn.commit()
        cursor.fetchall()
    except mysql.connector.errors.InterfaceError as success:  # 添加订单
        if str(success) == 'No result set to fetch from.':
            #下单成功，余票量减一
            cursor.execute('UPDATE ticket SET Sleft = Sleft - 1 WHERE Tnum = %s',(ticket_num,))
            conn.commit()
            closedatabse(cursor, conn)
            return orderid
def showorders(username):
    conn = mysql.connector.connect(user='root', password=password, database='ticket')
    cursor = conn.cursor()
    cursor.execute('select * from orders where Username=%s', (username,))
    orders=cursor.fetchall()
    closedatabse(cursor, conn)
    return orders
def tuipiao_order(orderid):
    conn = mysql.connector.connect(user='root', password=password, database='ticket')
    cursor = conn.cursor()
    cursor.execute('select * from orders where Orderid=%s', (orderid,))
    ticket_num=cursor.fetchall()[0][0]
    cursor.execute(' delete from orders where Orderid=%s', (orderid,))
    conn.commit()
    cursor.execute('UPDATE ticket SET Sleft = Sleft + 1 WHERE Tnum = %s', (ticket_num,))
    conn.commit()
    closedatabse(cursor, conn)