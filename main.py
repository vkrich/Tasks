import requests as rq
import re
import operator
text = rq.get("https://stepik.org/media/attachments/lesson/209719/2.html").text

tmp = r'<code>.+?</code>'
s = re.findall(tmp,text)
print(type(s))
print(s)
tmp1 = r'(<code>)(.+?)(</code>)'
d={}
for i in s:  
  result = re.match(tmp1, i)
  try:
    d[result[2]]+=1
  except:
    d[result[2]]=1  
d=dict(sorted(d.items(),key=operator.itemgetter(1,0)))
result = sorted(d.items(),key=operator.itemgetter(1,0),reverse=True)[:3]

print(result)
  
  

