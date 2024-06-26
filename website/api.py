from flask import Blueprint, jsonify
from .models import BlogPost

api = Blueprint('api', __name__)

@api.route('/fetch_all_posts/', methods=['GET'])
def fetch_all_posts():
    posts = BlogPost.query.order_by(BlogPost.id.desc()).all()
    print(f"Fetched Posts: {posts}")
    response = []
    for post in posts:
        response.append({
            'id': post.id,
            'title': post.title,
            'author': post.author,
            'thumbnail': post.thumbnail,
            'content': post.content_html,
            'date_created': post.date_created
        })
    if response == []:
        return jsonify({'error': 'No posts found'}), 404
    return jsonify(response), 200

@api.route('/fetch_6_posts',methods=['GET'])
def fetch_6_posts():
    posts = BlogPost.query.order_by(BlogPost.id.desc()).limit(6).all()
    response = []
    for post in posts:
        response.append({
            'id': post.id,
            'title': post.title,
            'author': post.author,
            'thumbnail': post.thumbnail,
            'content': post.content_html,
            'date_created': post.date_created
        })  
    return jsonify(response), 200