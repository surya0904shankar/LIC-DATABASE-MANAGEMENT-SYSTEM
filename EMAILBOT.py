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
    s.login("licdb@gmail.com","ABC@1234")
    h=['SNO','NAME','P_NAME','TOT_PREM','DUE_DATE']
    p=(tabulate(va,headers=h,tablefmt='psql'))
    s.sendmail("licdb@gmail.com","commmerce09@gmail.com",p)
    print("email sent")
    s.quit()
menu()
    
