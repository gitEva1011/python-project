#!/usr/bin/env python 
# coding=utf-8

import tornado.web 
import tornado.gen 
from handlers.base import BaseHandler

import time

"""
class SleepHandler(BaseHandler):
    #装饰器 @tornado.web.asynchronous，它的作用在于将Tornado服务器本身默认的 设置_auto_fininsh值修改为False。 
    @tornado.web.asynchronous    
    def get(self):
        #time.sleep(17)
        tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 17, callback=self.on_response) 
    def on_response(self):        
        self.render("sleep.html")        
        self.finish()
"""

class SleepHandler(tornado.web.RequestHandler):    
    @tornado.gen.coroutine    
    def get(self):        
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time()  #yield tornado.gen.sleep(17)        
        self.render("sleep.html")


class SeeHandler(BaseHandler):    
    def get(self):        
        self.render("see.html")
