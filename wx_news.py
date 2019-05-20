# -*- coding: utf-8 -*-
# author wengcheng
# 加载包
import requests
import itchat
import datetime
# import times
# from threading import Timer
from news import NewsGetter
from emojmgr import EmojMgr
from itchat.content import *


KEY1 = 'bfa87c0e11024b5793d2cfd20c828502'
KEY2 = '29a22f48eefa428e8e9d2d902997874d'
KEY3 = 'b9ca706829e1435d92204950202caecd'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY3,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')

    except:
        return

# 消息
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    nickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    print(nickName)
    # itchat.send_image('./emojs/hahahha.jpg',msg['FromUserName'])
    fromUserName = msg['FromUserName']
    if 'emoj' in msg['Text'] :
        #  if 'weng' in nickName :
            #  newtext = 'my dear，loading...'
            #  itchat.send_msg(newtext,msg['FromUserName'])
        #  else :
            #  newtext = 'loading...'
            #  itchat.send_msg(newtext,msg['FromUserName'])
         emojMgr = EmojMgr(msg['Text'].encode('utf8'),fromUserName)
         emojMgr.run_main()
    else :
        reply = get_response(msg['Text'])
        itchat.send_msg(reply, msg['FromUserName'])

# 处理群聊消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
#    print(msg)
    if(msg.isAt):
        if "早报" in msg['Text'].encode('utf8') :
#            print(msg['ActualNickName'])
            ng = NewsGetter()
            newsText = ng.getNews()
#            print(newsText)
            fromName = '@' + msg['ActualNickName'] + '  ' + 'Morning!' +  '\n'
            today = datetime.date.today()
            formatted_today = today.strftime('20%y-%m-%d') + '   ' + 'Share to do morning reading:' + '\n'
            itchat.send_msg(fromName + '\n' + formatted_today + '\n' + newsText, msg['FromUserName'])
        else :
            reply = get_response(msg['Text'])
            itchat.send_msg(reply, msg['FromUserName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()


itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()
#itchat.logout()



