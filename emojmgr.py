# coding: utf-8
import requests
import os
import re
from threading import Thread
import datetime
import itchat
import json

file_path = './emojs/'
if not os.path.exists(file_path):
    os.mkdir(file_path)

class EmojMgr(object):
    def __init__(self, keyWords,fromName):
        self.fromName = fromName
        word = keyWords.replace('emoj','')
        self.url = 'https://www.doutula.com/api/search?keyword=' + word + '&mime=0&page=1' 
    
    def get_link(self):

        resp = requests.get(self.url)
        json = resp.json()
        linkArr = json['data']['list']
        # firstItem = linkArr[0]
        # return [firstItem['image_url']]
        if len(linkArr) > 0 : 
            urlArr = []
            if len(linkArr) > 10 : 
                for item in linkArr :
                    print(item['image_url'])
                    urlArr.append(item['image_url'])
                    if len(urlArr) >= 10 :
                        break
            else :
                for item in linkArr :
                     print(item['image_url'])
                     urlArr.append(item['image_url'])
            return urlArr
        # print(json['data']['list'])
        return []

    def download(self, link):
        filename = os.path.basename(link)
        try:
            # pic = requests.get(link)
            # if pic.status_code == 200:
                # with open(os.path.join(file_path)+os.sep+filename, 'wb') as fp:
                #     fp.write(pic.content)
                #     fp.close()
            itchat.send_image(file_path + filename, self.fromName)
            itchat.send_msg(link, self.fromName)

            # print(file_path + filename + self.fromName) 
        except Exception as e:
            print e

    def run_main(self):
        threads = []
        links = self.get_link()
        for link in links:
            t = Thread(target=self.download, args=[link])
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

# EmojMgr = EmojMgr(file_path, 'hhh')
# EmojMgr.run_main()