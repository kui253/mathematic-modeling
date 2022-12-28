#爬取起点中文网上的三国演义的章节和对应内容
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    url = 'https://book.qidian.com/info/1022511137/#Catalog'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'Cookie':'newstatisticUUID=1672197104_1630101949; traffic_utm_referer=https://cn.bing.com/; _csrfToken=xfsBQ3Ho6ufcgnyEpYLEFiUlclaUBP4K2fg8jmyn; fu=1791010326; e1={"pid":"qd_p_qidian","eid":"","l1":2}; e2={"pid":"qd_p_qidian","eid":"qd_H_Search","l1":2}; Cc2838679FS=55p4.M8oneYhC9dC9WP14fH7HsXpqKBwIlWB3jLtBfM2erqfTzSlYdQWwnIlBwweJBZV5AymbvFYVRJb6U2PzGq; qdrs=0|3|0|0|1; navWelfareTime=1672197133385; showSectionCommentGuide=1; qdgd=1; rcr=1022511137; bc=1022511137; lrbc=1022511137|552949322|0; Cc2838679FT=63_Xy6Ki.Xw0qqqDmYzlU2aGj6WupTHLA3mGuW0blChqEStmACZFVzbo04nnIgn.etPM4oXNj9qFQZ9gJ8aXb2QP0YNhcSUdc_XJXvkZcwvzOyRmvB0yWI.NL4ly9dWpoj88iQWFc.y3pTbDYlBZam_w1SpFA84B4mSgOxfXGB_RhCQXYw29Lc40OM.XqrwYy7aKfbqmf2hhH.9v7kk1P3s8UBr49RaW53oBnGYA5GA.73Lh84PQuj900rUXwc3SXE4ydLhxtDrTv0X5y13ngaVVgp5ADwOX1KOGOelZMhrIvLtDSg09MrARjx5UiUqAjhrGgCXmWZVHS6oUGR10hAy',
        'Host':'book.qidian.com',
        'Referer':'https://book.qidian.com/info/1022511137/'
    }
    page_text = requests.get(url=url,headers=headers).text
    print(page_text)#这里爬取的内容和实际网站上的内容不一样
    # soup = BeautifulSoup(page_text,'lxml')
    # print(soup)
    # chapter = soup.select('.volume > ul > li > h2 > a')
    # print(chapter)