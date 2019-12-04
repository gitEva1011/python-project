#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

import imp
imp.reload(sys)

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.sleep import SleepHandler
from handlers.see import SeeHandler

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler ),
    (r'/sleep', SleepHandler ),
    (r'/see', SeeHandler ),
    ]
