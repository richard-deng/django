#-*- coding:utf-8 -*-
__author__ = '成'

import urllib
import urllib2
import hashlib
import time
import json
import traceback


message_dic = {
    "title": 'class push to user 2',
    "description": 'hello.....',
}
message = json.dumps(message_dic)
apikey='Kxz1ImLK4jzvIg2OcrsLeb5s'
secretkey='rGPfBB9EXpG00dXmaSHrn9pam29HmRxz'
user_id='2651946417'
channel_id='4390574681195043318'
push_type=1
device_type=3
message_type=1
deploy_status=1
tag='1'

common_params = {
    'apikey':apikey,
    'timestamp':time.time(),
    'expires':200000,
    'device_type':device_type
}

def deal_sign(post_dict):
    need_cmp = {}
    for key in post_dict.keys():
        need_cmp[key] = str(post_dict[key])

    rsort = sorted(need_cmp.items(), key=lambda need_cmp:need_cmp[0]) 
    rlist = []
    for item in rsort:
        sitem = '='.join(item)
        rlist.append(sitem)
    
    need_sign = 'POSThttp://api.tuisong.baidu.com/rest/3.0/app/query_tags' + ''.join(rlist) + secretkey 
    encode_s = hashlib.md5((need_sign)).hexdigest()
    post_dict['sign'] = encode_s
    
    print post_dict
    

    url = 'http://api.tuisong.baidu.com/rest/3.0/app/query_tags'
    headers = {'Content-Type': 'application/json;charset=utf-8', 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    post_str = urllib.urlencode(post_dict)
    

    print 'after encode post dict: ',post_str
    try:
        #req = urllib2.Request(url=url, data='', headers=headers)
        
        #print 'req', req
        req = urllib2.Request(url, post_str, headers)
        print req
        resp = urllib2.urlopen(req)
        print 'resp', resp
        ret = resp.read()
        print ret
        return ret
    except:
        print traceback.format_exc()
        print False


if __name__ == '__main__':
	deal_sign(common_params)