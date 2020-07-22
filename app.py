from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail


mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'bobbydylan20202020@gmail.com'
app.config["MAIL_PASSWORD"] = 'BobDylan2020'

mail.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/candidates')
def candidates():
    return render_template('candidates.html')


@app.route('/clients')
def clients():
    return render_template('clients.html')


@app.route('/legal')
def legal():
    return render_template('legal.html')


# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     form = ContactForm()

#     if request.method == 'POST':
#         if form.validate() is False:
#             flash('All fields are required.')
#         return render_template('contact.html', form=form)
#     elif request.method == 'GET':
#         return render_template('contact.html', form=form)
#     else:
#         msg = Message(form.subject.data, sender='contact@example.com',
#                           recipients=['your_email@example.com'])
#         msg.body = """
#             From: %s &lt;%s&gt;
#             %s
#             """ % (form.name.data, form.email.data, form.message.data)
#         mail.send(msg)

#     return render_template('contact.html', success=True)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() is False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run()
