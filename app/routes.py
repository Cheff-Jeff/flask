from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm, RegisterForm, IPform
from app.models import User, IP
from app import db

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
  form = LoginForm()
  if form.validate_on_submit():
    if form.username.data == 'admin' and form.password.data == 'admin':
      flash(f'Welkome {form.username.data}.', 'success')
      return redirect(url_for('account'))
    else:
      flash(f'Login unseccessfull. Please check username and password', 'danger')
  return render_template('home.html', title="login", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title="register", form=form)
#145.93.148.252
@app.route("/account", methods=['GET', 'POST'])
def account():
  form = IPform()
  if form.validate_on_submit():
    flash(f'Your ip has been added.', 'success')
    ip = IP(ip=form.IPaddress.data, user_id=1)
    db.session.add(ip)
    db.session.commit()
    return redirect(url_for('account'))
  IPs = IP.query.all()
  return render_template('account.html', title="account", form=form, ips=IPs)