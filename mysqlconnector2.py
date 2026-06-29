def main_menu():
    ch='y'
    while ch =='y':
        print("             Main Menu        ")
        print("1: To add a record in the table")
        print("2: To display all the record from the table")
        print("3: quit")
        choice=int(input("Enter your choice"))
        if choice == 1:
            add_rec()
        elif choice == 2:
            fetch_data()
        elif choice==3:
            print("Exiting")
            break
        else:
            print("Wrong output")
    ch = input("Do you want to continue")
def add_rec():
    import mysql.connector
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="dav123",database="diptesh")
        cursor=db.cursor()
        rno=int(input("Enter roll number"))
        nm=input("Enter name")
        gr=input("Enter grade")
        sql_query= "Insert into student1 values(%s,%s,%s)"
        val=(rno,nm,gr)
        cursor.execute(sql_query,val)
        db.commit()
        print("Record added")
    except:
        db.rollback()
        print("Error,Record not added")
def fetch_data():
    import mysql.connector
    try:
        db = mysql.connector.connect(host="localhost",user="root",password="dav123",database="diptesh")
        cursor=db.cursor()
        cursor.execute("Select * from student1")
        records = cursor.fetchall()
        for x in records:
            print(x[0],x[1],x[2])
    except:
        print("Error , unable to fetch data")
main_menu()
