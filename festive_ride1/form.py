from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,RadioField,EmailField,IntegerField
from wtforms.validators import InputRequired,Length,EqualTo,NumberRange

class LoginForm(FlaskForm):
    login_email=EmailField("User Email: ",validators=[InputRequired()],render_kw={"placeholder":"User Email","class":"inputfield"})
    login_password=PasswordField("Password: ",validators=[InputRequired()],render_kw={"placeholder":"Password","class":"inputfield"})
    login_submit=SubmitField("Submit",render_kw={"class":"registerBtn"})
    
class RegForm(FlaskForm):
    reg_name=StringField("Enter Name:",validators=[InputRequired()],render_kw={'placeholder':'Name','class':'name'})
    reg_age=IntegerField("Age:",validators=[InputRequired(),NumberRange(min=20,max=100)],render_kw={"placeholder":'Age'})
    reg_gender=RadioField("Gender:",choices=['male','female','others'],default='male',validators=[InputRequired()],render_kw={'placeholder':'Gender'})
    reg_email=EmailField("Enter Email: ",validators=[InputRequired()],render_kw={"placeholder":"User Email","class":"inputfield"})
    reg_number=StringField("Contact Number:",validators=[InputRequired(),Length(min=10,max=10)],render_kw={"placeholder":"Phone Number"})
    reg_password=PasswordField("Password:",validators=[InputRequired()],render_kw={"placeholder":"Password"})
    reg_confirm_password=PasswordField("Confirm Password",validators=[InputRequired(),EqualTo('reg_password', message='Passwords must match')], render_kw={"placeholder": "Confirm Password"} )
    reg_submit=SubmitField("Submit",render_kw={"class":"registerBtn"})
    
