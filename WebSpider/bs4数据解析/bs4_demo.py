from bs4 import BeautifulSoup
if __name__ == "__main__":
    #将本地的html文件数据加载到该对象中
    fp = open('./demoData/sogou.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    '''
    属性类的命令
    '''
    #print(soup.meta)#soup.tagName:返回的是文档中的第一次出现的文档
    #print('\n',soup.div)#属性
    '''
    find类的命令
    '''
    #print(soup.find('div'))#等同与soup.div,和tagName类似
    #属性定位
    #print(soup.find('div',class_='article-container__content'))#属性定位，这个会把这个属性中的一整个内容都会打印下来
    #print(soup.find_all('p'))#返回符合要求的所有标签，是一个列表
    #print(soup.select('某种选择类型'))#类，标签......选择器都可以


    #print(soup.select('.top-nav > ul a')[0])#使用大于号来区分层级，这个返回的是一个列表类型，这样选择数据即可
    #中间有多个层级也可直接使用一个空格来省略中间的层级，然后指向a
    '''
    1. soup.a.text 这个标签中所有的文本内容,
    2. soup.a.get_text() 这个标签下所有的内容
    3. soup.a.string: 只能获取直系内容
    获取标签中的对应的内容，可以直接通过索引来实现
    soup.a['tageName']
    '''
    print(soup.select('.top-nav > ul a')[0]['href'])#直接提取标签之后，标签下面还有很多的属性值



