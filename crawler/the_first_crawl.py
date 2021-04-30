import requests

#requests 入门
#客户端渲染比较常见  一次发框架  再一次发数据
url='https://www.sogou.com/web?query=周杰伦'   #地址栏用get


qq={
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
 }   #处理一个小反爬  User-Agent在 web Headers

resp=requests.get(url,headers=qq)
print(resp.text)  #看页面源代码