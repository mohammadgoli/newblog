#_*_ coding: utf-8 _*_ 

from views import db
from models import Post, Project, Way, Video, Comment
from datetime import date 

db.create_all()

# db.session.add(Project('test', 'testaeouaeuaeouao', date(2015,3,3), 0, 1))
# db.session.add(Project(u'تست ۱', u'این یک تست خیلی خیلی قوی است ', date(2015,3,3), 1, 0))
# db.session.add(Project(u'تست ۲', u'ایسیبشسیبشسیبشسیبشسیبشسیبشسیبشسبن یک تست خیلی خیلی قوی است ', date(2015,3,3), 1, 1))

# db.session.add(Way(u'یک'))
# db.session.add(Way(u'دو'))
# db.session.add(Way(u'سه'))
# db.session.add(Way(u'چهار'))

#
# db.session.add(Video('name2', 'aparat2', 'address2', 'sexy_thumbnail2'))
# db.session.add(Video('name3', 'aparat3', 'address3', 'sexy_thumbnail3'))
# db.session.add(Video('name4', 'aparat4', 'address4', 'sexy_thumbnail4'))

db.session.add(Comment('test', 'test', 'test', '1'))

db.session.commit()