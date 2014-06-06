import re
import requests
targetURL='http://www.ptt.cc/bbs/YTHT_TaiWan/index'
targetName='O9XXXX9897'
numberOfPage=re.findall('index(\d+)\.html',requests.get(targetURL+'.html').text.encode('utf-8','ignore'))
# numberOfPage 0 = oldestPage ,1 = totalPages
bordThatHave=[]
for i in range (int(numberOfPage[1])+1):
	# print 'http://www.ptt.cc/bbs/YTHT_TaiWan/index'+str(i)+'.html'
	# print re.findall(targetName,requests.get(targetURL+str(i)+'.html').text.encode('utf-8','ignore'))
	if(re.findall(targetName,requests.get(targetURL+str(i)+'.html').text.encode('utf-8','ignore'))):
		cookies=dict(over18="1")
		print i
		# print re.findall("<div class=\"r-ent\"><div class=\"nrec\"></div><div class=\"mark\"></div><div class=\"title\"><a href=\"/bbs/YTHT_TaiWan/(.+)\"?>"
		# 	,requests.get(targetURL+'.html',cookies=cookies).text.encode('utf-8','ignore'))



		# print re.findall("<div class=\"r-ent\"><div class=\"nrec\"></div><div class=\"mark\"></div><div class=\"title\"><a href=\"/bbs/YTHT_TaiWan/M.1206952394.A.F22.html\">"
		# 	,requests.get(targetURL+str(i)+'.html',cookies=cookies).text.encode('utf-8','ignore'))
#(.+)</?a>
# </div><div class=\"meta\"><div class=\"date\"> (.+)</div>?<div class=\"author\">(.+)</div></div></div>"