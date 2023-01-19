from flask import render_template, url_for, request, redirect, flash
from resume import app, db
from resume.models import User, Post
from resume.forms import RegistrationForm, LoginForm,PostForm
from flask_login import login_user, logout_user, current_user,login_required

@app.route("/")



@app.route("/home")
def home():
  posts=Post.query.all()
  return render_template('home.html',posts=posts, user = current_user)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/post/<string:post_cv>",methods=['POST','GET'])
def post(post_cv):
  if request.method == 'GET':
    posts=Post.query.filter_by(on = post_cv)
    for p in posts:
      print(p)
    return render_template('post.html',posts=posts)

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!')
    return redirect(url_for('login'))
  else:
    flash('Your username should be between 6 and 8 characters long, and can only contain lowercase letters.')
    flash('password must match.')
  return render_template('register.html',title='Register',form=form)



@app.route("/do_post",methods=['GET','POST'])
@login_required
def do_post():
  form = PostForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data, content=form.content.data,
    author_id=current_user.id, on= form.on.data)
    db.session.add(post)
    db.session.commit()
    flash('post successful!')
    return redirect(url_for('do_post'))
  return render_template('do_post.html',title='Make Post',form=form)

@app.route("/registered")
def registered():
  return render_template('registered.html', title='Thanks!')

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('You\'ve successfully logged in,'+' '+ current_user.username +'!')
      return redirect(url_for('home'))
    flash('Invalid username or password.')
  return render_template('login.html',title='Login', form=form)

@app.route("/logout")
def logout():
  logout_user()
  flash('You\'re now logged out. Thanks for your visit!')
  return redirect(url_for('home'))
