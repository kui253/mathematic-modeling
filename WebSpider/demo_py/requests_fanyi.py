#爬取百度翻译的结果
import requests
import json
if __name__ == "__main__":

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    url = "https://fanyi.baidu.com/sug"
    #总的url
    while(1):
        kw = str(input("请输入要查找的单词:  "))#你想查找的词条
        if kw == 'q':
            break
        #创建一个字典来存放这个词条
        data = {
            'kw':kw
        }
        response = requests.post(url=url,data=data,headers=headers)#params对应的就是一个字典类型变量
        #text = response.text
        dic_obj = response.json()#确认数据是json数据才可
        #这些地方是将得到的数据调整输出格式，并且不保存
        # fileName = './demoData/'+kw+'.json'
        # with open(fileName,'w',encoding='utf-8') as fp:
        #     json.dump(dic_obj,fp=fp,ensure_ascii=False)#有中文，不能用ASCII编码
        ls = list(dic_obj.values())
        ls_str = str(ls[1]).split("{")
        print(ls_str[1][4:len(ls_str[1])-3])
        
        #print("保存成功！")
    print("翻译结束")