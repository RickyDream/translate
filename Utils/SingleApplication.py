# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/4/16 8:57
# __fileName__ : GoldenCoordinateV2 SingleApplication.py
# __devIDE__ : PyCharm



from PySide2 import QtWidgets as qtw

from PySide2 import QtCore as qtc
from PySide2 import QtNetwork as qtn


class SingleApplication(qtw.QApplication):
    def __init__(self, *args):
        super().__init__(*args)
        self.bRunning = False
        self.localServer = None
        self.mainWindow = None
        # 取应用程序名作为LocalServer的名字
        self.serverName = qtc.QFileInfo(qtc.QCoreApplication.applicationFilePath()).fileName()

        self.initLocalConnection()


    def isRunning(self):
        return self.bRunning



    def initLocalConnection(self):
        """
        // 说明：
        // 通过socket通讯实现程序单实例运行，
        // 初始化本地连接，如果连接不上server，则创建，否则退出
        :return:
        """
        self.bRunning = False
        socket = qtn.QLocalSocket()
        socket.connectToServer(self.serverName)
        if(socket.waitForConnected(500)):
            self.bRunning = True
            # 其他处理，如：将启动参数发送到服务端
            data = ""
            args = qtc.QCoreApplication.arguments()
            if (len(args) > 1):
                data = args[-1]
            socket.write(qtc.QByteArray(bytes(data, 'utf-8')))
            socket.waitForBytesWritten()

            return


        # 连接不上服务器，就创建一个
        self.newLocalServer()



    def newLocalServer(self):
        """
        创建LocalServer
        :return:
        """
        self.localServer = qtn.QLocalServer(self)
        self.localServer.newConnection.connect(self.newLocalConnection)

        if (not self.localServer.listen(self.serverName)):
            # 此时监听失败，可能是程序崩溃时, 残留进程服务导致的, 移除之
            if (self.localServer.serverError() == qtn.QAbstractSocket.AddressInUseError):
                qtn.QLocalServer.removeServer(self.serverName) # < -- 重点
                self.localServer.listen(self.serverName) # 再次监听

    def newLocalConnection(self):
        """
        通过socket通讯实现程序单实例运行，监听到新的连接时触发该函数
        :return:
        """
        socket:qtn.QLocalSocket = self.localServer.nextPendingConnection()
        if (not socket):
            return
        socket.waitForReadyRead(1000)
        socket.deleteLater()
        if (self.mainWindow != None):
           # 激活窗口
           self.mainWindow.raise_()
           self.mainWindow.activateWindow()
           self.mainWindow.setWindowState((self.mainWindow.windowState() & qtc.Qt.WindowMinimized) | qtc.Qt.WindowActive)
           self.mainWindow.show()



