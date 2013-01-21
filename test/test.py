import urllib2
from xml.dom.minidom import parse, parseString

def getTagText(root, tag):
	node = root.getElementsByTagName(tag)[0]
	rc = ''
	for node in node.childNodes:
	if node.nodeType in ( node.TEXT_NODE, node.CDATA_SECTION_NODE):
		rc = rc + node.data
	return rc

result = urllib2.urlopen('http://api.douban.com/people/ahbei').read()
# result = '<title>just test</title>'
dom3 = parseString(result)
root = dom3.documentElement
name = dom3.documentElement.tagName == 'entry'
# for node in dom3.getElementsByTagName("entry"):  
# 	print (node, node.tagName, node.getAttribute("uid")) 
# for node in dom3.childNodes:
# 	print node.TextNode.data
print root.nodeName
print root.nodeValue
print root.getElementsByTagName('title')
print getTagText(root,'title')
print getTagText(root,'content')
print root.childNodes
print root.childNodes[1].toxml()
print root.lastChild.toxml()

# print result
# print dom3.documentElement
# print dom3.getElementsByTagName('title')
# print name