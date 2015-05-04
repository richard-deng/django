import time
import hashlib
print 'The tme is: ', time.time()
print 'The time is: ', time.ctime()
later = time.time() + 15
print '15 secs fron now :' ,time.ctime(later)

#Data to use to calculate md5 checksums

data = open(__file__, 'rt').read()

for i in range(5):
    h = hashlib.sha1()
    print time.ctime() , ': %0.3f %0.3f' % (time.time(), time.clock())
    for i in range(300000):
        h.update(data)

