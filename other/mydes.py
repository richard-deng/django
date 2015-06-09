import random
import base64
a=[]
for i in range(0,24):
    a.append(random.randint(0,255))

b=[]

for i in a:
    b.append(chr(i))

c=''.join(b)
d=base64.encodestring(c)
e=d.replace('\n','')
print a
print b
print c
print d
print len(d)
print e
print len(e)


