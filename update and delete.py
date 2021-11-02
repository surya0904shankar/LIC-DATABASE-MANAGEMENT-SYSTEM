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
