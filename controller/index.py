#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mojtaba.banaie'


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from EbaySDK import *



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        #########################################################################
        # id = self.application.db.entry.find_one({"_id": 434344})
        # GlobalVars = self.application.GlobalVar
        ####################################################################
        itemList = getItems()

        self.render('index.html',UN="U Are Already Logged In..",Items=itemList)#Global =GlobalVars)



class NotFoundErrorHandler(tornado.web.RequestHandler):
    def get(self,_Error):
        # self.set_status(400)
        self.render("redirects.html",
                    message_title ='متاسفانه صفحه مورد نظر پیدا نشد :(',
                    message_text = 'در حال بازگشت به صفحه اصلی ...',
                    go_to_page = '/',
                    time = 4

                    )
    def post(self,_Error):
        # self.set_status(400)
        self.render("redirects.html",
                    message_title ='متاسفانه صفحه مورد نظر پیدا نشد :(',
                    message_text = 'در حال بازگشت به صفحه اصلی ...',
                    go_to_page = '/',
                    time = 4

                    )

