# coding=utf-8


class DataSource(object):
    def __init__(self):    
        self.userList = []

    def addSubscriberToQueue(self,user):
        self.userList.append(user)

    def removeSubscriberFromQueue(self,user):    
        if user in self.userList :
            self.userList.remove(user)

    def getSubscribers(self):
        return self.userList

datasource = DataSource()
