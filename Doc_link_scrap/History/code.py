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

Enter_url="https://www.examveda.com/history/practice-mcq-question-on-mughal-empire/?page=1"
url = Enter_url
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

z=soup.get_text()
z=z.split("\n")
d=[]
n=[]
for i in range(1,71):
    d.append(str(i)+'.')
    
for i in z:
    for j in d:
        if((i.startswith(j))):
            n.append(i)
        else:
            pass
    if(i.startswith("Answer: Option")):
        n.append(i)

html = requests.get(Enter_url).content

#1 Recoding
unicode_str = html.decode("utf8")
encoded_str = unicode_str.encode("ascii",'ignore')

news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')

y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]

m=[]
for i in y:
    if((i=="\n\n") or (i=='Each Section contains maximum 70 questions. To get more questions visit other sections.')):
        pass
    else:
        s=''
        for j in i:
            if((j=="\n")):
                pass
            else:
                s=s+j
        m.append(s)


for i in range(0,10,2):
    print(n[i])
    for j in range((i*2),((i*2)+4)):
        print(m[j])
    print(n[i+1])
