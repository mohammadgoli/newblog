# _*_ coding: utf-8 _*_

from flask_wtf import Form, RecaptchaField
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SelectField, IntegerField
from wtforms_html5 import DateField, DateRange
from wtforms.validators import DataRequired, Email, Length
from datetime import date


# from flask_wtf.file import FileField

class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    recaptcha = RecaptchaField()


class BlogPostForm(Form):
    subject = SelectField("subject", choices=[('text', 'text'), ('video', 'video'), ('imagetext', 'imagetext')])
    header = StringField("Header", validators=[DataRequired()])
    digest = StringField("digest", validators=[DataRequired()])
    body = TextAreaField("Body", validators=[DataRequired()])


# class UploadForm(Form):
# 	myFile = FileField("File")

class ProjectForm(Form):
    subject = StringField("Subject", validators=[DataRequired()])
    discription = TextAreaField("discription", validators=[DataRequired()])
    duedate = DateField("DueDate", validators=[DataRequired()])
    finished = BooleanField("Finished", default='False')
    download_file = BooleanField("Download", default='False')


class SubscriptionForm(Form):
    name = StringField(u"نام", validators=[DataRequired()])
    phoneNumber = StringField(u"تلفن", validators=[Length(min=10, max=11)])
    email = StringField(u"ایمیل", validators=[DataRequired()])
    ways = SelectField(u"نوع همکاری")
    more = TextAreaField(u"توضیحات")


class WayForm(Form):
    way = StringField("Way")


class ContactForm(Form):
    name = StringField(u"name", validators=[DataRequired()])
    email = StringField(u"email", validators=[DataRequired(), Email()])
    message = TextAreaField(u"message", validators=[DataRequired()])
    recaptcha = RecaptchaField()


class VideoForm(Form):
    name = StringField(u"name", validators=[DataRequired()])
    video_type = SelectField(u"type", validators=[DataRequired()], choices=[(('test'), ('test'))])
    address = StringField(u"address", validators=[DataRequired()])
    thumbnail = StringField(u"thumbnail", validators=[DataRequired()])


class CommentForm(Form):
    name = StringField(u"name", validators=[DataRequired()])
    email = StringField(u"email", validators=[DataRequired()])
    comment = TextAreaField(u"comment", validators=[DataRequired(), Length(min=0, max=110)])
    recaptcha = RecaptchaField()