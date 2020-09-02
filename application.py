import os
from flask import Flask, render_template, request, flash
from forms import ContactForm, ClientsForm, CandidatesForm
from flask_mail import Message, Mail
# from dotenv import load_dotenv
# load_dotenv()

application = Flask(__name__)
app = application
mail = Mail(app)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.office365.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.getenv('MAIL_PASSWORD')

mail.init_app(app)


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
            msg.body = form.name.data, form.email.data, form.telephone.data, form.upload.data, form.message.data
            mail.send(msg)

            return render_template('candidates.html', success=True)
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
            From: %s &lt;%s&gt;
            %s
            """ % (form.name.data, form.company.data, form.role.data, form.email.data, form.telephone.data, form.position.datat, form.message.data)
            mail.send(msg)

            return render_template('clients.html', success=True)
    elif request.method == 'GET':
        return render_template('clients.html', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = CandidatesForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender=os.getenv('MAIL_USERNAME'), recipients=[os.getenv('MAIL_USERNAME')])
            msg.body = """
            From: %s &lt;%s&gt;
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=False)
