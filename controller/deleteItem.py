__author__ = 'mojtaba.banaie'

import tornado.web
from EbayHelper import *


class DeleteItemHandler(tornado.web.RequestHandler):
    def get(self):
        ItemID = self.get_argument('ItemID')
        dictstr = endItem(ItemID)
        if dictstr["Ack"] == "Error" :
            self.write(dictstr)
            self.finish()
        else :
            self.redirect('/')
