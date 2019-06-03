# -*- coding: utf-8 -*-
# author wengcheng
import sys
class TLKeyMgr(object):
    def __init__(self):
        path = sys.path[0] + '/tulingmsg/key.txt'
        # print(path)
        f = open(path)
        keytxt = f.read()
        f.close()
        self.keys = keytxt.split('\n')
        self.currentIndex = 0
    # 循环使用key 当当前key调用次数使用完后 自动切换到下一个key
    def getKey(self):
        key = self.keys[self.currentIndex] 
        # print(self.currentIndex)
        if self.currentIndex < len(self.keys):
            self.currentIndex = self.currentIndex + 1
        else:
            self.currentIndex = 0 
        return(key)

keymgr = TLKeyMgr()
# i = 0
# while i < 46:
#     i = i + 1
#     key =   obj.getKey() 
#     print(key)          