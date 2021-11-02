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
def updatedata():
    import mysql.connector as f
    my=f.connect(host="localhost",user="root",passwd="root",database="lic")
    k=my.cursor()
    i=input("enter policy holder name to be updated")
    k.execute("SELECT * from policy") 
    m=k.fetchall()
    for p in m:
        if i==p[1]:
           w=input("enter the new due date in YYYY-MM-DD format")
           k.execute("update policy set PREMIUM_DUE_DATE='%s' where NAME='%s'"%(w,i))
           my.commit()
           print(k.rowcount,"rows affected")
           print("updated successfully")
           break
    else:
        print(" policy holder not found")
def deletedata():
    import mysql.connector as f
    my=f.connect(host="localhost",user="root",passwd="root",database="lic")
    k=my.cursor()
    i=input("enter policy holder name to be deleted")
    k.execute("SELECT * from policy") 
    m=k.fetchall()
    for p in m:
        if i==p[1]: 
            k.execute(F"delete from policy where name='{i}'")
            my.commit()
            print("deleted successfully")
            break
    else:
        print("policy holder not found")
def display():
        import mysql.connector as f
        from tabulate import tabulate
        my=f.connect(host="localhost",user="root",passwd="root",database="lic")
        k=my.cursor() 
        k.execute("SELECT * from policy")
        va = k.fetchall()
        h=['SNO','NAME','AGE','POLICY_NAME','TERM','NOMINEE','SUM_ASSURED','TOTAL_PREMIUM','PREMIUM_DUE_DATE']
        p=(tabulate(va,headers=h,tablefmt='pretty'))
        print(p)
        my.close()
def email():
    import smtplib
    from tabulate import tabulate
    import mysql.connector as f 
    my=f.connect(host="localhost",user="root",passwd="root",database="lic")
    k=my.cursor() 
    k.execute("SELEct sno,name,policy_name,total_premium,premium_due_date from policy")
    va = k.fetchall()
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("suryalicdb@gmail.com","Lic@1234")
    h=['SNO','NAME','P_NAME','TOT_PREM','DUE_DATE']
    p=(tabulate(va,headers=h,tablefmt='psql'))
    s.sendmail("suryalicdb@gmail.com","surya090404@gmail.com",p)
    print("email sent")
    s.quit()
menu()
