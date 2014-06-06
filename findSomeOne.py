import re
import requests
targetURL='http://www.ptt.cc/bbs/YTHT_TaiWan/index'
targetName='O9XXXX9897'
numberOfPage=re.findall('index(\d+)\.html',requests.get(targetURL+'.html').text.encode('utf-8','ignore'))
# numberOfPage 0 = oldestPage ,1 = totalPages
bordThatHave=[]
cookies=dict(over18="1")
for i in range (int(numberOfPage[1])+1):
	if(re.findall(targetName,requests.get(targetURL+str(i)+'.html').text.encode('utf-8','ignore'))):
		print i
		print re.findall("<div class=\"(/w)\">"
		,requests.get(targetURL+str(i)+'.html').text.encode('utf-8','ignore'))
# <div class=\"nrec\"></div><div class=\"mark\"></div><div class=\"title\"><a href=\"/bbs/YTHT_TaiWan/(.+)\.html\">