#解析网站中的图片数据
import requests
if __name__ == '__main__':
    url =   'https://i0.hdslb.com/bfs/article/9b3b952da73786ee90c93bb147c0fe254b6cea03.jpg@942w_1517h_progressive.webp'
    #content返回的是二进制形式的图片数据
    img_data = requests.get(url=url).content
    with open('./demoData/test.png','wb') as fp:
        fp.write(img_data)
#这样就爬取了图片数据