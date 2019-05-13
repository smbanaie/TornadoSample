__author__ = 'mojtaba.banaie'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from EbaySDK import *

class DeleteItemHandler(tornado.web.RequestHandler):
    def get(self):
        ItemID = self.get_argument('ItemID')
        dictstr = endItem(ItemID)
        if dictstr["Ack"] == "Error" :
            self.write(dictstr)
            self.finish()
        else :
            itemList = getItems()
            self.render('index.html', Items=itemList)
