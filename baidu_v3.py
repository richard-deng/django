# coding: utf-8
import os, sys
import urllib, urllib2
import json, uuid, time
import hashlib
import traceback


secretkey='rGPfBB9EXpG00dXmaSHrn9pam29HmRxz'
comm_args={
    "apikey": 'Kxz1ImLK4jzvIg2OcrsLeb5s',
	"timestamp": time.time(),
	"sign": '',
	"expires": 1313293565,
	"device_type": 3,
	"tag":'dcbaidu3'
}

def deal_sort(post_dict):
    print 'new'
    print post_dict
    need_cmp = {}
    for key in post_dict.keys():
	    #need_cmp[key] = str(post_dict[key])
	    need_cmp[key] = str(post_dict[key])

    rsort = sorted(need_cmp.items(), key=lambda need_cmp:need_cmp[0])
    rlist= []
    for item in rsort:
	    sitem = '='.join(item)
	    rlist.append(sitem)
    paras_str = ''.join(rlist)

    #base='POSThttp://api.tuisong.baidu.com/rest/3.0/report/query_msg_status'
    base='POSThttp://api.tuisong.baidu.com/rest/3.0/app/create_tag'
    need_sign=base+paras_str+secretkey
    encode_s=hashlib.md5(urllib.quote_plus(need_sign)).hexdigest()
    post_dict['sign']=encode_s
    print 'new'
    print post_dict
    return post_dict

def send(data):
    post_str=urllib.urlencode(data)
    print 'post str'
    print post_str
    try:
        url='http://api.tuisong.baidu.com/rest/3.0/app/create_tag'
        req=urllib2.Request(url, post_str)
        resp=urllib2.urlopen(req)
        ret=resp.read()
        print ret
    except:
        print traceback.format_exc()
        print False

if __name__ == '__main__':
    send(deal_sort(comm_args))
