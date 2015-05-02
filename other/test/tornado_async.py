import os
import time
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado
from tornado import httpclient
from tornado import gen
class  AsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http_client = httpclient.AsyncHTTPClient()
        http_client.fetch("http://www.baidu.com",callback=self.on_fetch)
        self.write('hello world')
        self.finish()

    def on_fetch(self, response):
        print 'hello async' + str(response)


class GenAsynchHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = httpclient.AsyncHTTPClient()
        #time.sleep(6)
        #yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 5) 
        yield tornado.gen.Task(http_client.fetch, "http://127.0.0.1:8000/sleep") 
        self.write('hello world sleep')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world now")


application = tornado.web.Application(
        [
                #(r"/", AsyncHandler),
                (r"/", MainHandler),
                (r"/gen", GenAsynchHandler),
        ]
)

if __name__ == "__main__":
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()
