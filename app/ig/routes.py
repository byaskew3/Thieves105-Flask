from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import Post, User
from .forms import PostForm

ig = Blueprint('ig', __name__, template_folder='ig_templates')

@ig.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
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
            return redirect(url_for('ig.view_posts'))

    return render_template('create_post.html', form=form)

@ig.route('/posts')
def view_posts():
    posts = Post.query.all()
    return render_template('feed.html', posts=posts[::-1])

# Dynamic Routes
@ig.route('/posts/<int:post_id>')
def view_single_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return render_template('single_post.html', post=post)
    else:
        return redirect(url_for('ig.view_posts'))
            
@ig.route('/posts/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    form = PostForm()
    post = Post.query.get(post_id)
    if current_user.id == post.user_id:
        if request.method == 'POST':
            if form.validate():
                title = form.title.data
                img_url = form.img_url.data
                caption = form.caption.data

                # Update post on Attributes
                post.title = title
                post.img_url = img_url
                post.caption = caption

                # Update post on Database
                post.update_db()

                return redirect(url_for('ig.view_posts'))
    else:
        flash('You are not allowed to be here!', 'danger')
        return redirect(url_for('ig.view_posts'))
    return render_template('update_post.html', form=form, post=post)

@ig.route('/posts/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        post.delete_from_db()
    return redirect(url_for('ig.view_posts'))

@ig.route('/follow/<int:user_id>')
@login_required
def follow_user(user_id):
    user = User.query.get(user_id)
    if user:
        current_user.follow(user)
        flash(f'Successfully followed {user.username}!', 'success')
    else:
        flash('That user does not exist', 'danger')

    return redirect(url_for('home'))

@ig.route('/unfollow/<int:user_id>')
@login_required
def unfollow_user(user_id):
    user = User.query.get(user_id)
    if user:
        current_user.unfollow(user)
        flash(f'Successfully unfollowed {user.username}!', 'primary')
    else:
        flash('Cannot unfollow a user, that you\'re not following.', 'danger')
    return redirect(url_for('home'))