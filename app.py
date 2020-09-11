import os
from flask import Flask, render_template, request, flash
from forms import ContactForm, ClientsForm, CandidatesForm
from flask_mail import Mail, Message
from flask_sslify import SSLify
from dotenv import load_dotenv
load_dotenv()

# from flask_talisman import Talisman
# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
sslify = SSLify(app)


# Talisman is the newer version of sslify to replace eventually
# Talisman(app)
# csp = {
#     'default-src': [
#         '\'self\'',
#         '\'unsafe-inline\'',
#         'stackpath.bootstrapcdn.com',
#         'stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css',
#         'fonts.googleapis.com/css?family=Lato|Montserrat:700',
#         'maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css',
#         'fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap',
#         'cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js',
#         'cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js',
#         'code.jquery.com',
#         'cdn.jsdelivr.net'
#     ]
# }
# talisman = Talisman(app, content_security_policy=csp)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.office365.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.getenv('MAIL_PASSWORD')
app.config["MAIL_DEFAULT_SENDER"] = os.getenv('MAIL_USERNAME')

mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')


# @app.route('/candidates')
# def candidates():
#     return render_template('candidates.html')


# @app.route('/clients')
# def clients():
#     return render_template('clients.html')


@app.route('/legal')
def legal():
    return render_template('legal.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/candidates', methods=['GET', 'POST'])
def candidates():
    form = CandidatesForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('candidates.html', form=form)
        else:
            msg = Message(form.subject.data, sender=os.getenv('MAIL_USERNAME'), recipients=[os.getenv('MAIL_USERNAME')])
            msg.body =  """
            Name: %s Email: %s Telephone: %s CV: %s Message: %s 
            """ % (form.name.data, form.email.data, form.telephone.data, form.upload.data, form.message.data)
            mail.send(msg)

            return render_template('success.html', success=True)
    elif request.method == 'GET':
        return render_template('candidates.html', form=form)


@app.route('/clients', methods=['GET', 'POST'])
def clients():
    form = ClientsForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('clients.html', form=form)
        else:
            msg = Message(form.subject.data, sender=os.getenv('MAIL_USERNAME'), recipients=[os.getenv('MAIL_USERNAME')])
            msg.body = """
            Name: %s Company name: %s Role: %s Email: %s Telephone: %s 
            Position: %s Message: %s
            """ % (form.name.data, form.company.data, form.role.data, form.email.data, form.telephone.data, form.position.data, form.message.data)
            mail.send(msg)

            return render_template('success.html', success=True)
    elif request.method == 'GET':
        return render_template('clients.html', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender=os.getenv('MAIL_USERNAME'), recipients=[os.getenv('MAIL_USERNAME')])
            msg.body = """
            Name: %s Email: %s Message;
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('success.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=False)

# if __name__ == '__main__':
#     app.run(host=os.environ.get('IP'),
#             port=int(os.environ.get('PORT')),
#             debug=True)