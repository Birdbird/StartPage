#-*- coding: UTF-8 -*-
import urllib2
from xml.dom.minidom import parse, parseString
from flask import Flask
from flask import render_template
import feedparser
from future import Future

#read xml's data by tag
def getTagText(root, tag):
	node = root.getElementsByTagName(tag)[0]
	rc = ''
	for node in node.childNodes:
		if node.nodeType in ( node.TEXT_NODE, node.CDATA_SECTION_NODE):
			rc = rc + node.data
	return rc

def ReadRss(url):
	python_wiki_rss_url = url
	feed = feedparser.parse( python_wiki_rss_url )
	return feed

def ReadMultiRss():
	hit_list = ["http://www.infoq.com/cn/rss/rss.action?token=AWzTX92i7fruv2N5XqNJy1fRwA3qiBT7",
	"http://feeds.nytimes.com/nyt/rss/HomePage"]
	results = []
	for url in hit_list:
		feed = ReadRss(url)
		results.append(feed["items"])
	return results