from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Sm3llin'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Melbourne!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avenger\'s movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title="Home",
                           user=user,
                           posts=posts)
