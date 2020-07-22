from flask_wtf import Form
from wtforms.fields import TextField, BooleanField, SubmitField, TextAreaField

from wtforms import validators
from wtforms.validators import Required, ValidationError


class ContactForm(Form):
    name = TextField("Name",  [validators.Required()])
    email = TextField("Email",  [validators.Required(), validators.Email()])
    subject = TextField("Subject",  [validators.Required()])
    message = TextAreaField("Message",  [validators.Required()])
    submit = SubmitField("Send")
