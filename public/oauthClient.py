import httplib
import time
import oauth
import feedparser

# fake urls for the test server (matches ones in server.py)
REQUEST_TOKEN_URL = 'http://www.douban.com/service/auth/request_token'
ACCESS_TOKEN_URL = 'http://www.douban.com/service/auth/access_token'
AUTHORIZATION_URL = 'http://www.douban.com/service/auth/authorize'
CALLBACK_URL = ''
RESOURCE_URL = ''

# key and secret granted by the service provider for this consumer application - same as the MockOAuthDataStore
CONSUMER_KEY = 'API Key'
CONSUMER_SECRET = 'API Key Secret'

def runOAuth():
	consumer = oauth.OAuthConsumer(CONSUMER_KEY, CONSUMER_SECRET)
	signature_method_plaintext = oauth.OAuthSignatureMethod_PLAINTEXT()
	signature_method_hmac_sha1 = oauth.OAuthSignatureMethod_HMAC_SHA1()
	oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, callback=CALLBACK_URL, http_url=client.request_token_url)
	# oauth_request.sign_request(signature_method_plaintext, consumer, None)
	# print 'REQUEST (via headers)'
	# print 'parameters: %s' % str(oauth_request.parameters)
	# token = client.fetch_request_token(oauth_request)
	# print 'GOT'
	# print 'key: %s' % str(token.key)
	# print 'secret: %s' % str(token.secret)
	# print 'callback confirmed? %s' % str(token.callback_confirmed)

runOAuth()