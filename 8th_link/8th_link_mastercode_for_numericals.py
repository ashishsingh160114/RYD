import requests
from bs4 import BeautifulSoup
import re

html = requests.get("https://www.examsbook.com/mensuration-questions-and-answers-for-competitive-exams/2").content

#1 Recoding
unicode_str = html.decode("utf8")
encoded_str = unicode_str.encode("ascii",'ignore')

news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')

#2 Removing
y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]

n=[]
for i in y:
    if((i.startswith(" (A)")) or (i.startswith(" (B)")) or (i.startswith(" (C)")) or (i.startswith(" (D)"))  or (i.startswith(" (E)")) or (i.startswith("Correct Answer :"))):
        n.append(i)
    else:
        pass


b_text = news_soup.find_all('strong')
w=[re.sub(r'<.?>',r'',str(a)) for a in b_text]
m=[]
for i in w:
    if(i.startswith("<strong> Q :")):
        #print(i)
        m.append(i)
    else:
        pass

sub1='<strong>'
sub2='</strong>'
p=[]
for i in m:
    if((i.startswith(sub1)) and (i.endswith(sub2))): 
       res = i[(len(sub1)):-(len(sub2))] 
       p.append(res)

q=[]
for i in p:
    print(i)
    for j in range((len(q)),len(n)):
        if(n[j].startswith("Correct Answer :")):
            print(n[j])
            q.append(n[j])
            break
        else:
            print(n[j])
            q.append(n[j])
