#-*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template
import feedparser
from future import Future
from public.publicFunction import *
app = Flask(__name__)

@app.route('/')
def Index():
	return render_template('index.html',content=ReadMultiRss())

if __name__ == '__main__':
    app.run(debug=True)