import pymysql as sql
import time
conn=sql.connect(user='root',password='123',host='localhost')
mycursor=conn.cursor()
choice=input('Do You Want To Create Environment for Library Software (Y/N)?')
if choice in ['Y','y']:
    print('\n\n\n\n\n\nMaking Connection with MySQL.',end='')
    for i in range(1,20):
        print('.', end='')
        time.sleep(.5)
    print('Done!!!')
    mycursor.execute('create database if not exists libdata')
    conn=sql.connect(user='root',password='123',host='localhost',database='libdata')
    print('Creating Database.', end='')
    for i in range(1,10):
        print('#', end='')
        time.sleep(.5)
    print('Done!!!')
    mycursor.execute('use libdata')
    print('Opening Database.',end='')
    for i in range(1,15):
        print('◆', end='')
        time.sleep(.5)
    print('Done!!!')
    mycursor.execute('create table if not exists books(bookid int(7) primary key,bname varchar(25), author varchar(25), publisher varchar(25), btype varchar(20), pubyear int(4),nop int(4), noc int(3))')
    mycursor.execute('create table if not exists member(memberid int(7) primary key,mname varchar(25), address varchar(25), mobileno varchar(13))')
    mycursor.execute('create table if not exists trans(transid int(7) primary key,memberid int(7),bookid int(7),dateiss date, dateret date)')    
    print('Creating Tables.....')
    for i in range(1,40):
        print('■', end='')
        if i==12:
            print('Book Table Created..')
        if i==16:
            print('Member Table Created..')
        if i==36:
            print('Transaction Table Created..')
        time.sleep(.5)
    print('Done!!!')
    print('Complete Environment for Library Software is Ready.......')
else:
    print('Exiting........')
    
