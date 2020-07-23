import requests
from bs4 import BeautifulSoup
import re

html = requests.get("https://www.examsbook.com/today-gk-current-affairs-questions-2020-july-21/1").content

#1 Recoding
unicode_str = html.decode("utf8")
encoded_str = unicode_str.encode("ascii",'ignore')

news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')
#print(a_text)

#2 Removing
y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]

n=[]
for i in y:
    if(i.endswith("?")):
        n.append('Q : '+i)
    elif((i.startswith(" (A)")) or (i.startswith(" (B)")) or (i.startswith(" (C)")) or (i.startswith(" (D)")) or (i.startswith("Correct Answer :")) or (i.startswith("(A)")) or (i.startswith("(B)")) or (i.startswith("(C)")) or (i.startswith("(D)")) or (i.startswith("(E)")) or (i.startswith(" Ans ."))):
        n.append(i)
    elif(i.startswith("Q.")):
        n.append('Q : '+i)
    else:
        pass


for i in range(0,len(n)):
    if(n[i].startswith("Q :  Q :")):
        pass
    else:
        print(n[i])

