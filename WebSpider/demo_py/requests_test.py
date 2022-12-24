#requests库的第一次test使用
#testor ：whd
#需求：爬取搜狗网页的数据
import requests
if __name__ == "__main__":
    #step1:指定Url
    url = "https://www.sogou.com/"
    #step2：发起请求
    response = requests.get(url=url)#返回一个响应对象
    #step3:获取响应数据
    page_text = response.text#字符串形式数据
    print(page_text)
    #step4:存储
    with open('./demoData/sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('数据爬取结束')

