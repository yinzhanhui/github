import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("客户端")
win.geometry("500x350+200+20")

ck = None#用于储存客户端的信息


def getInfo():
    while True:
        data = ck.recv(1024)#用于接受服务其发送的信息
        text.insert(tkinter.INSERT, data.decode("utf-8"))#显示在信息框上


def connectServer():
    global ck
    ipStr = eip.get()
    portStr = eport.get()
    userStr = euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socked所准守ipv4或ipv6，和相关协议的
    client.connect((ipStr, int(portStr)))#连接ip和端口号:注意输入的端口号是str型而这里的要传入int型
    #2:bind()的参数是一个元组的形式
    client.send(userStr.encode("utf-8"))
    ck = client

    t = threading.Thread(target=getInfo)
    t.start()
    text.insert(tkinter.INSERT, "已连接\n")  # 显示在信息框上

def sendMail():
    friend = efriend.get()
    sendStr = esend.get()

    text.insert(tkinter.INSERT, "我:"+sendStr+"\n")  # 显示在信息框上

    sendStr = friend + ":" + sendStr+"\n"
    ck.send(sendStr.encode("utf-8"))



#下面是界面
labelUse = tkinter.Label(win, text="userName").grid(row=0, column=0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win, textvariable=euser).grid(row=0, column=1)

labelIp = tkinter.Label(win, text="ip").grid(row=1, column=0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=1, column=1)

labelPort = tkinter.Label(win, text="port").grid(row=2, column=0)
eport = tkinter.Variable()

entryPort = tkinter.Entry(win, textvariable=eport).grid(row=2, column=1)

button = tkinter.Button(win, text="启动", command=connectServer).grid(row=3, column=0)
text = tkinter.Text(win, height=10, width=50)
labeltext= tkinter.Label(win, text="显示消息").grid(row=4, column=0)
text.grid(row=4, column=1)

esend = tkinter.Variable()
labelesend = tkinter.Label(win, text="发送的消息").grid(row=5, column=0)
entrySend = tkinter.Entry(win, textvariable=esend).grid(row=5, column=1)

efriend = tkinter.Variable()
labelefriend= tkinter.Label(win, text="发给谁").grid(row=6, column=0)
entryFriend = tkinter.Entry(win, textvariable=efriend).grid(row=6, column=1)

button2 = tkinter.Button(win, text="发送", command=sendMail).grid(row=7, column=0)
win.mainloop()
