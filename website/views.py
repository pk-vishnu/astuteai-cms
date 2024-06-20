from flask import Blueprint, render_template,request, flash,redirect,url_for
from flask_login import login_required, current_user
import datetime
import markdown2
from . import db
from .models import BlogPost
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html",user = current_user)

@login_required
@views.route('/create',methods=['GET','POST'])
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