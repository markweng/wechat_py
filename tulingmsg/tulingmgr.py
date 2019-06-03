# -*- coding: utf-8 -*-
# author wengcheng

import requests
import sys
from tulingkeymgr import keymgr
reload(sys)
sys.setdefaultencoding('utf-8')

#图灵url
TL_URL = 'http://www.'+'tul'+'ing'+'123.'+'com/open'+'api/'+'api' #分开拼接反被抓

class TLBot(object):
    def __init__(self):    
        self.key = keymgr.getKey()   
    #获取新的key
    def refreshKey(self):
        self.key = keymgr.getKey()
        # print(self.key)
    def getBotMsg(self,msg):
        print(self.key)  
        key = self.key
        data = {
            'key'    : key,
            'info'   : msg,
            'userid' : 'wechat-robot',
            }
        try:
            r = requests.post(TL_URL, data=data).json()
            print(r)
            msg = r.get('text')
            if '当天请求次数已用完' in msg.encode('utf8'):
                self.refreshKey()
                return self.getBotMsg(msg)    
            elif '申请额外加次数' in msg.encode('utf8'):
                self.refreshKey()
                return self.getBotMsg(msg)
            elif 'key不对哦' in msg.encode('utf8'):
                self.refreshKey()
                return self.getBotMsg(msg)

            return r.get('text')
        except:
            return '呵呵'  

tlbot = TLBot()
# obj.getBotMsg('呵呵')
# obj.refreshKey()
        


