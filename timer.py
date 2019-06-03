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

def timedTask(fromname):
    Timer(10, task, [fromname]).start()

# 定时任务
def task(fromname):
    atime = datetime.now().strftime("%H:%M:%S")
    print(atime)
    strs = atime.split(':')
    second = string.atoi(strs[2])
    if strs[0] == '09' and strs[1] == '01' and second < 10 :
        ng = NewsGetter()
        newsText = ng.getNews()
        # print(newsText)
        fromName = '美好的一天从心开始！早安!' +  '\n'
        formatted_today = datetime.now().strftime("20%y-%m-%d") + '   ' + ' 今日早报:' + '\n'
        itchat.send_msg(fromName + "\n" + formatted_today + '\n' + newsText, fromname)

    elif strs[0] == '21' and strs[1] == '01' and second < 10 :
        aword = wordmgr.getWord()
        itchat.send_msg(aword, fromname)
        itchat.send_msg('晚安！', fromname)
        # print(aword)
    timedTask(fromname)

