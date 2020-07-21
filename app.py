from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)

app.secret_key = 'development key'


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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() is False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)
