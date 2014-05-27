#-*- coding: utf-8 -*-
import os
import re
import pickle
import requests
import time
from datetime import date
URL='http://www.ptt.cc/hotboard.html'
result=tuple(set(re.findall('/bbs/(\w+)/index.html',requests.get(URL).text.encode('utf-8','ignore'))))
PATHs=('data','hotboard')
for path in PATHs:
    if not(os.path.exists(path) and os.path.isdir(path)):
        os.mkdir(path)
    os.chdir(path)
pickle.dump(result,open('hotboard'+str(date.today())+'-'+str(time.localtime()[3])+'-'+str(time.localtime()[4])+'.pickle','wb'))
