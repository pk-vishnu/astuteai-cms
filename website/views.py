from flask import Blueprint, render_template,request, flash,redirect,url_for, jsonify, abort
from flask_login import login_required, current_user
import datetime
import markdown2
from . import db
from .models import BlogPost
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html",user = current_user)


@views.route('/create',methods=['GET','POST'])
@login_required
def blogPost():
    if request.method=='POST':
        title=request.form['title']
        author=request.form['author']
        thumbnail=request.form['thumbnail']
        md_content=request.form['content']
        date_created=datetime.datetime.now()
        html_content = markdown2.markdown(md_content)
        blog_post = BlogPost(title=title,
                        content_md=md_content,
                        content_html=html_content,
                        thumbnail=thumbnail,
                        author=author,
                        date_created=date_created)
        db.session.add(blog_post)
        db.session.commit()
        flash("Blog Post Created!",category='success')
        return redirect(url_for('views.home'))

    return render_template("create.html",user=current_user)

@views.route('/blog/<int:id>', methods=['GET'])
def get_blog(id):
    try:
        blog_post = BlogPost.query.get(id)
        if not blog_post:
            abort(404, description="Blog post not found")
        
        response = {
            'id': blog_post.id,
            'title': blog_post.title,
            'author': blog_post.author,
            'thumbnail': blog_post.thumbnail,
            'content': blog_post.content_html,
            'date_created': blog_post.date_created
        }
        return jsonify(response), 200
    except Exception as e:
        print(f"Error retrieving blog post: {e}")
        abort(500, description="Internal server error")

@views.route('/manage',methods=['GET'])
@login_required
def manage():
    posts = BlogPost.query.all()
    return render_template("manage.html",user=current_user,posts=posts)


@views.route('view/<int:id>',methods=['GET'])
@login_required
def view_post(id):
    return BlogPost.query.get(id).content_html


@views.route('/delete/<int:id>',methods=['GET'])
@login_required
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    flash("Blog Post Deleted!",category='success')
    return redirect(url_for('views.manage'))