#-*- coding:utf-8 -*-
__author__ = '成'
import urllib
import urllib2
from urllib import quote
print quote(':')
print quote('http://www.baidu.com')

params = urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
print params

f = urllib2.urlopen('http://www.musi-cal.com/cig-bin/query?%s' % params)
print f.read()