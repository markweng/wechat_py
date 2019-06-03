# coding=utf-8
import itchat
name = '人多人少 气势不倒'

def getroom_message():
    '''获取群的username，对群成员进行分析需要用到'''
    print('hahhaha')
    itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    RoomList =  itchat.search_chatrooms(name=name)
    if RoomList is None:
        print("%s group is not found!" % (name))
    else:
        print (RoomList[0]['UserName'])
        AnalyseChatFemale()
        return RoomList[0]['UserName']

    
    # RoomList = itchat.get_chatrooms(update=True)[0:]
    # for k in RoomList:        # 获取群名称以及它的username，此方法将会获取到所有的群原因是微信可能不会
    #     nickname = k['NickName']
    #     an = nickname.encode('utf8')
    #     print(nickname)
    #     print(k['UserName'])


def AnalyseChatFemale():
    '''对目标群进行女性的分析，update_chatroom()方法中第一个参数就是getroot_message()中获取到的UserName'''
    global total
    ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
    total = len(ChatRoom['MemberList'])
    female = 0
    print("女生名单及个性签名：")
    for i in range(total):
        if ChatRoom['MemberList'][i]['Sex'] == 2:
            female += 1
            # print(ChatRoom['MemberList'][i]['DisplayName'], ChatRoom['MemberList'][i]["NickName"], ChatRoom['MemberList'][i]['Signature'], sep='******')
    print("女生共有%s人" % (female))


def AnalyseChatMale():
    '''对目标群进行男性的分析'''
    global total
    ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
    total = len(ChatRoom['MemberList'])
    male = 0
    print("男生名单及个性签名：")
    for i in range(total):
        if ChatRoom['MemberList'][i]['Sex'] == 1:
            male += 1
            # print(ChatRoom['MemberList'][i]['DisplayName'], ChatRoom['MemberList'][i]["NickName"], ChatRoom['MemberList'][i]['Signature'], sep='*****')

    print("男生共有%s人" % (male))


def CheckSex():
    '''检测没有备注性别的用户'''
    ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
    total = len(ChatRoom['MemberList'])
    for i in range(total):
        if ChatRoom['MemberList'][i]['Sex'] != 1 and ChatRoom['MemberList'][i]['Sex'] != 2:
            print("这位朋友性别不详:")


def AnalyseChat():
    AnalyseChatFemale()
    AnalyseChatMale()
    CheckSex()
    print("%s 中共有%s人" % (name, total))


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    getroom_message()   # 当需要更新username的时候执行这个方法，可以将下方分析的方法注释掉
    # AnalyseChat()  # 同理当进行分析的时候可以将获取username的方法注释掉