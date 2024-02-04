from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    # run in debug mode
    app.run(debug=True)

''' create database
>>> from <your_app> import app, db
>>> with app.app_context():
...     db.create_all() # create both User and Post
>>> from flaskblog import User, Post
>>> with app.app_context():
...     user_1 = User(username='Mike', email='M@m.ca', password='password')
...     db.session.add(user_1)
...     db.session.commit()
...     User.query.all()
...
[User('Mike', 'M@m.ca', 'default.jpg')]
>>> 
>>> with app.app_context():
...     User.query.first()
...     user = User.query.filter_by(username='Mike').first()
...     user.id # user ID
...     user = User.query.get(1) # same as above
...     post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
...     db.session.add(post_1)
...     db.session.commit()
...     post = post.query.first()
...     post.author # see backref in User
...     db.drop_all() # delete all table

'''

''' password
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('testing')
b'$2b$12$k/KmP7VUQ3q0hXE9znAAauNKU6vLcuBalLDA7tSU6DUVIqImQU5Xe'
>>> bcrypt.generate_password_hash('testing')
b'$2b$12$WNjhWssnzHmfloGu5WB0ze5idE3X0CuRDw8Wu1I1AeVu7zkFc17Ha'
>>> hash_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
>>> bcrypt.check_password_hash(hash_pw, 'password')
False
>>> bcrypt.check_password_hash(hash_pw, 'testing')
True
>>>

'''


# posts = [
#     {
#         'author' : 'Mike Zhang',
#         'title': "My Blog Page",
#         'content': "The day I started this project",
#         'date_posted': 'Jan 26 2024'
#     },
#     {
#         'author' : 'Corey Schafer',
#         'title': "Credit",
#         'content': "I am the teacher",
#         'date_posted': 'Jan 26 2024'
#     }
# ]

