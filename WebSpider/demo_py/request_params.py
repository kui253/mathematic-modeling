
'''
UA检测：门户网站的服务器会检测对应请求的载体身份，如果检测到是某一款浏览器
说明是这个请求是一个正常的请求，如果是爬虫，那么可能会被拒绝

UA伪装：让爬虫对应的请求载体伪装成一个浏览器
'''
import requests
if __name__ == "__main__":
    #UA伪装：将对应的UA封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    url = "https://www.sogou.com/"
    #总的url
    kw = 'what'#你想查找的词条
    #创建一个字典来存放这个词条
    param = {
        'query':kw
    }
    
    response = requests.get(url=url,params=param,headers=headers)#params对应的就是一个字典类型变量
    text = response.text
    fileName = './demoData/'+kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(text)
    
    print("保存成功！")