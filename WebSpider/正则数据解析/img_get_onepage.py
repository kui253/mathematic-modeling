#爬取哔哩哔哩中大理寺日志中的壁纸
#这个智能访问某一个文章页面中的数据
import requests
import re
import os#这个是用来创建文件夹的

if __name__ == "__main__":
    #url = "https://search.bilibili.com/article"
    url = 'https://www.bilibili.com/read/cv6724011'
    if not os.path.exists('./demoData/dalisi'):
        os.mkdir('./demoData/dalisi')#创建文件夹
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    param = {
        'from':'search',
        'spm_id_from':'333.337.0.0',
    }
    pic_text = requests.get(url=url,headers=headers,params=param).text
    # with open('./demoData/pic.html','w',encoding='utf-8') as fp:
    #     fp.write(pic_text)
    ex = '<figure class="img-box" contenteditable="false">.*?<img data-src="(.*?)" width.*?</figure>'
    img_src_list = re.findall(ex,pic_text,re.S)#re.S单行匹配,一般都是单行匹配
    for src in img_src_list:
        src = 'https:'+src#拼接
        img_data = requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name = src.split('/')[-1]#取最后一个
        img_path = './demoData/dalisi/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,"下载成功！")
        
        