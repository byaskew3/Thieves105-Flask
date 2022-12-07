from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# Can do it this way, but not recommended
# class Followers(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
)

# create Models based off of our ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)
    followed = db.relationship('User',
        primaryjoin = (followers.columns.follower_id==id),
        secondaryjoin = (followers.columns.followed_id==id),
        secondary = followers,
        backref = db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def follow(self, user):
        self.followed.append(user)
        db.session.commit()
    
    def unfollow(self, user):
        self.followed.remove(user)
        db.session.commit()
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    img_url = db.Column(db.String)
    caption = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, img_url, caption, user_id):
        self.title = title
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update_db(self):
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'img_url': self.img_url,
            'caption': self.caption,
            'date_created': self.date_created,
            'user_id': self.user_id,
            'author': self.author.username
        }
