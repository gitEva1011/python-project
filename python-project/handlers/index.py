#!/usr/bin/env python
# coding=utf-8

import tornado.escape
import methods.readdb as mrd
from handlers.base import BaseHandler

class IndexHandler(BaseHandler): #继承base.py中的类BaseHandler
    def get(self):
        username = mrd.select_columns(table="users",column="username")
        one_user = username[0][0]
        self.render("index.html",user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == int(password):                                     
                #self.write("welcome you: " + username)
                self.set_cookie(username,db_pwd)     #设置cookie 
                #self.set_secure_cookie(username,db_pwd) #以明文加密的方式传输
                #self.set_secure_cookie(username, db_pwd, httponly=True, secure=True) #用httponly和secure属性，用来防范cookie投毒
                self.write(username)
            else:
                #self.write("your password was not right.")
                self.write("-1")
        else:
            #self.write("There is no this user.")
            self.write("-1")

    def set_current_user(self, user): #将用户名写入cookie
        if user:
            #注意这里使用了tornado.escape.json_encode()方法,本质是吧user转化为json,写入到cookie中
            self.set_secure_cookie('user', tornado.escape.json_encode('user'))
        else:
            self.clear_cookie("user")

    class ErrorHandler(BaseHandler): #增加了一个专门用来显示错误的页面
        def get(self):
            self.render("error.html")


        
