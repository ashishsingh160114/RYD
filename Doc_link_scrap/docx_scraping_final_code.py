import requests
from bs4 import BeautifulSoup
import re
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


url ="https://www.examveda.com/general-knowledge/practice-mcq-question-on-awards-and-honours/?page=9"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

z=soup.get_text()
#print(z)

z=z.split("\n")
#print(z)

n=[]

d=[]
for i in range(1,71):
    d.append(str(i)+'.')
    
for i in range(0,len(z)):
    for j in d:
        if((z[i].startswith(j))):
            n.append(z[i])
        else:
            pass
    if((z[i].startswith('I=')) or (z[i].startswith('II=')) or (z[i].startswith('III=')) or (z[i].startswith('IV='))):
            n.append(z[i])
    if((z[i]=="A. ") or (z[i]=="B. ") or (z[i]=="C. ") or (z[i]=="D. ") or (z[i]=="E. ")):
        n.append(z[i]+z[i+2])
    if(z[i].startswith("Answer: Option")):
        n.append(z[i])

for i in n:
    print(i)
