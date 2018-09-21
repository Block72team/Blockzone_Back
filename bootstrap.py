# coding=utf-8

from bootstrap_init import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == '__main__':
    # The init place of controllers
    from controller import post_controller

    # The place to register blue print
    app.register_blueprint(post_controller.posts_bp, url_prefix='/api/v1/posts')

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(app.config['HTTP_PORT'])
    IOLoop.instance().start()
