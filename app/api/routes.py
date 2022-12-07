from flask import Blueprint, request
from app.models import Post

api = Blueprint('api', __name__, url_prefix='/api')

# GET api routes
@api.route('/posts')
def view_posts_api():
    posts = Post.query.all()
    posts_json = []
    for post in posts:
        posts_json.append(post.to_dict())
    return {
        'status': 'ok',
        'data': posts_json
    }

@api.route('/posts/<int:post_id>')
def view_single_post_api(post_id):
    post = Post.query.get(post_id)
    if post:
        return {
            'status': 'ok',
            'data': post.to_dict()
        }
    return {
        'status': 'not ok',
        'message': 'That post does not exist. Try again.'
    }

# POST api routes
@api.route('/posts/create', methods=['POST'])
def create_post_api():
    data = request.json # this is coming from POST request body

    # unpacking the data
    title = data['title']
    img_url = data['img_url']
    caption = data['caption']
    user_id = data['user_id']

    # instatiate Post
    post = Post(title, img_url, caption, user_id)

    #add post to db
    post.save_to_db()

    return {
        'status': 'ok',
        'message': 'Post was successfully created.'
    }

