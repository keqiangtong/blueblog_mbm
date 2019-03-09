

from faker import Faker
from random import randint

from blueblog.extensions import db
from blueblog.models import Admin,Category,Post

def fake_admin():
    admin = Admin(
        username = 'fake_admin',
        blog_title='fake_blueblog',
        blog_sub_title='fake_sub_title',
        name='fake_name',
        about='this is fake account'
    )
    db.session.add(admin)
    db.session.commit(admin)


fake = Faker()

def fake_category(count=20):
    ctgy =  Category(name='Default')
    db.session.add(ctgy)
    db.session.commit()

    for i in range(count):
            ctgy = Category(name=fake.word())
            db.session.add(ctgy)
            try:
                db.session.commit()
            except:
                db.session.rollback()

def fake_post(count=50):
    for i in range(1,count):
        post =Post(
            title=fake.sentence(),
            body = fake.text(2000),
            category= Category.query.get(randint(1,Category.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()













