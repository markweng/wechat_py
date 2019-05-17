# encoding: utf-8
import requests
from bs4 import BeautifulSoup

class NewsGetter:
    def getNews(self):
        resp = requests.get('https://m.sohu.com/media/181028')
        #print(resp.content.decode("utf-8"))
        html_doc = resp.content.decode("utf-8")
        soup = BeautifulSoup(html_doc,                      #HTML文档字符串
                             'html.parser',                  #HTML解析器
                             from_encoding = 'utf-8'         #HTML文档编码
                             )
        #print(soup.prettify())
        newsUrl = ""
        for link in soup.find_all('a'):
        #    print(link.get('href'))
        #    print(link.find_all('h4'))
            isFind = False
            for node in link.find_all('h4'):
                text = node.get_text().encode('utf8')
                if text.find("日早读分享") >=0:
                    isFind = True
            #            print(text)
                    break
            if isFind == True:
              newsUrl = 'https://m.sohu.com' + link.get('href')
              break
        #print(newsUrl)

        newsResp = requests.get(newsUrl)
        news_html_doc = newsResp.content.decode("utf-8")
        newsSoup = BeautifulSoup(news_html_doc,                      #HTML文档字符串
                                 'html.parser',                  #HTML解析器
                                 from_encoding = 'utf-8'         #HTML文档编码
                                 )
                                 #print(newsSoup.prettify())
        newsText = ''
        for text in newsSoup.find_all('p'):
        
            if "微信公众号" in text.encode('utf8') :
                continue
            if "版权所有" in text.encode('utf8'):
                continue
            if "杂学杂问" in text.encode('utf8'):
                continue
            if "All Rights Reserve" in text.encode('utf8'):
                continue
#            print(text.get_text())
            newsText = newsText + text.get_text() + "\n"

        return newsText

#obj = NewsGetter()
#print(obj.getNews())
