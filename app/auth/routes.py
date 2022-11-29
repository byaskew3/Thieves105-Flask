from flask import Blueprint, render_template, request, redirect, url_for

from app.auth.forms import UserCreationForm
from app.models import User

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

            #instantiate User from models
            user = User(username, email, password)

            #add user to database
            # db.session.add(user)
            # db.session.commit()
            user.save_to_db()

            return redirect(url_for('auth.login'))
            
            
    return render_template('signup.html', form=form)

@auth.route('/login')
def login():
    return render_template('login.html')