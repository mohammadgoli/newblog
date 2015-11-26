# _*_ coding: utf-8 _*_
# imports
from functools import wraps
from flask import Flask, flash, redirect, session, url_for, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from forms import LoginForm, BlogPostForm, ProjectForm, SubscriptionForm, WayForm, ContactForm, VideoForm, CommentForm
# from werkzeug import secure_filename
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_pyfile("_config.py")
db = SQLAlchemy(app)
mail = Mail(app)

from models import Post, Project, Way, Video, Comment


# helper functions
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:  # s and qout
            return test(*args, **kwargs)  # return what ?????
        else:
            flash(u'باید اول وارد شوید!')  # u dont say
            return redirect(url_for('admin'))

    return wrap


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error), 'error')


def posts():
    return db.session.query(Post).order_by(Post.date.desc())


def finished_projects():
    return db.session.query(Project).filter_by(finished='1').order_by(Project.due_date.desc())


def last_project():
    return db.session.query(Project).filter_by(finished='0')


def latest_video():
    return db.session.query(Video).order_by(Video.video_id.desc()).first()


def other_videos():
    return db.session.query(Video).order_by(Video.video_id.desc())


def specific_post(postNumber):
    return db.session.query(Post).filter_by(postid=postNumber)

def latest_post():
    return db.session.query(Post).order_by(Post.postid.desc()).first()

def comments(postNumber):
    return db.session.query(Comment).filter_by(post_id=postNumber)


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"the error in {} field is {}".format(getattr(form, field).label.text, error), 'error')


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash(u'بازم بیا از این ورا')


@app.route('/')
@app.route('/index')
@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/blog')
def blog():
    return render_template('post.html', posts=posts())


@app.route('/blog/<int:post_number>', methods=['GET', 'POST'])
def viewpost(post_number):
    error = None
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_comment = Comment(
                form.name.data,
                form.email.data,
                form.comment.data,
                post_number
            )
            db.session.add(new_comment)
            db.session.commit()
    return render_template('specificpost.html', posts=specific_post(post_number), comments=comments(post_number), form=form, latest_post=latest_post())


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'logged_in' not in session:
        error = None
        form = LoginForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                if request.form['username'] != app.config['USERNAME'] \
                        or request.form['password'] != app.config['PASSWORD']:
                    error = u'داداش مطمئنی خود ممدی؟؟؟'
                else:
                    session['logged_in'] = True
                    session.permanent = True
                    flash(u'ببین کی اینجاس!!!')
                    return redirect(url_for('editposts'))
        return render_template('login.html', form=form, error=error)
    else:
        return redirect(url_for('blog'))


@app.route('/editposts', methods=['GET', 'POST'])
@login_required
def editposts():
    error = None
    form = BlogPostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_post = Post(
            	form.subject.data,
                form.header.data,
                form.digest.data,
                form.body.data,
            )
            db.session.add(new_post)
            db.session.commit()
            flash(u'پست ثبت شد!!')
    return render_template('postedit.html', form=form, error=error)


@app.route('/deleteposts/<int:postid>', methods=['GET', 'POST'])
@login_required
def deleteposts(postid):
    newid = postid
    post = db.session.query(Post).filter_by(postid=newid)
    post.delete()
    db.session.commit()
    flash(u'پاکش کردی :|')
    return redirect(url_for('blog'))


# @app.route('/upload/', methods=['GET', 'POST'])
# @login_required
# def upload():
# 	form = UploadForm()
# 	if form.validate_on_submit():
# 		fileName = secure_filename(form.myFile.data.fileName)
# 		form.myFile.data.save('uploads/' + fileName)
# 	else:
# 		fileName = None
# 	return render_template('upload.html', form=form, fileName = fileName)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    error = None
    deactive = False
    form = SubscriptionForm()
    choices = [(option, option) for option in db.session.query(Way)]
    if choices:
        form.ways.choices = choices
        if request.method == 'POST':
            print 'done!'
            msg = Message(u"با تشکر از اعلام آمادگی {}".format(form.name.data),
                          recipients=[form.email.data],
                          sender='gli.mhmd@gmail.com',
                          body=u'سلام.<br /> ممنون از این که برای همکاری در پروژه من اعلام آمادگی کردید.در اصرع وقت با شما تماس خواهم گرفت<br /> در صورتی که تماسی از بنده دریافت نکردید لطفا از طریق ایمیل من در سایت اقدام بفرمایید.<br /> با تشکر'.format(form.name.data)
                          )
            admin_msg = Message(u"you have a new subscription",
                                recipients=['gli.mhmd@gmail.com'],
                                sender='gli.mhmd@gmail.com',
                                body=u'سلام محمد. یک فرد جدید مایل به همکاری در پروژه اخیر است <br />{}<br />{}<br />{}<br />{}<br />{}'.format(
                                    form.name.data, form.more.data, form.email.data, form.ways.data, form.phoneNumber.data))
            mail.send(msg)
            mail.send(admin_msg)
    else:
        deactive = True
    return render_template('projects.html', form=form, last_project=last_project(),
                           finished_projects=finished_projects(), error=error, deactive=deactive)


@app.route('/newproject', methods=['GET', 'POST'])
@login_required
def newproject():
    error = None
    form = ProjectForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print 'validated'
            new_project = Project(
                form.subject.data,
                form.discription.data,
                form.duedate.data,
                form.finished.data,
                form.download_file.data,
            )
            db.session.add(new_project)
            db.session.commit()
            flash(u'پروژه ثبت شد ممد!')
        else:
            print 'not!'
    return render_template('newproject.html', form=form, error=error)


@app.route('/endproject/<int:projectid>', methods=['GET', 'POST'])
@login_required
def endproject(projectid):
    theproject = db.session.query(Project).filter_by(project_id=projectid)
    theproject.update({"finished": '1'})
    db.session.commit()
    flash(u'زدی رفت حاجی احسنت')
    return redirect(url_for('projects'))


@app.route('/editways', methods=['GET', 'POST'])
@login_required
def editways():
    form = WayForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_way = Way(form.way.data)
            db.session.add(new_way)
            db.session.commit()
    return render_template('editways.html', form=form)


@app.route('/deleteways', methods=['GET', 'POST'])
@login_required
def deleteways():
    for thing in db.session.query(Way):
        db.session.delete(thing)
    db.session.commit()
    return redirect(url_for('editways'))


@app.route('/about', methods=['GET', 'POST'])
def about():
    form = ContactForm()
    if request.method == 'POST':
        contact_msg = Message(u'پیامتون دریافت شد!',
                              recipients=[form.email.data],
                              sender='gli.mhmd@gmail.com',
                              body=u'پیامتون رو دریافت کردم . در اسرع وقت پاسخ خواهم داد !')
        admin_msg = Message(u'you have a new message!',
                            recipients=['gli.mhmd@gmail.com'],
                            sender='gli.mhmd@gmail.com',
                            body=u'you have a new message from {} which says {}'.format(form.email.data, form.message.data))
        mail.send(contact_msg)
        mail.send(admin_msg)
    return render_template('about.html', form=form)


@app.route('/vlog', methods=['GET', 'POST'])
def vlog():
    return render_template('vlog.html', latest_video=latest_video(), other_videos=other_videos())


@app.route('/newvideo', methods=['GET', 'POST'])
@login_required
def newvideo():
    form = VideoForm()
    if request.method == 'POST':
        new_video = [
            form.name.data,
            form.video_type.data,
            form.address.data,
        ]
        db.session.add(new_video)
        db.session.commit()

    return render_template('newvideo.html', form=form)
