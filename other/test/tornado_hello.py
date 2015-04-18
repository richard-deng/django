import os
import time
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello world")
		
	#def post(self):
	#	self.write("hello world post")

class StoryHandler(tornado.web.RequestHandler):
	def get(self, story_id):
		self.write("You requested the story " + story_id)

class MyFormHandler(tornado.web.RequestHandler):
	def get(self):
		req=self.request
		print 'self.request type is: ', type(self.request)
		print 'protocol: ', req.protocol
		print 'host: ', req.host
		print 'method: ', req.method
		print 'body: ', req.body
		print 'headers: ', req.headers
		self.write('<html><body><form action="/myform" method="post">'
			       '<input type="text" name="message">'
			       '<input type="submit" value="Submit">'
			       '</form></body></html>')

	def post(self):
		req=self.request
		print 'self.request type is: ', type(self.request)
		print 'protocol: ', req.protocol
		print 'host: ', req.host
		print 'method: ', req.method
		print 'body: ', req.body
		print 'headers: ', req.headers
		self.set_header("Content-Type","text/plain")
		self.write("You wrote " + self.get_argument("message"))

class ProfileHandler(tornado.web.RequestHandler):
	def initialize(self, database):
		self.database = database

	def get(self, username):
		self.write('name: '+ username)

class TRedirectHandler(tornado.web.RequestHandler):
	def get(self):
		self.redirect('/', permanent=True)

class NewMainHandler(tornado.web.RequestHandler):
	def get(self):
		items = ['Item 1','Item 2','Item 3']
		self.render("template.html",title="My title", items=items)

class MainHandler2(tornado.web.RequestHandler):
	def get(self):
		if not self.get_cookie("mycookie"):
			self.set_cookie("mycookie","myvalue")
			self.write("Your cookie was not set yet!")
		else:
			self.write("Your cookie was set!")

class MainHandler3(tornado.web.RequestHandler):
	def get(self):
		if not self.get_secure_cookie("mycookie"):
			self.set_secure_cookie("mycookie","myvalue")
			self.write("Your cookie was not set yet!")
		else:
			self.write("Your cookie was set!")

class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie("user")

class MainHandler4(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect("/login")
			return
		name = tornado.escape.xhtml_escape(self.current_user)
		self.write("Hello, " + name)

class MainHanlder5(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		name = tornado.escape.xhtml_escape(self.current_user)
		self.write("Hello, " + name)

class LoginHandler(BaseHandler):
	def get(self):
		self.write('<html><body><form action="/login" method="post">'
			       'Name: <input type="text" name="name">'
			       '<input type="submit" value="Sign in">'
			       '</form></body></html>')
	def post(self):
		self.set_secure_cookie("user",self.get_argument("name"))
		self.redirect("/handler4")

class MainHandler6(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		self.write("Hello , asynchronous")
		time.sleep(6)
		self.finish()

class MainHandler7(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		http = tornado.httpclient.Asynchronous()
		http.fetch("http://friendfeed-api.com/v2/feed/bret", callback=self.on_response)

	def on_response(self, response):
		if response.error:
			raise tornado.web.HTTPError(500)
			json = tornado.escape.json_decode(response.body)
			self.write("Feteched " + str(len(json["entries"])) + " entries " "from the FriendFeed API")
			self.finish()

database='test'

settings = {
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
	"cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
	"login_url":'/login',
	"xsrf_cookie": True,
}

application = tornado.web.Application(
	[
		(r"/", MainHandler),
		(r"/new", NewMainHandler),
		(r"/cookie", MainHandler3),
		(r"/myform", MyFormHandler),
		(r"/handler4", MainHanlder5),
		(r"/async", MainHandler6),
		#(r"/fasync", MainHandler7),
		(r"/login", LoginHandler),
		(r"/story/([0-9]+)", StoryHandler),
		(r"/redirect",TRedirectHandler),
		(r"/user/(.*)", ProfileHandler, dict(database=database)),
		(r"/(apple-touch-icon\.jpg)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
	], **settings
	
)

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()