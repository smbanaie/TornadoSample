__author__ = 'mojtaba.banaie'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pycket.session import SessionManager

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        session = SessionManager(self)
        # if session.get()
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        us = self.get_current_user()

        self.application.db.Doctor.find_one({"_id": 4})

        self.render('poem.html', roads=noun1, wood=noun2, made=verb,difference=noun3,user = us,ID=session.get('_id'),INFO=session.get('info'))

