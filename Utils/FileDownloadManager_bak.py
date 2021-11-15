# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/5/8 16:24
# __fileName__ : GoldenCoordinateV2 FileUploadManager.py
# __devIDE__ : PyCharm

import sys
import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc
import re
from Utils.Aria2JsonRpc import *
token = 'download'
port=6800
identity=1
cmdStr = """
aria2c.exe --rpc-listen-all=true   --max-connection-per-server=5 --min-split-size=50M --continue=true --file-allocation=prealloc --enable-mmap=true
"""
"""

urls = ["http://192.168.2.254:8080/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98%E4%B8%8B%E8%BD%BD/0002/%E5%BE%AE%E6%93%8E%E8%A7%86%E9%A2%91/1-6%E3%80%81%E6%A8%A1%E5%9D%97%E5%B7%A5%E6%B5%81%E7%A8%8B%E4%BD%9C.mp4","http://192.168.2.254:8080/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98%E4%B8%8B%E8%BD%BD/0002/%E5%BE%AE%E6%93%8E%E8%A7%86%E9%A2%91/1-7%E3%80%81%E5%BE%AE%E6%93%8E%E5%8F%98%E9%87%8F%E5%B8%B8%E9%87%8F%E8%B7%AF%E7%94%B1%E5%88%9B%E5%BB%BA.mp4","http://192.168.2.254:8080/BaiduNetdiskDownload/%E3%80%8AKotlin%E7%A8%8B%E5%BA%8F%E5%BC%80%E5%8F%91%E5%85%A5%E9%97%A8%E7%B2%BE%E8%A6%81%E3%80%8B.pdf","http://192.168.2.254:8080/BaiduNetdiskDownload/%E3%80%8AKotlin%E4%BB%8E%E9%9B%B6%E5%88%B0%E7%B2%BE%E9%80%9AAndroid%E5%BC%80%E5%8F%91%EF%BC%88%E7%A7%BB%E5%8A%A8%E5%BC%80%E5%8F%91%E4%B8%9B%E4%B9%A6%EF%BC%89%E3%80%8B.pdf","http://192.168.2.254:8080/BaiduNetdiskDownload/%E3%80%8A%E7%96%AF%E7%8B%82Kotlin%E8%AE%B2%E4%B9%89%E3%80%8B.pdf"]
# cmd = ['aria2c', '--rpc-listen-all=false', '--continue']


cmd = list(filter(lambda x: x.strip(), re.split(r'\s', cmdStr)))
aria2RpcServer = Aria2RpcServer(cmd, token, port, identity)
aria2Client:Aria2JsonRpc = aria2RpcServer.launch()
gids = []
for url in urls:
    gid = aria2Client.addUri(uris=[url])
    print(gid)
    gids.append(gid)
while True:
    result = aria2Client.get_global_status()
    globalStat = result['globalStat']
    eta = globalStat.get('eta')

    data = json.dumps(result, sort_keys=True, indent=4, separators=(',',':'))
    print(data)
    time.sleep(1)
    print(''.center(50, '-'))
    if eta and eta == 'finished':
        break

aria2RpcServer.kill()
"""


class DownloadManager(qtc.QObject):
    finished = qtc.Signal(dict)

    def __init__(self):
        super().__init__()
        self.pool = qtc.QThreadPool.globalInstance()
        cmd = list(filter(lambda x: x.strip(), re.split(r'\s', cmdStr)))
        self.aria2RpcServer = Aria2RpcServer(cmd, token, port, identity)


    def do_hashing(self, source, destination, threads):
        """
            调用setMaxThreadCount来设置线程池最大并发数，pool维护的队列可以容纳任意多个QRunnable对象
            但是并发执行的最大线程数只能为maxThreadCount这么多
            Once this is set, we can queue up any number of QRunnable objects in the
        thread pool, but only maxThreadCount threads will actually be
        started up concurrently
        :param source:
        :param destination:
        :param threads:
        :return:
        """
        self.pool.setMaxThreadCount(threads)
        qdir = qtc.QDir(source)

        for filename in qdir.entryList(qtc.QDir.Files):
            filepath = qdir.absoluteFilePath(filename)
            runner = HashRunner(filepath, destination)
            self.pool.start(runner)
        self.pool.waitForDone()
        self.finished.emit()


class HashRunner(qtc.QRunnable):
    file_lock = qtc.QMutex()

    def __init__(self, infile, outfile):
        super().__init__()

        self.infile = infile
        self.outfile = outfile
        # 这里使用QCryptographicHash密码学类来创建一个指定算法的hash对象
        self.hasher = qtc.QCryptographicHash(
            qtc.QCryptographicHash.Md5)

        self.setAutoDelete(True)



    def run(self):
        print(f'hashing {self.infile}')
        self.hasher.reset()
        with open(self.infile, 'rb') as fh:
            self.hasher.addData(fh.read())
        fileName = qtc.QUrl.fromLocalFile(self.infile).fileName()
        hash_string = bytes(self.hasher.result().toHex()).decode('UTF-8')
        """
            使用mutex.lock()即确保在同一时间只有一个线程可以操作文件的写操作，
            其他线程只能等到该线程执行完毕
            This method is much cleaner. By using the mutex context
        manager, we are assured that anything done inside the with
        block is done by only one thread at a time, and other threads
        will wait until the object finishes
        """
        try:
            self.file_lock.lock()
            with open(self.outfile, 'a', encoding='utf-8') as out:
                out.write(f'{fileName}\t{hash_string}\n')
        finally:
            self.file_lock.unlock()



