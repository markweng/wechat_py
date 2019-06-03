# coding: utf-8
from datetime import datetime
from threading import Timer
import time
import string
import sys
from qinghua.dailyloverword import wordmgr
import itchat
from news import NewsGetter
reload(sys)
sys.setdefaultencoding('utf-8')
from datasource import datasource

def timedTask():
    Timer(10, task, ()).start()

# 定时任务
def task():
    atime = datetime.now().strftime("%H:%M:%S")
    print(atime)
    strs = atime.split(':')
    second = string.atoi(strs[2])
    # if strs[0] == '16' :
    if strs[0] == '09' and strs[1] == '01' and second < 10 :
        ng = NewsGetter()
        newsText = ng.getNews()
        # print(newsText)
        fromName = '美好的一天从心开始！早安!' +  '\n'
        formatted_today = datetime.now().strftime("20%y-%m-%d") + '   ' + ' 今日早报:' + '\n'
        msg = fromName + "\n" + formatted_today + '\n' + newsText
        for usr in datasource.getSubscribers() :
            itchat.send_msg(msg, usr)
            time.sleep(1)    

    elif strs[0] == '21' and strs[1] == '01' and second < 10 :
        aword = wordmgr.getWord()
        for usr in datasource.getSubscribers() :
            itchat.send_msg(aword, usr)
            itchat.send_msg('晚安！', usr)
            time.sleep(1)  
        # print(aword)
    timedTask()

timedTask()   

