#-*- coding: utf-8 -*-
import os
import re
import pickle
import requests
import time
from datetime import date
URL='http://www.ptt.cc/hotboard.html'
PATHs=('data','hotboard')
def hotBordCatch():
	result=tuple(set(re.findall('/bbs/(\w+)/index.html',requests.get(URL).text.encode('utf-8','ignore'))))
	print result
	goPath()
	pickle.dump(result,open('hotboard'+str(date.today())+'-'+str(time.localtime()[3])+'-'+str(time.localtime()[4])+'.pickle','wb'))
	pass
def goPath():
	for path in PATHs:
	    if not(os.path.exists(path) and os.path.isdir(path)):
	        os.mkdir(path)
	    os.chdir(path)
def catchPost(bordName):
	cookies=dict(over18="1")
	html_src=requests.get('http://www.ptt.cc/bbs/'+bordName+'/index.html',cookies=cookies).text.encode('utf-8','ignore')
	print html_src
catchPost("Gossiping")