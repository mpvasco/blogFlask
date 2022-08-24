from flask import Flask, render_template, url_for, request, flash, redirect
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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_create_account = FormCreateAccount()
    if form_login.validate_on_submit() and 'btn_submit_login' in request.form:
        flash(f'Login bem sucedido: {form_login.emaill.data}', 'alert-success')
        return redirect( url_for('home'))
        
    if form_create_account.validate_on_submit() and 'btn_submit_create_account' in request.form:
        flash(f'Conta criada com sucesso: {form_create_account.email.data}', 'alert-success')
        return redirect( url_for('home'))
    return render_template('login.html',form_login=form_login, form_create_account=form_create_account )

if __name__ == '__main__':
  app.run(debug=True)