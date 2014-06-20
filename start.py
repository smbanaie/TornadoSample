#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pycket.session import SessionManager
from tornado.options import define, options
from controller.index import IndexHandler
from controller.poem import PoemPageHandler
import pymongo

define("port", default=7080, help="run on the given port", type=int)


def ErrorHandler(self, status_code, **kwargs):
    if status_code == 404 :
        self.render("redirects.html",
                    message_title ='متاسفانه صفحه مورد نظر پیدا نشد :(',
                    message_text = 'در حال بازگشت به صفحه اصلی ...',
                    go_to_page = '/',
                    time = 4
                    )
    else:
        self.render("redirects.html",
                    message_title ='متاسفانه خطایی در سیستم رخ داده است.',
                    message_text = 'اگر همچنان با این خطا مواجه شدید ، با مدیریت کل در ارتباط باشید.',
                    go_to_page = '/',
                    time = 4
                    )

tornado.web.RequestHandler.write_error = ErrorHandler





urlPattern =  [(r'/$', IndexHandler),
                (r'/poem$', PoemPageHandler)
                # (r'/.*',NotFoundHandler)
 ]
# Your app launch code here..
class MedxApplication(tornado.web.Application):

    def __init__(self):
        ##################################################
        # conn = pymongo.Connection("localhost", 27017)
        # self.db = conn["republishan2"]
        # self.GlobalVar = [1,4,8,9]
        ###################################################
        handlers = urlPattern
        settings = dict(
            debug=True,
            cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path= os.path.join(os.path.dirname(__file__), "static"),
            **{
                'pycket': {
                    'engine': 'redis',
                    'storage': {
                        'host': 'localhost',
                        'port': 6379,
                        'db_sessions': 10,
                        'db_notifications': 11,
                        'max_connections': 2 ** 31,
                        },
                    'cookies': {
                        'expires_days': 120,
                        },
                    },
                }

        )
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    # app = MedxApplication(
    #     handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler)],debug=True,
    #     cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    #     template_path=os.path.join(os.path.dirname(__file__), "templates"),
    #     static_path= os.path.join(os.path.dirname(__file__), "static"),
    #     **{
    #     'pycket': {
    #         'engine': 'redis',
    #         'storage': {
    #             'host': 'localhost',
    #             'port': 6379,
    #             'db_sessions': 10,
    #             'db_notifications': 11,
    #             'max_connections': 2 ** 31,
    #             },
    #         'cookies': {
    #             'expires_days': 120,
    #             },
    #         },
    #         }
    #
    #     )


    http_server = tornado.httpserver.HTTPServer(MedxApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()