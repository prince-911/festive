from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,RadioField,EmailField,IntegerField
from wtforms.validators import InputRequired,Length,EqualTo,NumberRange,DataRequired,Email

class LoginForm(FlaskForm):
    login_email=EmailField("User Email: ",validators=[InputRequired()],render_kw={"placeholder":"User Email","class":"inputfield"})
    login_password=PasswordField("Password: ",validators=[InputRequired()],render_kw={"placeholder":"Password","class":"inputfield"})
    login_submit=SubmitField("Submit",render_kw={"class":"registerBtn"})


class RegForm(FlaskForm):
   reg_username=StringField("UserName",validators=[DataRequired()])
   reg_firstname = StringField('First Name:', validators=[DataRequired()])
   reg_middlename = StringField('Middle Name:', validators=[DataRequired()])
   reg_lastname = StringField('Last Name:', validators=[DataRequired()])
   reg_email = StringField('Email:', validators=[DataRequired(), Email()])
   reg_number = StringField('Contact Number:', validators=[DataRequired(),Length(min=10,max=10)])
   reg_password = PasswordField('Password:', validators=[DataRequired()])
   reg_confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('reg_password')])
   reg_submit = SubmitField('Submit')
    
