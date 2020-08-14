import flask
from flask import Flask,render_template

application= app= Flask(__name__)


@app.route('/')
def home():
    return render_template('inde.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')





application.run()(Debug=True)