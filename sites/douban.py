#-*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template
import feedparser
from future import Future
from public.publicFunction import *
app = Flask(__name__)

def BookRss(uid):
	url = 'http://api.douban.com/people/'+uid
	dom3 = parseString(result)
	root = dom3.documentElement