import mysql.connector
def test():
    mydb=mysql.connector.connect(host='localhost',user='root',password='dav123')
    cur = mydb.cursor()
    if mydb.is_connected():
        print(mydb)
        print('Connection Established!')
    else:
        print('ERROR!!')
def showdb():
    mydb=mysql.connector.connect(host='localhost',user='root',password='dav123')
    mycursor=mydb.cursor()
    mycursor.execute('Show Databases')
    print('----------------------------------------------------------------------------------------------------------')
    print('                                                                                 DATABASES                                                                              ')
    print('----------------------------------------------------------------------------------------------------------')
    for i in mycursor:
        print(i[0])
    print('----------------------------------------------------------------------------------------------------------')
    print()
def createdb():
    mydb=mysql.connector.connect(host='localhost',user='root',password='dav123')
    mycursor=mydb.cursor()
    databas=input('Enter Database to create: ')
    mycursor.execute('create database '+ databas)
    print('Database',databas,'created !!')
    print()
def usedb():
    mydb=mysql.connector.connect(host='localhost',user='root',password='dav123')
    mycursor=mydb.cursor()
    databas=input('Enter Database to use: ')
    mycursor.execute('Use ' + databas)
    print('Database',databas,'in use !!')
    print()
def createtable():
    mydb=mysql.connector.connect(host='localhost',user='root',password='dav123',database='span')
    mycursor=mydb.cursor()
    tab=input('Enter table name to create: ')
    try:
        mycursor.execute('Create table  '+  tab  +' (Roll int(3),Name varchar(20),marks int(3))')
        print ('Table Created !!!')
    except:
        print('Table already created')
def desctable():
    mydb=mysql.connector.connect(host='localhost',user='root',password='dav123',database='span')
    mycursor=mydb.cursor()
    destab=input('Enter Table name to view structure: ')
    try:
        print('Table Description')
        cur.execute('Desc '+ destab)
        for i in cur:
            print(i)
    except:
        print('Error')
    print()

ans='y'
while(1):
    print('1. To establish connection')
    print('2. To show all the databases')
    print('3. To create a database')
    print('4. To use a database')
    print('5. To create a new table')
    print('6. To describe structure of table')
    print('0. EXIT!!!')
    print('----------------------------------------------------------------------------------------------------------')
    ch=int(input('Enter your choice: '))
    if ch==1:
        test()
    if ch==2:
        showdb()
    if ch==3:
        createdb()
    if ch==4:
        usedb()
    if ch==5:
        createtable()
    if ch==6:
        desctable()
        break
