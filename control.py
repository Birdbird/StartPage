#-*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template
import feedparser
from future import Future
from public.publicFunction import *
from sites.douban import *
app = Flask(__name__)

@app.route('/')
def Index():
	return render_template('index.html',content=ReadMultiRss())

@app.route('/doubanauth')
def DoubanAuthor():
	return render_template('douban.html',content=DoubanAuth())

@app.route('/auth')
def AfterAuth():
	return render_template('auth.html',content=DoumaoAuth())

if __name__ == '__main__':
    app.run(debug=True)