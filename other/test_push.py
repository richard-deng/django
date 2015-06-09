import urllib2, time, hashlib, urllib
#url='http://127.0.0.1:8080/hello'
base_url='http://api.tuisong.baidu.com/rest/3.0/app/query_tags'
url='http://www.baidu.com'
#secretkey='rGPfBB9EXpG00dXmaSHrn9pam29HmRxz'
secretkey='87772555E1C16715EBA5C85341684C58'
#v1
#response=urllib2.urlopen(url,timeout=10)
#print response.read()
#v2
#request = urllib2.Request(base)
#request.add_header('User-Agent','fake-client')
#request.add_header('Content-Type','application/json')
#response = urllib2.urlopen(request, timeout=5)
#print response.read()
#v3
params={
    #'apikey':'Kxz1ImLK4jzvIg2OcrsLeb5s',
    'apikey':'Ljc710pzAa99GULCo8y48NvB',
    'timestamp': 1427180905,
    #'sign':'',
    'expires': 1313293565,
    #'device': 3,
}

def deal_sort(post_dict):
    need_cmp = {}
    for key in post_dict.keys():
	    need_cmp[key] = str(post_dict[key])

    rsort = sorted(need_cmp.items(), key=lambda need_cmp:need_cmp[0])
    rlist= []
    for item in rsort:
	    sitem = '='.join(item)
	    rlist.append(sitem)
    paras_str = ''.join(rlist)

    base='POSThttp://api.tuisong.baidu.com/rest/3.0/app/query_tags'
    need_sign=base+paras_str+secretkey
    print 'need_sign: %s' % need_sign
    #encode_s=hashlib.md5(urllib.quote_plus(need_sign)).hexdigest()
    encode_s=hashlib.md5(need_sign).hexdigest()
    post_dict['sign']=encode_s
    return post_dict


#httpHandler = urllib2.HTTPHandler(debuglevel=1)
#httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#opener = urllib2.build_opener(httpHandler,httpsHandler)
#urllib2.install_opener(opener)
#request = urllib2.Request(base_url)
##request.add_header('User-Agent','Python-urllib/2.7\r\n\r\n')
#request.add_header('User-Agent','BCCS_SDK/3.0 (Linux 3.13.0-52-generic Ubuntu i686 GNU/Linux) Python/2.7 (Baidu Push Server SDK V3.0.0)')
##request.add_header('User-Agent','BCCS_SDK/3.0 (Darwin; Darwin Kernel Version 14.0.0: Fri Sep 19 00:26:44 PDT 2014; root:xnu-2782.1.97~2/RELEASE_X86_64; x86_64) PHP/5.6.3 (Baidu Push Server SDK V3.0.0 and so on..) cli/Unknown ZEND/2.6.0')
##request.add_header('Content-Type','application/json; charset=UTF-8')
#request.add_header('Content-Type','application/x-www-form-urlencoded;charset=utf-8')
#data = urllib.urlencode(deal_sort(params))
#print 'data',data
#response = urllib2.urlopen(request, data, timeout=5)
#print response.read()
##response = urllib2.urlopen(base_url)
##print response.read()



data = urllib.urlencode(deal_sort(params))
print 'data',data
response = urllib.urlopen(base_url, data)
print response.read()
#response = urllib2.urlopen(base_url)
#print response.read()

