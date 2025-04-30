from flask import Flask,render_template,request,redirect,url_for
# from form import LoginForm,RegForm
import mysql.connector
from flask_mysqldb import MySQL

app=Flask(__name__)
# app.config['MYSQL_HOSt']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']=""
# app.config['MYSQL_DB']='festive_ride'
# app.config['MYSQL_CURSORCLASS']='DictCursor'
# app.config['SECRET_KEY']='1234 This is a secret key'
# mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/login',methods=['GET','POST'])
# def admin():
#     admin=LoginForm()
#     msg1=""
#     conn=mysql.connect
#     cur=conn.cursor()
#     cur.execute("select count(*) as c from admin where email=%s and password=%s",(admin.login_email.data,admin.login_password.data))
#     v1=cur.fetchone()['c']
#     if (admin.validate_on_submit()):
#         if(v1==1):
#             msg1="Logged In Sucessfully"
#         else:
#             msg1="Invalid Crendentials"
#     return render_template("login.html",login_form=admin,msg=msg1)
        
if __name__ == "__main__":
    app.run(debug=True)
