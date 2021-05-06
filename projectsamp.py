import pymysql as sql
import sys
import os
import time

# code for adding book **************************
def addBook():
    mycursor=conn.cursor()
    query="select bookid from books order by bookid desc limit 1"
    mycursor.execute(query)
    row=mycursor.fetchone()
    
    if mycursor.rowcount==0:
        bookno=1
    else:
        bookno=row["bookid"]
        bookno+=1
    print('Book ID :',bookno)
    bname=input('Enter Book Name:')
    author=input('Enter Author Name:')
    publisher=input('Enter Publisher Name:')
    booktype=input('Enter Book Type:')
    publyear=int(input('Enter Publish Year:'))
    nopage=int(input('Enter Number of Pages:'))
    nocopies=int(input('Enter No. of Copies:'))
    query="insert into books values({},'{}','{}','{}','{}',{},{},{})"
    mycursor.execute(query.format(bookno,bname,author,publisher,booktype,publyear,nopage,nocopies))
    resp=input('Do you want to Save Book(Y/N)?')
    if resp in ['Y','y']:
        conn.commit()
        print('Book Save sucessfully!!!')
    else:
        conn.rollback()
        print('No Records Saved!!!')

#code for modifying book **************************
def modiBook():
    mycursor=conn.cursor()
    bookno=int(input('Enter Book ID:'))
    query="select * from books where bookid={}"
    mycursor.execute(query.format(bookno))
    count=mycursor.rowcount
    if count==0:
        print('Book ID ',bookno,' Not Found!!!')
    else:
        print('Book ID ',bookno,'has Following Details:')
        rows=mycursor.fetchall()
        for row in rows:
            print("BOOK NO         :",row["bookid"])
            print("BOOK NAME       :",row["bname"])
            print("AUTHOR          :",row["author"])
            print("PUBLISHER       :",row["publisher"])
            print("BOOK TYPE       :",row["btype"])
            print("PUBLISH YEAR    :",row["pubyear"])
            print("NUMBER OF PAGES :",row["nop"])
            print("NUMBER OF COPIES:",row["noc"])
            print('------------------------------------------------------')
        c=input('Do You Want to Change Book(Y/N)?')
        if c in ['Y','y']:
            bname=input('Enter Book Name:')
            author=input('Enter Author Name:')
            publisher=input('Enter Publisher Name:')
            booktype=input('Enter Book Type:')
            publyear=int(input('Enter Publish Year:'))
            nopage=int(input('Enter Number of Pages:'))
            nocopies=int(input('Enter No. of Copies:'))
            query="update books set bname='{}',author='{}',publisher='{}',btype='{}',pubyear={},nop={},noc={} where bookid={}"
            mycursor.execute(query.format(bname,author,publisher,booktype,publyear,nopage,nocopies,bookno))
            conn.commit()
            print('Book Changed sucessfully!!!')
        else:
            conn.rollback()
            print('No Records Changed!!!')
    
#code for deleting book **************************
def delBook():
    mycursor=conn.cursor()
    bookno=int(input('Enter Book ID:'))
    query="select * from books where bookid={}"
    mycursor.execute(query.format(bookno))
    count=mycursor.rowcount
    if count==0:
        print('Book ID ',bookno,' Not Found!!!')
    else:
        print('Book ID ',bookno,'has Following Details:')
        rows=mycursor.fetchall()
        for row in rows:
            print("BOOK NO         :",row["bookid"])
            print("BOOK NAME       :",row["bname"])
            print("AUTHOR          :",row["author"])
            print("PUBLISHER       :",row["publisher"])
            print("BOOK TYPE       :",row["btype"])
            print("PUBLISH YEAR    :",row["pubyear"])
            print("NUMBER OF PAGES :",row["nop"])
            print("NUMBER OF COPIES:",row["noc"])
            print('------------------------------------------------------')
        c=input('Do You Want to Delete(Y/N)?')
        if c in ['Y','y']:
            query="delete from books where bookid={}"
            mycursor.execute(query.format(bookno))
            conn.commit()
            print('Book Deleted sucessfully!!!')
        else:
            conn.rollback()
            print('No Records Deleted!!!')

# code for adding member *******************
def addMember():
    mycursor=conn.cursor()
    query="select memberid from member order by memberid desc limit 1"
    mycursor.execute(query)
    row=mycursor.fetchone()
    
    if mycursor.rowcount==0:
        memberno=1001
    else:
        memberno=row["memberid"]
        memberno+=1
    print('Member ID :',memberno)
    mname=input('Enter Member Name:')
    addr=input('Enter Address:')
    mobile=input('Enter Mobile Number:')
    query="insert into member values({},'{}','{}','{}')"
    mycursor.execute(query.format(memberno,mname,addr,mobile))
    resp=input('Do you want to Save Member(Y/N)?')
    if resp in ['Y','y']:
        conn.commit()
        print('Member Save sucessfully!!!')
    else:
        conn.rollback()
        print('No Records Saved!!!')

#code for modifying member *********************     
def modiMember():
    mycursor=conn.cursor()
    memberno=int(input('Enter Member ID:'))
    query="select * from member where memberid={}"
    mycursor.execute(query.format(memberno))
    count=mycursor.rowcount
    if count==0:
        print('Member ID ',memberno,' Not Found!!!')
    else:
        print('Member ID ',memberno,'has Following Details:')
        rows=mycursor.fetchall()
        for row in rows:
            print("MEMBER NO         :",row["memberid"])
            print("MEMBER NAME       :",row["mname"])
            print("ADDRESS           :",row["address"])
            print("MOBILE NUMBER     :",row["mobileno"])
            print('------------------------------------------------------')
        c=input('Do You Want to Change Book(Y/N)?')
        if c in ['Y','y']:
            mname=input('Enter Member Name:')
            addr=input('Enter Address:')
            mobile=input('Enter Mobile Number:')
            query="update member set mname='{}',address='{}',mobileno='{}' where memberid={}"
            mycursor.execute(query.format(mname,addr,mobile,memberno))
            conn.commit()
            print('Member Changed sucessfully!!!')
        else:
            conn.rollback()
            print('No Records Changed!!!')

# code for delete member ******************
def delMember():
    mycursor=conn.cursor()
    memberno=int(input('Enter Member ID:'))
    query="select * from member where memberid={}"
    mycursor.execute(query.format(memberno))
    count=mycursor.rowcount
    if count==0:
        print('Member ID ',memberno,' Not Found!!!')
    else:
        print('Member ID ',memberno,'has Following Details:')
        rows=mycursor.fetchall()
        for row in rows:
            print("MEMBER NO         :",row["memberid"])
            print("MEMBER NAME       :",row["mname"])
            print("ADDRESS           :",row["address"])
            print("MOBILE NUMBER     :",row["mobileno"])
            print('------------------------------------------------------')
        c=input('Do You Want to Delete Member(Y/N)?')
        if c in ['Y','y']:
            query="delete from member where memberid={}"
            mycursor.execute(query.format(memberno))
            conn.commit()
            print('Member Deleted sucessfully!!!')
        else:
            conn.rollback()
            print('No Records Deleted!!!')

#code for issue book ****************
def issueBook():
    mycursor=conn.cursor()
    memberno=int(input('Enter Member ID:'))
    query="select * from member where memberid={}"
    mycursor.execute(query.format(memberno))
    count=mycursor.rowcount
    if count==0:
        print('Member ID ',memberno,' Not Found!!!')
    else:
        print('Member ID ',memberno,'has Following Details:')
        rows=mycursor.fetchall()
        for row in rows:
            print("MEMBER NO         :",row["memberid"])
            print("MEMBER NAME       :",row["mname"])
            print("ADDRESS           :",row["address"])
            print("MOBILE NUMBER     :",row["mobileno"])
            print('------------------------------------------------------')
        bookno=int(input('Enter Book ID:'))
        query="select * from books where bookid={}"
        mycursor.execute(query.format(bookno))
        cont=mycursor.rowcount
        if cont==0:
            print('Book ID ',bookno,' Not Found!!!!')
        else:
            doi=input('Enter Date of Issue(YYYY-MM-DD):')
            c=input('Do You Want to Issue Book(Y/N)?')
            mycursor.execute("select * from trans")
            cnt=mycursor.rowcount
            if cnt==0:
                trid=1
            else:
                trid=cnt+1
            if c in ['Y','y']:
                query="insert into trans values({},{},{},'{}',null)"
                mycursor.execute(query.format(trid,memberno,bookno,doi))
                query="update books set noc=noc-1 where bookid={}"
                mycursor.execute(query.format(bookno))
                conn.commit()
                print('Book Issued Sucessfully!!!')
            else:
                conn.rollback()
                print('No Book Issued!!!')

# code for return book *******************
def returnBook():
    mycursor=conn.cursor()
    memberno=int(input('Enter Member ID:'))
    query="select * from trans where memberid={} and dateret is null"
    mycursor.execute(query.format(memberno))
    count=mycursor.rowcount
    if count==0:
        print('Member ID ',memberno,' Has No Book Issued!!!')
    else:
        print('Member ID ',memberno,'Issued Book Details:')
        rows=mycursor.fetchall()
        for row in rows:
            print("TRANSACTION ID    :",row["transid"])
            print("MEMBER NO         :",row["memberid"])
            print("BOOK ID           :",row["bookid"])
            print("ISSUE DATE        :",row["dateiss"])
            print('------------------------------------------------------')
        c=input('Do You Want to Return Book(Y/N)?')
        
        if c in ['Y','y']:
                bookno=input('Enter Book ID to be Returned:')
                retd=input('Enter Return Date (YYYY-MM-DD):')
                query="update trans set dateret='{}' where memberid={} and bookid={} and dateret is null and dateiss<='{}'"
                mycursor.execute(query.format(retd,memberno,bookno,retd))
                if mycursor.rowcount==0:
                    print("Date of Issue Must be Less Than Date of Return!!!/Wrong Book ID!!!")
                else:
                    query="update books set noc=noc+1 where bookid={}"
                    mycursor.execute(query.format(bookno))
                    conn.commit()
                    print('Book Returned Sucessfully!!!')
        else:
            conn.rollback()
            print('No Book Returned!!!')

# code for Lost book *******************
def lostBook():
    print('You Have to Submit a New Book for for book you have Lost!!!')
    c=input('Do You Want to Submit(Y/N)?')
    if c in ['Y','y']:
        mycursor=conn.cursor()
        memberno=int(input('Enter Member ID:'))
        query="select * from trans where memberid={} and dateret is null"
        mycursor.execute(query.format(memberno))
        count=mycursor.rowcount
        if count==0:
            print('Member ID ',memberno,' Has No Book Issued!!!')
        else:
            print('Member ID ',memberno,'Issued Book Details:')
            rows=mycursor.fetchall()
            for row in rows:
                print("TRANSACTION ID    :",row["transid"])
                print("MEMBER NO         :",row["memberid"])
                print("BOOK ID           :",row["bookid"])
                print("ISSUE DATE        :",row["dateiss"])
                print('------------------------------------------------------')
            bookno=input('Enter Book ID to be Returned for Lost:')
            retd=input('Enter Return Date (YYYY-MM-DD):')
            query="update trans set dateret='{}' where memberid={} and bookid={} and dateret is null and dateiss<='{}'"
            mycursor.execute(query.format(retd,memberno,bookno,retd))
            if mycursor.rowcount==0:
                print("Date of Issue Must be Less Than Date of Return!!!/Wrong Book ID!!!")
                conn.rollback()
            else:
                query="update books set noc=noc+1 where bookid={}"
                mycursor.execute(query.format(bookno))
                conn.commit()
                print('Book Replaced Sucessfully!!!')
    else:
        print('No Book Replaced!!!')

# code for Queries all books **************
def qallBooks():
    mycursor=conn.cursor()
    query="select * from books order by bname asc"
    mycursor.execute(query)
    count=mycursor.rowcount
    if count==0:
        print('No Book Found!!!')
    else:
        print('Books Details are:')
        rows=mycursor.fetchall()
        print("BOOK NO".ljust(7),"BOOK NAME".ljust(25),"AUTHOR".ljust(25),"PUBLISHER".ljust(25),"BOOK TYPE".ljust(20),"PUBLISH YEAR".center(4),"PAGES".center(4),"COPIES".center(3))
        print(132*'=')
        ctr=1
        for row in rows:
            print(str(row["bookid"]).ljust(7),str(row["bname"]).ljust(25),str(row["author"]).ljust(25),str(row["publisher"]).ljust(25),str(row["btype"]).ljust(20),str(row["pubyear"]).center(12),str(row["nop"]).center(4),str(row["noc"]).center(3))
            ctr+=1
            if ctr%30==0:
                input('Press any key to see more...')
                print("BOOK NO".ljust(7),"BOOK NAME".ljust(25),"AUTHOR".ljust(25),"PUBLISHER".ljust(25),"BOOK TYPE".ljust(20),"PUBLISH YEAR".center(4),"PAGES".center(4),"COPIES".center(3))
                print(132*'=')
                
# code for name wise book
def qnamewiseBook():
    mycursor=conn.cursor()
    bkname=input('Enter Book Name:')
    query="select * from books where lower(bname) like '%{}%'"
    mycursor.execute(query.format(bkname))
    count=mycursor.rowcount
    if count==0:
        print('No Book Found!!!')
    else:
        print('Books Details are:')
        rows=mycursor.fetchall()
        print("BOOK NO".ljust(7),"BOOK NAME".ljust(25),"AUTHOR".ljust(25),"PUBLISHER".ljust(25),"BOOK TYPE".ljust(20),"PUBLISH YEAR".center(4),"PAGES".center(4),"COPIES".center(3))
        print(132*'=')
        ctr=1
        for row in rows:
            print(str(row["bookid"]).ljust(7),str(row["bname"]).ljust(25),str(row["author"]).ljust(25),str(row["publisher"]).ljust(25),str(row["btype"]).ljust(20),str(row["pubyear"]).center(12),str(row["nop"]).center(4),str(row["noc"]).center(3))
            ctr+=1
            if ctr%30==0:
                input('Press any key to see more...')
                print("BOOK NO".ljust(7),"BOOK NAME".ljust(25),"AUTHOR".ljust(25),"PUBLISHER".ljust(25),"BOOK TYPE".ljust(20),"PUBLISH YEAR".center(4),"PAGES".center(4),"COPIES".center(3))
                print(132*'=')

# code for publisher wise
def qpublisherBook():
    mycursor=conn.cursor()
    pbname=input('Enter Publisher Name:')
    query="select * from books where lower(publisher) like '%{}%'"
    mycursor.execute(query.format(pbname))
    count=mycursor.rowcount
    if count==0:
        print('No Book Found!!!')
    else:
        print('Books Details are:')
        rows=mycursor.fetchall()
        print("BOOK NO".ljust(7),"BOOK NAME".ljust(25),"AUTHOR".ljust(25),"PUBLISHER".ljust(25),"BOOK TYPE".ljust(20),"PUBLISH YEAR".center(4),"PAGES".center(4),"COPIES".center(3))
        print(132*'=')
        ctr=1
        for row in rows:
            print(str(row["bookid"]).ljust(7),str(row["bname"]).ljust(25),str(row["author"]).ljust(25),str(row["publisher"]).ljust(25),str(row["btype"]).ljust(20),str(row["pubyear"]).center(12),str(row["nop"]).center(4),str(row["noc"]).center(3))
            ctr+=1
            if ctr%30==0:
                input('Press any key to see more...')
                print("BOOK NO".ljust(7),"BOOK NAME".ljust(25),"AUTHOR".ljust(25),"PUBLISHER".ljust(25),"BOOK TYPE".ljust(20),"PUBLISH YEAR".center(4),"PAGES".center(4),"COPIES".center(3))
                print(132*'=')    
            


def qtypeBook():
    mycursor=conn.cursor()
    bt=input('Enter Book Type:')
    query="select * from books where lower(btype) like '%{}%'"
    mycursor.execute(query.format(bt))
    count=mycursor.rowcount
    if count==0:
        print('No Book Found!!!')
    else:
        print('Books Details are:')
        rows=mycursor.fetchall()
        print("BOOK NO".ljust(7),"BOOK NAME".ljust(25),"AUTHOR".ljust(25),"PUBLISHER".ljust(25),"BOOK TYPE".ljust(20),"PUBLISH YEAR".center(4),"PAGES".center(4),"COPIES".center(3))
        print(132*'=')
        ctr=1
        for row in rows:
            print(str(row["bookid"]).ljust(7),str(row["bname"]).ljust(25),str(row["author"]).ljust(25),str(row["publisher"]).ljust(25),str(row["btype"]).ljust(20),str(row["pubyear"]).center(12),str(row["nop"]).center(4),str(row["noc"]).center(3))
            ctr+=1
            if ctr%30==0:
                input('Press any key to see more...')
                print("BOOK NO".ljust(7),"BOOK NAME".ljust(25),"AUTHOR".ljust(25),"PUBLISHER".ljust(25),"BOOK TYPE".ljust(20),"PUBLISH YEAR".center(4),"PAGES".center(4),"COPIES".center(3))
                print(132*'=')

# code for all members****************
def qallMembers():
    mycursor=conn.cursor()
    query="select * from member order by mname asc"
    mycursor.execute(query)
    count=mycursor.rowcount
    if count==0:
        print('No Member Found!!!')
    else:
        print('Member Details are:')
        rows=mycursor.fetchall()
        print("MEMBER NO".rjust(7),"MEMBER NAME".ljust(25),"ADDRESS".ljust(25),"MOBILE NUMBER".ljust(13))
        print(80*'=')
        ctr=1
        for row in rows:
            print(str(row["memberid"]).rjust(7),str(row["mname"]).ljust(25),str(row["address"]).ljust(25),str(row["mobileno"]).rjust(13))
            ctr+=1
            if ctr%30==0:
                input('Press any key to see more...')
                print("MEMBER NO".rjust(7),"MEMBER NAME".ljust(25),"ADDRESS".ljust(25),"MOBILE NUMBER".ljust(13))
                print(80*'=')

# code for Member id wise
def qmemNumber():
    mycursor=conn.cursor()
    query="select * from member where memberid={}"
    memno=int(input('Enter Member ID:'))
    mycursor.execute(query.format(memno))
    count=mycursor.rowcount
    if count==0:
        print('No Member Found!!!')
    else:
        print('Member Details are:')
        rows=mycursor.fetchall()
        print("MEMBER NO".rjust(7),"MEMBER NAME".ljust(25),"ADDRESS".ljust(25),"MOBILE NUMBER".ljust(13))
        print(80*'=')
        ctr=1
        for row in rows:
            print(str(row["memberid"]).rjust(7),str(row["mname"]).ljust(25),str(row["address"]).ljust(25),str(row["mobileno"]).rjust(13))
            ctr+=1
            if ctr%30==0:
                input('Press any key to see more...')
                print("MEMBER NO".rjust(7),"MEMBER NAME".ljust(25),"ADDRESS".ljust(25),"MOBILE NUMBER".ljust(13))
                print(80*'=')

# code for Member Name wise
def qmemName():
    mycursor=conn.cursor()
    query="select * from member where mname like '%{}%'"
    memname=input('Enter Member Name:')
    mycursor.execute(query.format(memname))
    count=mycursor.rowcount
    if count==0:
        print('No Member Found!!!')
    else:
        print('Member Details are:')
        rows=mycursor.fetchall()
        print("MEMBER NO".rjust(7),"MEMBER NAME".ljust(25),"ADDRESS".ljust(25),"MOBILE NUMBER".ljust(13))
        print(80*'=')
        ctr=1
        for row in rows:
            print(str(row["memberid"]).rjust(7),str(row["mname"]).ljust(25),str(row["address"]).ljust(25),str(row["mobileno"]).rjust(13))
            ctr+=1
            if ctr%30==0:
                input('Press any key to see more...')
                print("MEMBER NO".rjust(7),"MEMBER NAME".ljust(25),"ADDRESS".ljust(25),"MOBILE NUMBER".ljust(13))
                print(80*'=')
        
# Code for Query of Member for Transaction
def qtransMember():
    mycursor=conn.cursor()
    query="select * from trans where memberid={}"
    memno=int(input('Enter Member ID:'))
    mycursor.execute(query.format(memno))
    count=mycursor.rowcount
    if count==0:
        print('No Member Found!!!')
    else:
        print('Member Details are:')
        rows=mycursor.fetchall()
        print("TRANSACTION NO".rjust(15),"MEMBER NUMBER".center(12),"BOOK NUMBER".center(12),"ISSUE DATE".ljust(12),"RETURN DATE".ljust(12))
        print(90*'=')
        ctr=1
        for row in rows:
            print(str(row["transid"]).rjust(15),str(row["memberid"]).rjust(12),str(row["bookid"]).rjust(12),str(row["dateiss"]).center(12),str(row["dateret"]).center(12))
            ctr+=1
            if ctr%30==0:
                input('Press any key to see more...')
                print("TRANSACTION NO".rjust(7),"MEMBER NUMBER".center(10),"BOOK NUMBER".center(10),"ISSUE DATE".ljust(12),"RETURN DATE".ljust(12))
                print(90*'=')

# code for how to use
def howtoUse():
    print('\n\n\n\n\nInstruction to use Library Software......')
    print('Using Book menu, you can add new book, change details and remove book.')
    print('Using Member menu, you can add new member, change member details and remove member')
    print('Using Transaction menu, you can do Issue, Return and Lost book processing')
    print('Using Queries, you can perform various queries based on Books, Members and Transactions')
    print('Using Utilities, you can run Calcullator, Notepad and Paint Program of Windows')
    print('Thank You.....')
    
def mainmenu():
    print('\n\n\n\n~~~~~~~~~~~~~~~~')
    print('M A I N   M E N U')
    print('*****************')
    print('1.Book Menu.......')
    print('2.Member Menu.....')
    print('3.Transactions....')
    print('4.Queries.........')
    print('5.Utilities.......')
    print('6.Help............')
    print('7.Exit............')
    ch=int(input('Enter Your Choice:'))
    if ch==1:
        print('\n*****************')
        print('B O O K    M E N U')
        print('##################')
        print('1.Add New Book....')
        print('2.Modify Book.....')
        print('3.Delete Book.....')
        print('4.Back to Main....')
        ch1=int(input('Enter Your Choice:'))
        if ch1==1:
            addBook()
        elif ch1==2:
            modiBook()
        elif ch1==3:
            delBook()
        elif ch1==4:
            mainmenu()
        else:
            print('Wrong Choice!!!, Back to Main')
            mainmenu()
    elif ch==2:
        print('\n*******************')
        print('M E M B E R   M E N U')
        print('#####################')
        print('1.Add New Member....')
        print('2.Modify Member.....')
        print('3.Delete Member.....')
        print('4.Back to Main....')
        ch1=int(input('Enter Your Choice:'))
        if ch1==1:
            addMember()
        elif ch1==2:
            modiMember()
        elif ch1==3:
            delMember()
        elif ch1==4:
            mainmenu()
        else:
            print('Wrong Choice!!!, Back to Main')
            mainmenu()
    elif ch==3:
        print('\n*****************************')
        print('T R A N S A C T I O N   M E N U')
        print('###############################')
        print('1.Issue Book....')
        print('2.Return Book.....')
        print('3.Lost Book.....')
        print('4.Back to Main....')
        ch1=int(input('Enter Your Choice:'))
        if ch1==1:
            issueBook()
        elif ch1==2:
            returnBook()
        elif ch1==3:
            lostBook()
        elif ch1==4:
            mainmenu()
        else:
            print('Wrong Choice!!!, Back to Main')
            mainmenu()
    elif ch==4:
        print('\n*****************')
        print('Q U E R Y   M E N U')
        print('###################')
        print('-------Books---------')
        print('1.All Books Alphabetical')
        print('2.Specific Book Name Wise')
        print('3.Book Publisher Wise')
        print('4.Type Wise')
        print('-------Member------------')
        print('5.All Members Alphabetical')
        print('6.Member Number Wise')
        print('7.Member Name Wise')
        print('8.Transaction for Member')
        print('9.Back to Main....')
        ch1=int(input('Enter Your Choice:'))
        if ch1==1:
            qallBooks()
        elif ch1==2:
            qnamewiseBook()
        elif ch1==3:
            qpublisherBook()
        elif ch1==4:
            qtypeBook()
        elif ch1==5:
            qallMembers()
        elif ch1==6:
            qmemNumber()
        elif ch1==7:
            qmemName()
        elif ch1==8:
            qtransMember()
        elif ch1==9:
            mainmenu()
        else:
            print('Wrong Choice!!!, Back to Main')
            mainmenu()
    elif ch==5:
        print('\n*********************')
        print('U T I L I T Y   M E N U')
        print('#######################')
        print('1.Calculator....')
        print('2.Notepad.......')
        print('3.Paint.........')
        print('4.Back to Main....')
        ch1=int(input('Enter Your Choice:'))
        if ch1==1:
            os.system('calc')
        elif ch1==2:
            os.system('notepad')
        elif ch1==3:
            os.system('mspaint')
        elif ch1==4:
            mainmenu()
        else:
            print('Wrong Choice!!!, Back to Main')
            mainmenu()
        
    elif ch==6:
        howtoUse()
    elif ch==7:
        status=input('Dou you realy want to Quit/Exit(Y/N)...?')
        if status in ['Y','y']:
            sys.exit()
        else:
            pass
            
    else:
        print('Wrong Choice!!! Try Again!!!')
    
conn=sql.connect(user='root',password='123',host='localhost',database='libdata',cursorclass=sql.cursors.DictCursor)
while True:
    mainmenu()
