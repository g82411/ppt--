#-*- coding:utf-8 -*-
import re
import requests
targetURL='http://www.ptt.cc/bbs/YTHT_TaiWan/index'
targetName='O9XXXX9897'
cookies=dict(over18="1")
count=0
numberOfPage=re.findall('index(\d+)\.html',requests.get(targetURL+'.html',cookies=cookies).text.encode('utf-8','ignore'))
# numberOfPage 0 = oldestPage ,1 = totalPages
bordThatHave=[]
for i in range (int(numberOfPage[1])+1):
	if(re.findall(targetName,requests.get(targetURL+str(i)+'.html',cookies=cookies).text.encode('utf-8','ignore'))):
		r=requests.get(targetURL+str(i)+'.html')
		article=r.text.encode('utf-8','ignore')
		correctArticle=re.sub('\s','',article)
		if r.status_code==200 :
			result=re.findall("<divclass=\"r-ent\"><divclass=\"nrec\"></div><divclass=\"mark\">"
				"</div><divclass=\"title\"><ahref=\"/bbs/YTHT_TaiWan/(.+?)"
				".html\">(.+?)</a></div><divclass=\"meta\"><divclass=\"date\">(\d\d?/\d\d)"
				"</div><divclass=\"author\">(.+?)</div></div></div>",correctArticle)
		else:
			print '503'
		for j in range (len(result)):
			if result[j][3]==targetName :
				print 'page=%s ,\nurl=%s ,\ndate=%s ,\ntitle=%s'%(i,result[j][0],result[j][2],result[j][1])
				print '============================================================================'