from flask import Flask, render_template

app = Flask(__name__)


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


@app.route('/contact')
def contact():
    return render_template('webform.php')



if __name__ == "__main__":
    app.run(debug=True)
