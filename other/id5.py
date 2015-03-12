import urllib2
from bs4 import BeautifulSoup
httpstr='http://bai.com/all?ac_id=5'
web_cont=urllib2.urlopen(httpstr).read()
soup=BeautifulSoup(web_cont)
i=0
for link in soup.find_all('img'):
    if 'haibao' in link.get('src'):
        print i,link.get('src')
        i+=1
        goal=link.get('src')
        f1=urllib2.urlopen(goal)
        f1c=f1.read()
        if goal[-1]=='g':
            f2=open(str(i)+'.jpeg','wb')
        else:
            f2=open(str(i)+'.gif','wb')
        f2.write(f1c)
        f1.close()
        f2.close()

