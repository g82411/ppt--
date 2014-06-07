#-*- coding:utf-8 -*-
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
		r=requests.get(targetURL+str(i)+'.html')
		article=r.text.encode('utf-8','ignore')
		correctArticle=re.sub('\s','',article)
		# print correctArticle
		if r.status_code==200 :
			result=re.findall("<divclass=\"r-ent\"><divclass=\"nrec\"></div><divclass=\"mark\">"
				"</div><divclass=\"title\"><ahref=\"/bbs/YTHT_TaiWan/(.+?)"
				".html\">(.+?)</a></div><divclass=\"meta\"><divclass=\"date\">(\d/\d\d)"
				"</div><divclass=\"author\">"+targetName+"</div></div></div>",correctArticle)
			# print result
			# print 'url=%s \n'%(result[0])
			# print 'url=%s \n, title=%s \n, date=%s\n'%(result[0],result[1],result[2])
		else:
			print '503'
for i in range (len(result)):
	 print 'url=%s ,\ndate=%s ,\ntitle=%s'%(result[i][0],result[i][2],result[i][1])
	 print '============================================================================'