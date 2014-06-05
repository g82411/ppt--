# -*- coding: utf-8 -*-
import requests
import gevent
from gevent import monkey
import re
try:
	text = requests.get('http://www.ptt.cc/bbs/NTU/M.1401173067.A.041.html').text
except Exception as e:
	print e
print re.sub('<.+>?',',',text)