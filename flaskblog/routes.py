import secrets
from PIL import Image
from flask import escape, request, render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt, mail
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm,PostForm,RequestResetForm,ResetPasswordForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

@app.route('/')
@app.route('/home')
def home():
	page = request.args.get('page', 1 ,type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')



















