from bs4 import BeautifulSoup
import requests
import re
html = requests.get("http://www.indiabix.com/current-affairs/science/").content
#1 Recoding
unicode_str = html.decode("utf8")
encoded_str = unicode_str.encode("ascii",'ignore')

news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')

#2 Removing
y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]

m=[]
for i in range(4,(len(y)-2)):
    if(y[i]=="Explanation:"):
        pass
    else:
        #print(y[i])
        m.append(y[i])

b_text = news_soup.find_all('tr')
z=[re.sub(r'<.+?>',r'',str(a)) for a in b_text]

n=[]
for i in z:
    if((i.startswith("A.")) or (i.startswith("B.")) or (i.startswith("C.")) or (i.startswith("D."))):
        #print(i)
        n.append(i)
    else:
        pass

for i in range(0,10,2):
    print(m[i])
    for j in range((i*2),((i*2)+4)):
        print(n[j])
    print(m[i+1])
