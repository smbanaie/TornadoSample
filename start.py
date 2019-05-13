#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from controller.index import IndexHandler
from controller.addItem import AddItemHandler
from controller.deleteItem import DeleteItemHandler
from controller.editItem import EditItemHandler

define("port", default=8000, help="run on the given port", type=int)

urlPattern = [(r'/$',    IndexHandler),
    (r'/addItem', AddItemHandler),
    (r'/deleteItem',DeleteItemHandler),
    (r'/editItem',EditItemHandler)
              ]

    # Your app launch code here..


class SandBoxApplication(tornado.web.Application):

    def __init__(self):
        ###################################################
        handlers = urlPattern
        settings = dict(
            debug=True,
            cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path= os.path.join(os.path.dirname(__file__), "static"),

        )
        tornado.web.Application.__init__(self,handlers,**settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(SandBoxApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()