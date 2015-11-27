from views import db
import datetime


# from flask import Markup
# from markdown import markdown
# from markdown.extensions.codehilite import CodeHiliteExtension
# from markdown.extensions.extra import ExtraExtension
# from micawber import bootstrap_basic, parse_html
# from micawber.cache import Cache as OEmbedCache


# oembed_providers = bootstrap_basic(OEmbedCache())


class Post(db.Model):
    __tablename__ = 'blogposts'

    postid = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, nullable=False, default='text')
    header = db.Column(db.String, nullable=False)
    digest = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=True)
    date = db.Column(db.Date, default=datetime.datetime.now)
    comments = db.relationship('Comment', backref='commentor')

    def __init__(self, subject, header, digest, body):
        self.subject = subject
        self.header = header
        self.digest = digest
        self.body = body

    def __repr__(self):
        return '<header{0}>'.format(self.header)

    # @property
    # def html_content(self):
    # 	highlight = CodeHiliteExtension(linenums=False, css_class='highlight')
    # 	extras = ExtraExtension()
    # 	markdown_content = markdown(self.content, extentions=[highlight, extras])
    # 	oembed_content = parse_html(
    # 		markdown_content,
    # 		oembed_providers,
    # 		urlize_all = True,
    # 		maxwidth = app.config['SITE_WIDTH']
    # 		)
    # 	return Markup(oembed_content)
    #


class Project(db.Model):
    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    discription = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, default=datetime.datetime.now)
    finished = db.Column(db.Boolean, default=0)
    download_file = db.Column(db.Boolean, default=0)
    start_date = db.Column(db.Date, default=datetime.datetime.now)

    def __init__(self, subject, discription, due_date, finished, download_file):
        self.subject = subject
        self.discription = discription
        self.due_date = due_date
        self.finished = finished
        self.download_file = download_file

    def __repr__(self):
        return '<subject{0}>'.format(self.subject)


class Way(db.Model):
    __tablename__ = 'ways'

    way_id = db.Column(db.Integer, primary_key=True)
    way = db.Column(db.String, nullable=False)

    def __init__(self, way):
        self.way = way

    def __repr__(self):
        return self.way


class Video(db.Model):
    __tablename__ = 'videos'

    video_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    video_type = db.Column(db.String, nullable=False)
    digest = db.Column(db.String, nullable=False)
    thumbnail = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    comments = db.relationship('videoComment', backref='commentor')

    def __init__(self, name, video_type, digest, address, thumbnail):
        self.name = name
        self.video_type = video_type
        self.digest = digest
        self.address = address
        self.thumbnail = thumbnail

    def __repr__(self):
        return self.name


class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('blogposts.postid'))

    def __init__(self, name, email, comment, post_id):
        self.name = name
        self.email = email
        self.comment = comment
        self.post_id = post_id

    def __repr__(self):
        return self.comment


class videoComment(db.Model):
    __tablename__ = 'videoComments'

    comment_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('videos.video_id'))

    def __init__(self, name, email, comment, video_id):
        self.name = name
        self.email = email
        self.comment = comment
        self.video_id = video_id

    def __repr__(self):
        return self.comment