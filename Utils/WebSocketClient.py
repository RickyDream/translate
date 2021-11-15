# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/27 14:55
# __fileName__ : GoldenCoordinateV2 WebSocketClient.py
# __devIDE__ : PyCharm

import sys

from PySide2 import QtCore as qtc
from PySide2 import QtWebSockets as qtws
from PySide2 import QtNetwork as qtn
from Utils.Contants import baseHost


class WebSocketClient(qtc.QObject):

    received = qtc.Signal(str, str)
    error = qtc.Signal(str)

    def __init__(self, auth, username=None):
        super().__init__()

        self.maxRetries = 20
        self.connAddress = f"ws://{baseHost}/socket/chat?auth={auth}"
        self.username = username
        self.auth = auth
        self.webSocket = qtws.QWebSocket()
        self.webSocket.ignoreSslErrors()
        self.webSocketConnect()
        self.webSocket.connected.connect(self.webSocketConnected)

        self.webSocket.textMessageReceived.connect(self.recvMsg)
        self.webSocket.stateChanged.connect(self.webSocketStateChanged)
        self.webSocket.error.connect(self.webSocketError)



    def setAuth(self, auth):
        self.auth = auth
        self.connAddress = f"ws://{baseHost}/socket/chat?auth={auth}"

    def webSocketConnect(self):
        self.webSocket.open(qtc.QUrl(self.connAddress))

    def webSocketStateChanged(self, state:qtn.QAbstractSocket.SocketState):
        # socketStateEnum = qtn.QAbstractSocket.SocketState.__dict__['values']
        print("state", state)
        if self.maxRetries < 0:
            self.webSocket.stateChanged.disconnect(self.webSocketStateChanged)
        # print(socketStateEnum)
        try:
            if state == qtn.QAbstractSocket.ClosingState or state == qtn.QAbstractSocket.UnconnectedState:
                self.webSocketConnect()
            self.received.emit("stateType", str(state))
        except Exception as e:
            print(e)
        self.maxRetries -= 1

    # 客户端接收消息
    def recvMsg(self, message:str):
        # msg = message.encode('utf-8').decode('unicode_escape')
        self.received.emit("msgType", message)
    def send_message(self, message:str):
        self.webSocket.sendTextMessage(message)

    def webSocketConnected(self):
        print("连接成功")
        if self.maxRetries < 0:
            self.webSocket.stateChanged.connect(self.webSocketStateChanged)
        self.maxRetries = 20
        if hasattr(self, 'timerForReTry'):
            if self.timerForReTry.isActive():
                self.timerForReTry.stop()
        # self.webSocket.sendTextMessage("Hello, world!")
    # def webSocketDisConnected(self):
    #     print("断开连接")
    #     self.error.emit("close")



    def webSocketError(self, socket_error):
        error_index = (qtn.QAbstractSocket
                       .staticMetaObject
                       .indexOfEnumerator('SocketError'))

        error = (qtn.QAbstractSocket
                 .staticMetaObject
                 .enumerator(error_index)
                 .valueToKey(socket_error))
        message = f"There was a network error: {error}"
        print("webSocketError", message)
        if not hasattr(self, 'timerForReTry'):
            self.retryConnect()
        elif not self.timerForReTry.isActive():
            self.timerForReTry.start()
        self.error.emit(message)
    def retryConnect(self):
        self.timerForReTry = qtc.QTimer(self)
        self.timerForReTry.setInterval(5000)
        self.timerForReTry.timeout.connect(self.webSocketConnect)
        self.timerForReTry.start()


    # def process_datastream(self):
    #     for socket in self.connections:
    #         self.datastream = qtc.QDataStream(socket)
    #         if not socket.bytesAvailable():
    #             continue
    #         # raw_message = self.datastream.readQString()
    #         raw_message = self.datastream.readRawData(1024)
    #         print(raw_message)
    #         # if raw_message and self.delimiter in raw_message:
    #         #     username, message = raw_message.split(self.delimiter, 1)
    #         #     self.received.emit(username, message)

if __name__ == '__main__':
    app = qtc.QCoreApplication([])
    host = "shaoq.tpddns.cn"
    port = "8099"
    auth = "6b5a1b2b39d837cf97d9e8de63f7bf85a5227348c70a3adcb191d207fd239dff"
    websocket = WebSocketClient(auth, "wbj")
    sys.exit(app.exec_())


