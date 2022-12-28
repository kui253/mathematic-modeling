# 爬虫

## 概论：

### 什么是爬虫：

通过编写程序，模拟浏览器上网，然后让其去互联网上抓取数据的过程。

### http协议&https协议

#### 概念

http：服务器和客户端进行数据交互的一种形式

https：安全的超文本传输协议

#### 头信息

##### 请求

1. User-Agent：请求载体的身份标识，这个载体可以是一个电脑的浏览器，也可是一个爬虫
2. Connection：请求成功之后，是断开连接还是保持连接

##### 相应

1. Content-type：服务器响应回客户端的数据类型

## requests模块

模拟浏览器发送请求，指定url，然后发起请求，获取响应数据，数据存储

### 使用demo

1. [爬取文件的案例](./demo_py/requests_test.py)爬取了搜狗首页的数据

2. 采用UA伪装

3. 使用爬虫爬取百度翻译结果

   （这个的实现是由特殊性的，百度翻译的输入框每次输入都会发送一个请求，然后讲得到的翻译信息返回，这昂就方便我们通过浏览器抓包工具找寻翻译结果,最后发现这个东西是出现在aug里面，然后选择新版本的aug，设定程url，然后就是处理数据显示的类型，方便人阅读

4. 爬取豆瓣的官网的评论信息：

   这个demo，没有什么实质性的多的内容，就是要善于发现浏览器什么时候发送请求，这里是滚轮在刷新的时候进行请求，然后就可以直接使用requests去访问就可，上面给的是get就用`requests.get()`上面写的是post就用`requests.post()`然后别忘记使用UA伪装，还有`param`这个字典，就是把url问好”？“之后的内容写道字典里就可以了

5. 国家药检局数据

   - 如果直接对url进行访问，爬取数据没有里面的公司的信息，说明这里面的公司信息是通过某种请求获取的，不能直接获取，数据是动态加载的

     <img src="C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20221227111001477.png" alt="image-20221227111001477" style="zoom:60%;" />

   - 在F12工作状态下，选取xhr，然后可以发现一个访问信息。我要对这个发送，需要访问这个url

   - 观察详情页的url，发现有一个id值，可以通过首页中的json串中获得，然后拼接处详情页的url

     <img src="C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20221227112615491.png" alt="image-20221227112615491" style="zoom:70%;" />

   - 结果发现详情页中的数据也是动态加载出来的，然后通过xhr来发现有一个请求。然后访问这个url

     <img src="C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20221227112926454.png" alt="image-20221227112926454" style="zoom:50%;" />

   - 代码：

     <img src="C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20221227114010201.png" alt="image-20221227114010201" style="zoom:67%;" />

     通过循环实现对每一个页的遍历，然后将这些数据放在一个字典，后面再用for进行访问和存储

### 数据解析

聚焦爬虫：爬取页面中的指定内容

**数据解析的原理**：因为大多数的信息都是有标签的，图片是放在一个url中，放在标签队对应的属性中。

1. 定位指定标签的定位
2. 标签或属性中存储的数据值进行提取

中间就会多一步，数据解析

#### 正则数据解析

<img src="C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20221227145046584.png" alt="image-20221227145046584" style="zoom:67%;" />

1. 第一点需要找到页面下面的图片位置

<img src="C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20221227162945599.png" alt="image-20221227162945599" style="zoom:50%;" />

2. 第二点就是定位图片的url，这里就要使用正则表达式去写

3. 获取多个页面的数据，如果不能直接在url中看出，那就要到抓包工具中去看，看xhr，像我使用的案例，是这里面的每一个文档都是由id的

   <img src="C:\Users\夔whd\AppData\Roaming\Typora\typora-user-images\image-20221227165655058.png" alt="image-20221227165655058" style="zoom:67%;" />

   这个id在首页在搜索这个关键词的xhr中可以找到，我们只要解析出来，然后用这个url访问每个文档就可以找到这些图片，但是不知道为什么这里的图片只有三张。不能找到所有的图片

#### bs4数据解析

1. 实现原理：

   - 标签定位，实例化一个BeautifulSoup对象，讲源码数据加载该对象中
   - 通过调用这个对象中的属性或者方法进行标签定位和数据提取

2. 实现：

   - 本地和互联网

     ```python
     fp = open('./demoData/pic.html','r',encoding='utf-8')
     soup = BeautifulSoup(fp,'lxml')
     print(soup)
     #如果是互联网上的
     pagetext = response.text
     soup = BeautifulSoup(pagetext,'lxml')
     ```

   - 定位标签：主要是几个函数：`soup.select('某种选择器')   soup.find_all('tagname')   soup.find('tagname')`

     [源文件在此，可以参考上面的用法](bs4数据解析\bs4_demo.py)

#### xpath解析