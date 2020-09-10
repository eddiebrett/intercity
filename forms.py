from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators, IntegerField, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField


# class ContactForm(Form):
#     name = TextField("Name",  [validators.Required("Please enter your name.")])
#     email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
#     subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
#     message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
#     submit = SubmitField("Send")


# from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(FlaskForm):
    name = TextField("Name", validators=[InputRequired('Please enter your name.')])
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",  validators=[InputRequired("Please enter a subject.")])
    message = TextAreaField("Message",  validators=[InputRequired("Please enter a message.")])
    submit = SubmitField("Send")


class ClientsForm(FlaskForm):
    name = TextField("Name", validators=[InputRequired('Please enter your name.')])
    company = TextField("Company", validators=[InputRequired('Please enter your company name.')])
    role = TextField("Job title", validators=[InputRequired('Please enter your job title.')])
    position = TextField("Position to fill", validators=[InputRequired('Please enter the position you wish to fill.')])
    email = EmailField("Email", validators=[InputRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    telephone = IntegerField("Telephone", validators=[InputRequired("Please enter a subject.")])
    subject = TextField("Subject",  validators=[InputRequired("Please enter a telephone number.")])
    message = TextAreaField("Message", validators=[InputRequired("Please enter a message.")])
    submit = SubmitField("Send")


class CandidatesForm(FlaskForm):
    name = TextField("Name", validators=[InputRequired('Please enter your name.')])
    email = EmailField("Email", validators=[InputRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    telephone = IntegerField("Telephone", validators=[InputRequired("Please enter a telephone numbers.")])
    upload = FileField('Resume', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    subject = TextField("Subject",  validators=[InputRequired("Please enter a subject.")])
    message = TextAreaField("Message", validators=[InputRequired("Please enter a message.")])
    submit = SubmitField("Send")
