# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/5/8 16:24
# __fileName__ : GoldenCoordinateV2 FileUploadManager.py
# __devIDE__ : PyCharm


from PySide2 import QtCore as qtc
import re
from Utils.Aria2JsonRpc import *
from .Contants import Aria2c
token = 'download'
port=6800
identity=1
cmdStr = """
--rpc-listen-all=true --max-connection-per-server=5 --min-split-size=50M --continue=true --file-allocation=prealloc --enable-mmap=true --allow-overwrite=true --auto-file-renaming=true
"""


class DownloadManager(qtc.QObject):


    def __init__(self, aria2=None):
        super().__init__()
        cmd = list(filter(lambda x: x.strip(), re.split(r'\s', cmdStr)))
        cmd.insert(0, Aria2c)
        if aria2:
            cmd[0] = aria2
        self.aria2RpcServer = Aria2RpcServer(cmd, token, port, identity)
        self.aria2Client: Aria2JsonRpc = self.aria2RpcServer.launch()

    def killAria2(self):
        self.aria2RpcServer.kill()

    def getAria2Client(self):
        return self.aria2RpcServer.get_a2jr()


downloadManager = DownloadManager()
aria2Client = downloadManager.aria2Client






