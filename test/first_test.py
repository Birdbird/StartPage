from flask import Flask
from flask import render_template
import feedparser
import urllib2
from xml.dom.minidom import getDOMImplementation
from xml.dom.minidom import parse, parseString
app = Flask(__name__)

@app.route('/')
def hello_world():
	python_wiki_rss_url = "http://www.infoq.com/cn/rss/rss.action?token=AWzTX92i7fruv2N5XqNJy1fRwA3qiBT7"
	feed = feedparser.parse( python_wiki_rss_url )
	return render_template('child.html',content=feed["items"])

@app.route('/test')
def test():
	return render_template('child.html')

@app.route('/test-var/<name>')
def TestVar(name):
	return render_template('hello.html',name=name)

@app.route('/testget')
def TestGet():
	result = urllib2.urlopen('http://api.douban.com/people/ahbei').read()
	dom3 = parseString(result)
	name = dom3.documentElement.tagName == 'entry'
	return render_template('hello.html',name = name)
	# print result

if __name__ == '__main__':
    app.run(debug=True)