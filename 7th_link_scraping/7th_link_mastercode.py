from bs4 import BeautifulSoup
import requests
import re

html = requests.get("https://jobsandhan.com/mcq-questions-answers/indian-history/indian-national-movement/").content

#1 Recoding
unicode_str = html.decode("utf8")
encoded_str = unicode_str.encode("ascii",'ignore')

news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')

#2 Removing
y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]

d=[]
no_of_Questions=50
for i in range(0,no_of_Questions+1):
    d.append((str(i))+')')

n=[]
for i in range(0,len(y)):
    if(y[i].startswith("Directions (")):
            n.append(y[i])
    for j in d:
        if((y[i].startswith(j))):
            n.append(y[i])
        else:
            pass
    if((y[i].startswith("a) ")) or (y[i].startswith("b) ")) or (y[i].startswith("c) ")) or (y[i].startswith("d) "))):
        n.append(y[i])#(+z[i+2])
    if(y[i].startswith("View AnswerOption – ")):
        n.append(y[i])

for i in n:
    print(i)
