# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2020/12/31 13:32
# __fileName__ : MasteringGUIProgramming HashManager.py
# __devIDE__ : PyCharm



import queue
from PySide2 import QtCore as qtc
from .HashRunner import HashRunner

class HashManager(qtc.QObject):
    finished = qtc.Signal()
    def __init__(self):
        super().__init__()
        self.pool = qtc.QThreadPool.globalInstance()
        self.queue = queue.Queue()


    def do_hashing(self, fileList, threads):
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

        for filepath in fileList:
            runner = HashRunner(filepath, self.queue)
            self.pool.start(runner)
        self.pool.waitForDone()
        self.queue.put(None)
        self.finished.emit()



