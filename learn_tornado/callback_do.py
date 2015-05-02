from tornado import web, ioloop
import datetime
period = 5*1000

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello tornado")

def like_cron():
    print datetime.datetime.now()

def xiaorui():
    print 'xiaori 2s'
def lee():
    print 'lee 3s'

if __name__ == '__main__':
    app= web.Application([(r'/', MainHandler),])
    app.listen(8000)
    ioloop.PeriodicCallback(like_cron, period).start()
    ioloop.PeriodicCallback(lee, 3000).start()
    ioloop.IOLoop.instance().start()
    
