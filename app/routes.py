from app import app
from flask import render_template
from .models import User
from flask_login import current_user

@app.route('/')
@app.route('/home')
def home():
    users = User.query.all()

    following_set = set()
    if current_user.is_authenticated:
        for user in current_user.followed.all():
            following_set.add(user.id)
        
        for user in users:
            if user.id in following_set:
                user.isFollowing = True

    return render_template('index.html', users=users)
