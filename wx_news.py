# encoding: utf-8
# author wengcheng
# 加载包
import requests
import itchat
import datetime
# import times
# from threading import Timer
from news import NewsGetter
from itchat.content import *


KEY1 = 'bfa87c0e11024b5793d2cfd20c828502'
KEY2 = '29a22f48eefa428e8e9d2d902997874d'
KEY3 = 'b9ca706829e1435d92204950202caecd'

def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY3,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    print(msg.fromUserName)
#    ng = NewsGetter()
#    print(ng.getNews())
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
#    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
#    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试

#    return reply or defaultReply



# 处理群聊消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
#    print(msg)
    if(msg.isAt):
        if "早报" in msg['Text'].encode('utf8') :
#            print(msg['ActualNickName'])
            ng = NewsGetter()
            newsText = ng.getNews()
            fromName = '@' + msg['ActualNickName'] + '  ' + 'Morning!' +  '\n'
            today = datetime.date.today()
            formatted_today = today.strftime('20%y-%m-%d') + '   ' + 'Share to do morning reading:' + '\n'
            itchat.send_msg(fromName + formatted_today + newsText, msg['FromUserName'])
        else :
            reply = get_response(msg['Text'])
            itchat.send_msg(reply, msg['FromUserName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
	itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
	itchat.send_msg(u'你好哇,大色狼！', msg['RecommendInfo']['UserName'])

itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()



