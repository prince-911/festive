from db import mysql

def registration(username,firstname,middlename,lastname,email,number,password,confirm_password):
    if(password==confirm_password):
        conn=mysql.connect
        cur=conn.cursor()
        cur.execute("insert into admin (username,firstname,middlename,lastname,email,number,password) values (%s,%s,%s,%s,%s,%s,%s)",(username,firstname,middlename,lastname,email,number,password))
        conn.commit()
        cur.close()
        conn.close()
        return True
    else:
        return False
