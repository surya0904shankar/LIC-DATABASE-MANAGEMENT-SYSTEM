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
