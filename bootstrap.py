# coding=utf-8

from bootstrap_init import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == '__main__':
    # The init place of controllers

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(app.config['HTTP_PORT'])
    IOLoop.instance().start()
