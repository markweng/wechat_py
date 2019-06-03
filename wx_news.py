# coding=utf-8
# # author wengcheng

import requests
import itchat
import datetime
import sys
from news import NewsGetter
from emojmgr import EmojMgr
from analysechat import *
from itchat.content import *
from tulingmsg.tulingmgr import tlbot
from qinghua.dailyloverword import wordmgr
from timer import *
reload(sys)
sys.setdefaultencoding('utf-8')

USER_NAME = '@集市&小行家' #@robot @集市&小行家

# 消息
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    nickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    print(nickName)
    # itchat.send_image('./emojs/hahahha.jpg',msg['FromUserName'])
    fromUserName = msg['FromUserName']
    if 'emoj' in msg['Text']:
        #  if 'weng' in nickName :
            #  newtext = 'my dear，loading...'
            #  itchat.send_msg(newtext,msg['FromUserName'])
        #  else :
            #  newtext = 'loading...'
            #  itchat.send_msg(newtext,msg['FromUserName'])
         emojMgr = EmojMgr(msg['Text'].encode('utf8'),fromUserName)
         emojMgr.run_main()
    else :
        amsg = msg['Text']
        reply = tlbot.getBotMsg(amsg)
        itchat.send_msg(reply, msg['FromUserName'])

# 处理群聊消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg['Text'].encode('utf8'))
    if(msg.isAt):
        if "早报" in msg['Text'].encode('utf8') :
#            print(msg['ActualNickName'])
            ng = NewsGetter()
            newsText = ng.getNews()
#            print(newsText)
            fromName = '@' + msg['ActualNickName'] + '  ' + 'Morning!' +  '\n'
            formatted_today = datetime.now().strftime("20%y-%m-%d") + '   ' + 'Share to do morning reading:' + '\n'
            itchat.send_msg(fromName + '\n' + formatted_today + '\n' + newsText, msg['FromUserName'])
            return    
        elif 'emoj' in msg['Text']:
        #  if 'weng' in nickName :
            #  newtext = 'my dear，loading...'
            #  itchat.send_msg(newtext,msg['FromUserName'])
        #  else :
            #  newtext = 'loading...'
            #  itchat.send_msg(newtext,msg['FromUserName'])
            emojMgr = EmojMgr(msg['Text'].encode('utf8'), msg['FromUserName'])
            emojMgr.run_main()
            return
        elif '情话' in msg['Text'].encode('utf8'):
            aword = wordmgr.getWord()
            itchat.send_msg(aword, msg['FromUserName'])
            return    
        elif '订阅消息' in msg['Text'].encode('utf8'):
            timedTask(msg['FromUserName'])
            return
        else:
            amsg = msg['Text'].replace(USER_NAME,'')
            reply = tlbot.getBotMsg(amsg)            
            itchat.send_msg(reply, msg['FromUserName'])    
    elif "@weng" in msg['Text'].encode('utf8'):
        amsg = '主人可能正在忙哦，你也可以@我聊聊！'
        itchat.send_msg(amsg, msg['FromUserName'])
        getroom_message()

#添加好友  
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()

itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()
# itchat.logout()



