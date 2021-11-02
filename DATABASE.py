def menu():
    ch="y"
    while(ch=="y"):
        print("__________________________________________")
        print("1.ADD A NEW CUSTOMER")
        print("2.UPDATE CUSTOMER DUE DATE")
        print("3.DELETE A CUSTOMER")
        print("4.DISPLAY CUSTOMERS")
        print("5.TO RECEIVE EMAIL OF CUSTOMER DATABASE") 
        print("6.EXIT")
        print("__________________________________________") 
        c=int(input('enter choice'))
        if c==1:
            insertdata()
        elif c==2:
            updatedata()
        elif c==3:
            deletedata()
        elif c==4:
            display()
        elif c==5:
            email()
        elif c==6:
            print("exiting")
            break
    ch=input("do you want to continue(y/n)")
def insertdata():
    import mysql.connector as f
    my=f.connect(host="localhost",user="root",passwd="root",database="lic")
    k=my.cursor()
    r=int(input("enter serial no"))
    n=input("enter name")
    o=int(input("enter age"))
    p=input("enter policy name")
    q=int(input("enter policy term"))
    s=input("enter nominee name")
    t=int(input("enter sum assured "))
    u=int(input("enter total premium "))
    v=input("enter due date in YYYY-MM-DD format")
    val="insert into policy values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    k.execute(val,(r,n,o,p,q,s,t,u,v))
    my.commit()
    print("entered successfully")
    my.rollback()
