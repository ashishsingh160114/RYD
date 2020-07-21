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

Enter_url="https://www.gkduniya.com/world-history"
url = Enter_url
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

z=soup.get_text()
z=z.split("\n")


n=[]
d=[]
no_of_Questions=225
for i in range(1,no_of_Questions+1):
    d.append('Q'+(str(i))+'.')
    d.append(' Q'+(str(i))+'.')
    
for i in range(0,len(z)):
    for j in d:
        if((z[i].startswith(j))):
            n.append(z[i])
        else:
            pass
    if((z[i].startswith("(A) ")) or (z[i].startswith("(B) ")) or (z[i].startswith("(C) ")) or (z[i].startswith("(D) ")) or (z[i].startswith("(E) ")) or (z[i].startswith("(a) ")) or (z[i].startswith("(b) ")) or (z[i].startswith("(c) ")) or (z[i].startswith("(d) ")) or (z[i].startswith("(e) "))):
        n.append(z[i])#(+z[i+2])
    if(z[i].startswith("Answer: ")):
        n.append(z[i])


for i in n:
    print(i)
