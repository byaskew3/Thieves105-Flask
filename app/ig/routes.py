from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.models import Post
from .forms import CreatePostForm

ig = Blueprint('ig', __name__, template_folder='ig_templates')

@ig.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if request.method == 'POST':
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            caption = form.caption.data

            post = Post(title, img_url, caption, current_user.id)

            # add post to database
            # db.session.add(post)
            # db.session.commit()
            post.save_to_db()
            return redirect(url_for('home'))

    return render_template('create_post.html', form=form)

@ig.route('/posts')
def view_posts():
    posts = Post.query.all()
    return render_template('feed.html', posts=posts)