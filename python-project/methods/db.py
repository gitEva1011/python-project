#!/usr/bin/env python
# coding=utf-8

import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='qiwsirtest')
cur = conn.cursor()


