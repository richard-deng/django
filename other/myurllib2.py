import urllib2
url='http://127.0.0.1:8080/hello'
try:
    #v1
    #response=urllib2.urlopen(url,timeout=10)
    #print response.read()
    #v2
    #request = urllib2.Request(url)
    #request.add_header('User-Agent','fake-client')
    #request.add_header('Content-Type','application/json')
    #response = urllib2.urlopen(request, timeout=5)
    #print response.read()
    #v3
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler,httpsHandler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url)
    print response.read()
#except urllib2.HTTPError, e:
except:
    print 'time out'
