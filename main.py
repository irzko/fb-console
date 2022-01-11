import requests
import os
from bs4 import BeautifulSoup
from requests.api import get
import json
os.system("clear")


URL_FACEBOOK = 'https://mbasic.facebook.com' 
URL_MESSAGES = '{0}/messages/?ref_component=mbasic_home_header&ref_page=MNotificationsController&refid=48'.format(URL_FACEBOOK)
URL_NOTIFICATIONS = '{0}/notifications.php?ref_component=mbasic_home_header&ref_page=MMessagingThreadlistController&refid=11'.format(URL_FACEBOOK)


class Facebook:

    def __init__(self, cookies):
         self.cookies = cookies

    def saveHTML(self, content):
        with open('index.html', 'w') as f:
            f.write(content)
            f.close()


    def get(self, url):
        response = requests.get(url, cookies = self.cookies)
        return response.text

    def getNotifications(self):
        html = self.get(URL_NOTIFICATIONS)
        soup = BeautifulSoup(html, 'html.parser')
        notifications = soup.find_all(class_='bt')
        for noti in notifications:
            print(noti.text)


    def loadMessages(self, url):
        html = self.get(url)
        soup = BeautifulSoup(html, 'html.parser')
        messages = soup.find_all(class_='bt')
        nav_messages = soup.find_all(class_='d bi')
        list_messages = []
        try:
            nav_messages[2].a['href']
            list_messages.append(nav_messages[1].a['href'])
        except:
            list_messages.append(-1)
        i = 1
        for message in messages:
            name = message.find_all('a')[0].text
            print('{0}. {1}'.format(i, name))
            list_messages.append(message.a['href'])
            i += 1
        
        print("\n[N]ext\t\t[P]revious\t\t[Q]uit")
        try:
            list_messages.append(nav_messages[2].a['href'])
        except:
            list_messages.append(nav_messages[1].a['href'])
        return list_messages
    
    def readMessage(self, url):
        html = self.get(url)
        self.saveHTML(html)
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find(id="messageGroup")
        b = a.find_all('div')
        try:
            c = " ".join(b[2].div['class'])
        except:
            try:
                c = " ".join(b[0].div['class'])
            except:
                c = " ".join(b[-12].div['class'])
        mess = soup.find_all(class_= c)
        for m in mess:
            try:
                try:
                    user = m.find_all(class_='bu')[0].find('strong').text
                except:
                    user = m.find_all(class_='bu')[0].text
                print(user, end=' [')
                print(m.find_all('abbr')[0].text, end="]\n")
                mess = m.find_all('span')[0].text
                cx = m.find_all('span')
                for i in cx:
                    if (i.text != '') and ('·' not in i.text) and ('Đã gửi từ Messenger' not in i.text) and ('Gửi từ điện thoại di động' not in i.text):
                        print(i.text.strip())
            except:
                print(m.text, end="\n\n")
            print()



    def getMessages(self):
        n = None
        list_messages = self.loadMessages(URL_MESSAGES)
        while n!= 'q':
            n = input('\nNhap lua chon: ')
            os.system('clear')
            if n == 'n':
                url = URL_FACEBOOK + list_messages[-1]
                list_messages = self.loadMessages(url)
                #Facebook.getMessages(url)
            if n == 'p':
                url = URL_FACEBOOK + list_messages[0]
                list_messages = self.loadMessages(url)
            if n == '1':
                self.readMessage(URL_FACEBOOK + list_messages[1])
            if n == '2':
                self.readMessage(URL_FACEBOOK + list_messages[2])
            if n == '3':
                self.readMessage(URL_FACEBOOK + list_messages[3])
            if n == '4':
                self.readMessage(URL_FACEBOOK + list_messages[4])
            if n == '5':
                self.readMessage(URL_FACEBOOK + list_messages[5])
            if n == '6':
                self.readMessage(URL_FACEBOOK + list_messages[6])
            if n == '7':
                self.readMessage(URL_FACEBOOK + list_messages[7])
            if n == '8':
                self.readMessage(URL_FACEBOOK + list_messages[8])
            if n == '9':
                self.readMessage(URL_FACEBOOK + list_messages[9])
            if n == '10':
                self.readMessage(URL_FACEBOOK + list_messages[10])
            


    def sendMessage(self, id, message):
        id = str(id)
        data = {"fb_dtsg":"AQGyt91SeNpZZjw:23:1641610970",
        "body": message,
        "send":"Gửi",
        "tids":"cid.c."+id,
        "wwwupp":"C3",
        "ids["+id+"]":id,
        "referrer":"",
        "ctype":"",
        "cver":"legacy"
}       
        print(data)
        response = requests.post('https://mbasic.facebook.com/messages/send/?icm=1&refid=12', data=data, cookies = self.cookies)
    
        


cookie = {
    "c_user": "100008153974056",
    "datr": "9O7YYV2g9Yrtn-R8fYjwbhsN",
    "sb": "9O7YYTyLVh0N8tFAEQIDEihR",
    "xs": "31:U73re8L-pAA21g:2:1641814260:-1:6191"
}

facebook = Facebook(cookie)
facebook.getMessages()
#facebook.login('tmkha', '877665')
#facebook.getNotifications()
#facebook.get(URL_FACEBOOK + '/login/device-based/validate-pin/?refid=9')


