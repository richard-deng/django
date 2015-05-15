import urllib
import urllib2

url='http://127.0.0.1:8080/deal'
post_data={'spam':1,'eggs':2,'bacon':0}
params = urllib.urlencode(post_data)

req=urllib2.urlopen('http://127.0.0.1:8080/hello')
data=req.read()
print 'info: %s' % req.info()
print 'code: %s' % req.getcode()
print 'url: %s' % req.geturl()
print 'data: %s' % data
print 'quote: %s' % urllib.quote(url)
print 'quote plus: %s' % urllib.quote_plus(url)
print 'post_data: %s' % post_data
print 'params: %s' % params
f=urllib.urlopen("http://127.0.0.1:8080/deal?%s" % params)
print 'get data: %s' % f.read()

f=urllib.urlopen(url,params)
print 'post data: %s' % f.read()
