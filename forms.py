from flask_wtf import Form
from wtforms.fields import TextField, BooleanField, SubmitField, TextAreaField

from wtforms import validators
from wtforms.validators import Required, ValidationError


# class ContactForm(Form):
#     name = TextField("Name",  [validators.Required("Please enter your name.")])
#     email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
#     subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
#     message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
#     submit = SubmitField("Send")


# from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError
 
class ContactForm(Form):
  name = TextField("Name",  [validators.Required("Please enter your name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
  submit = SubmitField("Send")