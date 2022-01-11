import os
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    html = f.read()
    f.close()

os.system('clear')
soup = BeautifulSoup(html, 'html.parser')
a = soup.find(id="messageGroup")
b = a.find_all('div')
try:
    c = " ".join(b[2].div['class'])
    if c != 'd bt bu':
        c = 'd bt bu'
except:
    try:
        c = " ".join(b[0].div['class'])
    except:
        c = " ".join(b[-12].div['class'])
mess = soup.find_all(class_= c)
# print(mess)
for m in mess:
    try:
        try:
            user = m.find_all(class_='bu')[0].find('strong').text
        except:
            user = m.find_all(class_='bu')[0].text
            print('check')
        print(user, end=' [')
        print(m.find_all('abbr')[0].text, end="]\n")
        mess = m.find_all('span')[0].text
        cx = m.find_all('span')
        for i in cx:
            if (i.text != '') and ('·' not in i.text) and ('Đã gửi từ Messenger' not in i.text) and ('Gửi từ điện thoại di động' not in i.text):
                print(i.text.strip())
    except Exception as e:
        print(m.text, end="\n\n")
    print()