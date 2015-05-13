import web

urls = (
    '/hello','Hello',
    '/deal', 'Deal',
)

class Hello:
    def GET(self):
        return 'hello'

    def POST(self):
        return self.GET()
class Deal:
    def GET(self):
	data=web.input()
	return data

    def POST(self):
        return self.GET()

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
