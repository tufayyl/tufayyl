import mysql.connector as ms
import time
mydb=ms.connect (host='localhost', user='root',  password='sis@12345', database='library123')
mc=mydb.cursor()

def register():
    print()
    print()

    def makeacc():
        ch = 'y'
        while ch in 'yY':
            a = input('Enter New 4-digit CustomerID : ')   
            b = input('Enter New UserName           : ')   
            c = input('Enter New Password           : ')
        
            try:
                mc.execute("INSERT INTO customermaster (CustomerNo,Username,Password) VALUES(%s,%s,%s)",(a,b,c))
                mydb.commit()
                print()
                print(" ----- Account Created  ----- ")
                print('You can now use this account to rent books')
            except:
                print(" !!! Account Not Created (TRY CHANGING CustomerID) !!!  ")
                mydb.rollback()
                
            print()
            ch = input('\nDo you want to add another account ? (y/n) :')



    print()
    print()
            
    if not mydb.is_connected():
        print('Could not connect to database Assignment')
        print('Exiting ......')
        time.sleep(3)
        exit()
    else:
        print('\n')
        mc=mydb.cursor()
        makeacc()


def login():
    global mc
    print()

    def seebooks():
        mc.execute('Select BookID, BookName, BookPrice, Author, LanguageName from bookmaster, booklanguages where status = "In Inventory" and bookmaster.LanguageID = booklanguages.LanguageID')
        data = mc.fetchall()
        print('\n\n---   BOOKS AVAILABLE TO RENT IN LIBRARY   --- ')
        print()

        if mc.rowcount>0:
            print('%6s'%'BookID','%25s'%'BookName','%15s'%'BookPrice','%15s'%'Author','%15s'%'Language')
            print('='*80)
            for i in data:
                print('%6s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3],'%15s'%i[4])
            print('='*80)

    def namesearch():
        print()
        query = """SELECT * from bookmaster where BookName = %s"""
        bookname =input('Enter THE Book\'s Name:  ')
        print()
        mc.execute(query, (bookname,))
        data=mc.fetchall()
        if mc.rowcount>0:
            print('%6s'%'BookID','%15s'%'BookName','%15s'%'BookPrice','%15s'%'Author','%15s'%'LanguageID')
            print('-'*70)
            for i in data:
                print('%6s'%i[0],'%15s'%i[1], '%15s'%i[2], '%15s'%i[3],'%15s'%i[4])
            print('-'*70)
        else:
            print('\n* * * The Book you Searched for isnt Availible * * * ')

    def languagesort():
        print()
        #Enlgish books
        mc.execute('Select BookID, BookName, BookPrice, Author, Status from bookmaster where LanguageID = "909"')
        data = mc.fetchall()
        print('\n\n---   English Books   --- ')
        if mc.rowcount>0:
            print('%7s'%'BookID','%25s'%'BookName','%15s'%'BookPrice','%15s'%'Author','%15s'%'Status')
            print('='*80)
            for i in data:
                print('%7s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3],'%15s'%i[4])
            print('='*80)
        #Hindi books
        mc.execute('Select BookID, BookName, BookPrice, Author, Status from bookmaster where LanguageID = "707"')
        data = mc.fetchall()
        print('\n\n---   Hindi Books   --- ')
        if mc.rowcount>0:
            print('%7s'%'BookID','%25s'%'BookName','%15s'%'BookPrice','%15s'%'Author','%15s'%'Status')
            print('='*80)
            for i in data:
                print('%7s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3],'%15s'%i[4])
            print('='*80)
        #Spanish books
        mc.execute('Select BookID, BookName, BookPrice, Author, Status from bookmaster where LanguageID = "808"')
        data = mc.fetchall()
        print('\n\n---   Spanish Books   --- ')
        if mc.rowcount>0:
            print('%7s'%'BookID','%25s'%'BookName','%15s'%'BookPrice','%15s'%'Author','%15s'%'Status')
            print('='*80)
            for i in data:
                print('%7s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3],'%15s'%i[4])
            print('='*80)
        #Spanish books
        mc.execute('Select BookID, BookName, BookPrice, Author, Status from bookmaster where LanguageID = "606"')
        data = mc.fetchall()
        print('\n\n---   Russian Books   --- ')
        if mc.rowcount>0:
            print('%7s'%'BookID','%25s'%'BookName','%15s'%'BookPrice','%15s'%'Author','%15s'%'Status')
            print('='*80)
            for i in data:
                print('%7s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3],'%15s'%i[4])
            print('='*80)

    def bookidsearch():
        print()
        r=input('Enter THE BOOKID: ')
        print('-'*80)
        mc.execute('Select * from bookmaster where BookID={}'.format(r))
        data=mc.fetchall()
        if mc.rowcount>0:
            print('%6s'%'BookID','%25s'%'BookName','%20s'%'BookPrice','%20s'%'Author')
            print('-'*80)
            for i in data:
                print('%6s'%i[0],'%25s'%i[1], '%20s'%i[2], '%20s'%i[3])
            print('-'*80)
        else:
            print('\n* * * The Book you Searched for isnt Availible * * * ')
        

    def searchmethods():
        cnn= int(input('''
1) SEARCH BY NAME
2) SORT AS LANGUAGE
3) SEARCH WITH BOOK ID  
.
.
ENTER YOUR CHOICE :  ''' ))
        if cnn==1:
            namesearch()
        elif cnn==2:
            languagesort()
        elif cnn==3:
            bookidsearch()   

        else:
            print('INVALID OPTION PLEASE ENTER A VALID OPTION')
            print('\n')
            searchmethods()

    def renttype():
        while True:
            eee=int(input(''' 
1. RENT WITH WITH BOOK NAME
2. RENT WITH BOOKID
0. GO BACK
\n \n ENTER YOUR CHOICE : '''))
            if eee==1:
                rentusingname()
            elif eee==2:
                rentbook()
            elif eee==0:
                break 
            else:
                print('PLEASE ENTER A VALID OPTION')



    def rentbook():
        print()
        ch = 'y'
        while ch in 'yY':
            bid= input('ENTER THE BOOK ID OF THE BOOK YOU WANT TO RENT :  ')
            sta = "In Inventory"
            f = '''select BookName from bookmaster where BookID = %s and  Status= %s'''
            mc.execute(f, (bid,sta))
            data=mc.fetchall()
            if mc.rowcount>0:
                for i in data:
                    bn =i[0]
                    print()
                    c = input('ENTER THE RENT START DATE (YYYY-MM-DD) : ')
                    d = input('ENTER THE RENT END DATE (YYYY-MM-DD) : ')
                    print()
                    if d > c :
                        try:
                            mc.execute("INSERT INTO bookrentissuance (CustomerNo,CustomerName, BookID ,BookName, RentStartDate , RentEndDate ) VALUES(%s,%s,%s,%s,%s,%s)",(strq,userrr,bid,bn,c,d))
                            mydb.commit()
                            print(" ----- BOOK HAS BEEN RENTED (ANY DAMAGES CAUSED TO THE BOOK WILL BE FINED)  ----- \n \n ")
                            mc.execute("UPDATE bookmaster SET Status= 'Rented' WHERE BookID={}".format(bid))
                            mydb.commit()
                        except:
                            print(" ERROR OCCURED !!!!! PLEASE TRY AGAIN ")
                            mydb.rollback()
                    else:
                        print('----- Please enter VALID rent dates ------ ')
                break
            else:
                print()
                print('The Book You Chose Has Already Been rented OR The BookID You Chose Does Not Exist ')   
                print()

    def rentusingname():
        print()
        ch = 'y'
        while ch in 'yY':
            bid= input('ENTER THE BOOK NAME OF THE BOOK YOU WANT TO RENT :  ').title()
            sta = "In Inventory"
            f = '''select BookID from bookmaster where BookName = %s  and  Status= %s '''
            mc.execute(f, (bid,sta))
            data=mc.fetchall()
            if mc.rowcount>0:
                for i in data:
                    bn =i[0]
                    print()
                    c = input('ENTER THE RENT START DATE (YYYY-MM-DD) : ')
                    d = input('ENTER THE RENT END DATE (YYYY-MM-DD) : ')
                    print()
                    if d > c :
                        try:
                            mc.execute("INSERT INTO bookrentissuance (CustomerNo,CustomerName, BookID ,BookName, RentStartDate , RentEndDate ) VALUES(%s,%s,%s,%s,%s,%s)",(strq,userrr,bn,bid,c,d))
                            mydb.commit()
                            print(" ----- BOOK HAS BEEN RENTED (ANY DAMAGES CAUSED TO THE BOOK WILL BE FINED)  ----- \n \n ")
                            mc.execute("UPDATE bookmaster SET Status= 'Rented' WHERE BookID={}".format(bn))
                            mydb.commit()
                        except:
                            print(" ERROR OCCURED !!!!! PLEASE TRY AGAIN ")
                            mydb.rollback()
                    else:
                        print('----- Please enter VALID rent dates ------ ')        
                break
            else:
                print()
                print('----The Book You Chose Has Already Been rented OR The BookName You Chose Does Not Exist  ---')   
                print()           

    def givebook():
            print()
            ch = 'y'
            while ch in 'yY':
                quer3 = """select BookID from bookrentissuance WHERE CustomerNo =%s"""
                mc.execute(quer3,(strq,))
                dattta=mc.fetchall()
                if mc.rowcount>0:
                    for i in dattta:
                        bn =i[0]
                        try:
                            f = ''' DELETE FROM bookrentissuance WHERE CustomerName= %s'''
                            mc.execute(f, (userrr,))
                            mydb.commit()
                            jk = """UPDATE bookmaster SET Status= 'In Inventory' WHERE BookID = %s"""
                            mc.execute(jk, (bn,))
                            mydb.commit()
                            print("-----THE BOOK HAS BEEN RETURNED-----")
                            
                        except:
                            print(" ERROR OCCURED !!!!! PLEASE TRY AGAIN ")
                            mydb.rollback()
                    break
                else:
                        print()
                        print('----YOU HAVENT RENTED ANY BOOKS ---')   
                        print()
                        break
                
                

    while True:

        userrr=input("ENTER YOUR CUSTOMER USERNAME : ")
        pasd=input('ENTER YOUR CUSTOMER PASSWORD : ')
        query = """SELECT * from customermaster where Username = %s and  Password = %s"""
        mc.execute(query, (userrr,pasd))
        datta=mc.fetchall()
        if mc.rowcount>0:
            print('-'*70)
            print('                          ACCESS GRANTED')
            print('-'*70)
        
        
            if not mydb.is_connected():
                                print('Could not connect to database Assignment')
                                print('Exiting ......')
                                time.sleep(3)
                                exit() 
            else :

                print('\n')
                mc=mydb.cursor()
                ch='y'
                while ch in 'Yy':
                    print()
                    print('''
1. SEE THE BOOKS THAT ARE CURRENTLY AVAILABLE
2. SEARCH FOR A BOOK
3. RENT A BOOK
4. RETURN A BOOK
0. GO BACK 
''')
                    queryy = """select CustomerNo from customermaster WHERE Username =%s"""
                    mc.execute(queryy,(userrr,))
                    datta=mc.fetchall()
                    for i in datta:
                        ltt=i
                    strq = ''.join(ltt)

                    cn=int(input('ENTER YOUR CHOICE :'))
                    if cn==1:
                        seebooks()

                    elif cn==2:
                        searchmethods()

                    elif cn==3:
                        renttype()

                    elif cn==4:
                        givebook()

                    elif cn==0:
                        mainmenu()

                    else:
                        print('INVALID OPTION , PLEASE ENTER A VALID OPTION \n \n')

        else :
            print()
            print ( '---There is no such account, please enter valid Credentials---')
            print()


def admin():
    def add():
        ch = 'y'
        while ch in 'yY':
            a = input('BookID : ')   
            b = input('BookName: ').title()
            c = input('BookPrice : ')
            d = input('Author :').title()
            e = input('LanguageID :')
            f = "In Inventory"
            try:
                mc.execute("INSERT INTO bookmaster (BookID, BookName, BookPrice, Author, LanguageID, Status) VALUES(%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f))
                mydb.commit()
                print(" ----- Record Saved ----- ")
            except:
                print(" !!! Record not Saved  !!!  ")
                mydb.rollback()
            print()
            ch = input('\nDo you want to add more Records ? ')
        
        print('\n------ BOOK ADDED SUCCESSFULLY  ------ ')
        print('\n')


    def delete():
        print()
        r=input('Enter BookID of book to be deleted : ')
        mc.execute('Delete from bookmaster where BookID = {}'.format(r))
        mydb.commit()
        print('The  has been deleted. ')
        print()


    def update():
        r=input('Enter BookID of the Book\'s status to be changed  : ')
        mc.execute('Select * from bookmaster where BookID={}'.format(r))
        data=mc.fetchall()
        print('Data to be changed : ', data) 
        A= input('Enter updated BookPrice: ')
        mc.execute("UPDATE bookmaster SET  BookPrice= '{}' where BookID = {}".format(A,r))
        mydb.commit()
        print()
        print('Record Updated')


    def status():

        # books in inventory
        mc.execute('Select BookID, BookName, BookPrice, LanguageID from bookmaster where status = "In Inventory"')
        data = mc.fetchall()
        print('\n\n---   BOOKS IN INVENTORY  --- ')
        print()

        if mc.rowcount>0:
            print('%6s'%'BookID','%25s'%'BookName','%15s'%'BookPrice','%15s'%'LanguageID')
            print('='*70)
            for i in data:
                print('%6s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3])
            print('='*70)

        # rented books
        mc.execute('Select BookID, BookName, BookPrice, LanguageID from bookmaster where status = "Rented"')
        data = mc.fetchall()
        print('\n\n---   BOOKS THAT ARE RENTED  --- ')
        if mc.rowcount>0:
            print('%6s'%'BookID','%25s'%'BookName','%15s'%'BookPrice','%15s'%'LanguageID')
            print('='*70)
            for i in data:
                print('%6s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3])
            print('='*70)

    def disp():
        mc.execute('Select * from bookmaster')
        data = mc.fetchall()
        print()
        if mc.rowcount>0:
            print('%7s'%'BookID,','%25s'%' BookName','%10s'%'BookPrice','%25s'%'Author','%15s'%'LanguageID','%15s'%'Status')
            print('='*100)
            for i in data:
                print('%7s'%i[0],'%25s'%i[1],'%10s'%i[2],'%25s'%i[3],'%15s'%i[4],'%15s'%i[5])
            print('='*100)
        else:
            print("No Books in inventory!!")


    def showbookissuance():
        mc.execute('Select * from bookrentissuance')
        data = mc.fetchall()
        print()
        if mc.rowcount>0:
            print('%7s'%'CustomerNo','%25s'%' CustomerName','%15s'%' BookID','%25s'%'BookName','%15s'%'RentStartDate','%15s'%'RentEndDate',)
            print('='*110)
            for i in data:
                print('%7s'%i[0],'%25s'%i[1],'%15s'%i[2],'%25s'%i[3],'%15s'%i[4],'%15s'%i[5])
            print('='*110)
        else:
            print("NO book has been rented!")


    def showbooklang():
        mc.execute('Select * from booklanguages')
        data = mc.fetchall()
        print()
        if mc.rowcount>0:
            print('%7s'%'LanguageID','%15s'%' LanguageName')
            print('='*27)
            for i in data:
                print('%7s'%i[0],'%15s'%i[1])
            print('='*27)
        else:
            print("No one has rented a book , All books are in available")

    def showacc():
        mc.execute('Select * from customermaster')
        data = mc.fetchall()
        print()
        if mc.rowcount>0:
            print('%7s'%'CustomerNo','%20s'%'Name','%15s'%'Password')
            print('='*50)
            for i in data:
                print('%7s'%i[0],'%23s'%i[1],'%13s'%i[2])
            print('='*50)
        else:
            print("No Accounts have been resgistered ")
            print(20*'-')


    print()
    print()
    print()
    while True:
        name=input('ENTER THE ADMIN\'s USERNAME : ' )
        pasd=input('ENTER THE ADMIN PASSWORD    : ')
        print()
        file=open("useridpass.txt", "r")
        for i in file:
            a,b=i.split(",")
            if (a==name and b==pasd):
                print('''                                               
                        ___  ______________________  ________  ___   _  _______________ 
                       / _ |/ ___/ ___/ __/ __/ __/ / ___/ _ \/ _ | / |/ /_  __/ __/ _ \\
===================   / __ / /__/ /__/ _/_\ \_\ \  / (_ / , _/ __ |/    / / / / _// // / =================== 
                     /_/ |_\___/\___/___/___/___/  \___/_/|_/_/ |_/_/|_/ /_/ /___/____/ 
''')
                print()
                print()
                print(" WELCOME TO THE ADMIN INTERFACE")
            
                if not mydb.is_connected():
                    print('Could not connect to database Assignment')
                    print('Exiting ......')
                    time.sleep(3)
                    exit() 
                else:
                    print('\n')
                    mc=mydb.cursor()
                    ch='y'
                    while ch in 'Yy':
                        print()
                        print('''
1. ADD BOOKS TO INVENTORY  
2. DISPLAY INVENTORY 
3. UPDATE PRICE OF BOOK  
4. DELETE BOOK FROM INVENTORY  
5. DISPLAY STATUS OF BOOKS  
6. DISPLAY BOOK ISSUANCE TABLE  
7. DISPLAY BOOK LANGUAGE IDs 
8. DISPLAY CUSTOMER ACCOUNT DETAILS 
0. GO BACK''')
                        op=int(input("\nEnter your choice: "))
                        if op==1:
                            add()

                        elif op==2:
                            disp()

                        elif op==3:
                            update()

                        elif op==4:
                            delete()

                        elif op==5:
                            status()

                        elif op==6:
                            showbookissuance() 

                        elif op==7:
                            showbooklang()  

                        elif op==8:
                            showacc()
                        elif op==0:
                            mainmenu() 
                        else:
                            print('Wrong choice')
            else :
                print ( '''There is no such account , please enter valid credentials.....
    
    . ''' )
def mainmenu():
    while True:
        if not mydb.is_connected():
            print('Could not connect to database Assignment')
            print('Exiting ......')
            time.sleep(3)
            exit() 
        else :

            print('''
    ██████╗ ██╗  ██╗██████╗     ██╗     ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗
    ██╔══██╗╚██╗██╔╝██╔══██╗    ██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██║  ██║ ╚███╔╝ ██████╔╝    ██║     ██║██████╔╝██████╔╝███████║██████╔╝ ╚████╔╝ 
    ██║  ██║ ██╔██╗ ██╔══██╗    ██║     ██║██╔══██╗██╔══██╗██╔══██║██╔══██╗  ╚██╔╝  
    ██████╔╝██╔╝ ██╗██████╔╝    ███████╗██║██████╔╝██║  ██║██║  ██║██║  ██║   ██║   
    ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝                                                                                   
        ''')
            while True:
                print('''
1. LOGIN IS ADMIN 
2. LOGIN AS CUSTOMER
3. REGISTER AS CUSTOMER
0. EXIT THE PROGRAM               ''')
                print()

                d=int(input('Enter your choice : '))
                if d==1:
                    admin()

                elif d==2:
                    login()

                elif d==3:
                    register()
                elif d==0:
                    kkk=input('PLEASE PRESS ENTER TO CLOSE THE PROGRAM')
                    if kkk=='':
                        exit()

                else:
                    print( 'OPTION INVALID, ENTER A VALID OPTION...... ')

mainmenu()
