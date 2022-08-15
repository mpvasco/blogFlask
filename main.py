from flask import Flask, render_template, url_for
from forms import FormLogin, FormCreateAccount

app = Flask(__name__)

lista_users = ['paula', 'yasmim', 'paloma']

app.config['SECRET_KEY'] = 'jdfh349t8309soiw3irugh83939839'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contact():
    return render_template('contact.html')

@app.route("/usuarios")
def users():
    return render_template('users.html', x=lista_users)

@app.route("/login")
def login():
    form_login = FormLogin()
    form_create_account = FormCreateAccount()
    return render_template('login.html',form_login=form_login, form_create_account=form_create_account )

if __name__ == '__main__':
  app.run(debug=True)