from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField


# class ContactForm(Form):
#     name = TextField("Name",  [validators.Required("Please enter your name.")])
#     email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
#     subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
#     message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
#     submit = SubmitField("Send")


# from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
    name = TextField("Name", validators=[InputRequired('Please enter your name.')])
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",  validators=[InputRequired("Please enter a subject.")])
    message = TextAreaField("Message",  validators=[InputRequired("Please enter a message.")])
    submit = SubmitField("Send")


