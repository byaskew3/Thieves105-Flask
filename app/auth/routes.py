from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.auth.forms import UserCreationForm, LoginForm
from app.models import User
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            print(username, email, password)

            user = User(username, email, password)

            # add user to database
            # db.session.add(user)
            # db.session.commit()
            user.save_to_db()
            return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method=='POST':
        if form.validate():
            username = form.username.data
            password = form.password.data

            # Query user from db
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash(f'Successfully Logged In! Welcome back, {user.username}!', 'success')
                    login_user(user)
                    return redirect(url_for('ig.view_posts'))
                else:
                    flash('Invalid Password!', 'danger')
            else:
                print('User does not exist')
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
