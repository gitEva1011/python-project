#!/usr/bin/env python 
# coding=utf-8

import tornado.web 
import tornado.gen 
from handlers.base import BaseHandler

import time

class SeeHandler(BaseHandler):    
    def get(self):        
        self.render("see.html")
