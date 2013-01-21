#-*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template,redirect, url_for
import feedparser
from future import Future
from public.publicFunction import *
from douban_client import DoubanClient
app = Flask(__name__)

def BookRss(uid):
	url = 'http://api.douban.com/people/'+uid
	dom3 = parseString(result)
	root = dom3.documentElement

def DoubanAuth():
	API_KEY = '0e599b6718a074832b0cd23549e15d89'
	API_SECRET = '0ce584ebcdda1f87'
	redirect_uri = 'http://doumao.net/auth'

	SCOPE = 'douban_basic_common,shuo_basic_r,shuo_basic_w'

	client = DoubanClient(API_KEY, API_SECRET, redirect_uri, SCOPE)

	result = client.authorize_url
	# result = client.auth_with_code("birdbirdcatcat")

	# return redirect(url_for(result))
	return result

def DoumaoAuth():
	result = "Welecome to Doumao"
	return result