from flask import Flask,render_template,request,redirect,url_for
from form import LoginForm,RegForm
# from main import validate_username
from main import registration
import mysql.connector
from flask_mysqldb import MySQL

 
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']='festive_ride'
app.config['MYSQL_CURSORCLASS']='DictCursor'
app.config['SECRET_KEY']='1234 This is a secret key'
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    admin=LoginForm()
    msg1=""
    conn=mysql.connect
    cur=conn.cursor()
    cur.execute("select * from admin where email=%s and password=%s",(admin.login_email.data,admin.login_password.data))
    v1=cur.fetchall()    
    if (admin.validate_on_submit()):
        if(v1):
            msg1="Logged In Sucessfully"
        else:
            msg1="Invalid Crendentials"
    return render_template("login.html",login_form=admin,msg=msg1)
@app.route('/register',methods=['GET','POST'])
def register():
    reg=RegForm()
    msg2=""
    if (reg.validate_on_submit()):
        username=reg.reg_username.data
        firstname=reg.reg_firstname.data
        middlename=reg.reg_middlename.data
        lastname=reg.reg_lastname.data
        email=reg.reg_email.data
        number=reg.reg_number.data
        password=reg.reg_password.data
        confirm_password=reg.reg_confirm_password.data

        #insert user data into mysql database

        res=registration(username,firstname,middlename,lastname,email,number,password,confirm_password)

        if res:
            return redirect(url_for('login'))
        else:
            msg2="incorrect"

    return render_template("register.html",reg_form=reg,msg=msg2)


        
if __name__ == "__main__":
    app.run(debug=True)
