import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.baidu.com")
#网络请求状态码
print(response)
#网络请求内容
print(".....origin content...............................................")
print(response.content)
print()
print(".....parse content...............................................")
#使用数据内容和lxml包装BeautifulSoup来进行解析
bobj = BeautifulSoup(response.content,'lxml')
#获取到所有<a>标签内容列表
a_list = bobj.find_all('a')
b = 0
text = ''
#遍历<a>标签列表
for a in a_list:
    #提取单个<a>标签内容中的href内容
    href = a.get('href')
    text += href + '\n'
    b = b + 1
    print(str(b) + "  " + href)
#写入文件（若文件不存在则创建）
with open('output/3_output.txt','w') as f:
    f.write(text)
print(".....read content...............................................")
#重新读取文件
with open('output/3_output.txt','r') as f:
    #一次性读取所有内容
    print(f.read())
    #将所有内容按行读取，输出为每行内容的数组
    #print(f.readlines())
