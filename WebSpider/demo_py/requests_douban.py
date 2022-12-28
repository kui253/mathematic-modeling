import requests
import json
if __name__ == "__main__":
    #UA伪装：将对应的UA封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        "type": '24',
        'interval_id': '100:90',
        'action':' ', 
        'start': '0',#从第几部开始取出来
        'limit': '20'#取出第几个电影
    }
    response = requests.get(url=url,params=param,headers=headers)
    list_data = response.json()
    kw = 'douban'
    fileName = './demoData/'+kw+'.json'
    with open(fileName,'w',encoding='utf-8') as fp:
        json.dump(list_data,fp=fp,ensure_ascii=False)#有中文，不能用ASCII编码
        #一开始出现了路径问题

    print('over!')