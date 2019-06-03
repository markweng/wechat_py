# -*- coding: utf-8 -*-
# author wengcheng
import sys
class Dailylw(object):
    def __init__(self):
        path = sys.path[0] + '/qinghua/masg.txt'
        # print(path)
        f = open(path)
        wordtxt = f.read()
        f.close()
        words = wordtxt.split('\n')
        words.remove('')    
       
        self.words = words            
        self.currentIndex = 0
        # for word in self.words:
        #     # word.replace("\""," ")
        #     # if len(word) == 0 :
        #     #     continue
        #     aword = eval(word)
        #     print(aword)
            

    def getWord(self):
        word = self.words[self.currentIndex] 
        # print(self.currentIndex)
        if self.currentIndex < len(self.words):
            self.currentIndex = self.currentIndex + 1
        else:
            self.currentIndex = 0     
        aword = eval(word)
        # print(aword)
        return(aword)

wordmgr = Dailylw()

# i = 0
# while i < 46:
#     i = i + 1
#     key =   obj.getKey() 
#     print(key)  