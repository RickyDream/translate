# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2020/12/31 11:54
# __fileName__ : MasteringGUIProgramming HashRunner.py
# __devIDE__ : PyCharm


import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc
from Utils.Helper import toJson, format_bytes
import os

class HashRunner(qtc.QRunnable):

    def __init__(self, infile, queue, maxSize=30):
        super().__init__()

        self.infile = infile
        self.queue = queue
        self.maxSize = maxSize*1024*1024
        tmp = self.infile.split('.')
        self.fileExt = tmp[-1] if len(tmp)>1 else ''

        # 这里使用QCryptographicHash密码学类来创建一个指定算法的hash对象
        self.hasher = qtc.QCryptographicHash(
            qtc.QCryptographicHash.Md5)

        self.setAutoDelete(True)



    def run(self):
        self.hasher.reset()
        with open(self.infile, 'rb') as fh:
            data = fh.read()
        length = len(data)
        print(f'hashing {self.infile},大小为: {length}')
        self.hasher.addData(data)
        hash_string = bytes(self.hasher.result().toHex()).decode('UTF-8')
        file_hash = hash_string if not self.fileExt else f"{hash_string}.{self.fileExt}"
        fileInfo = {
            'file_hash': file_hash,
            'file_size': length,
            'file_path': self.infile,
            'part_hash': hash_string,
            'file_name': qtc.QUrl.fromLocalFile(self.infile).fileName(),
            'count': length
        }
        if length > self.maxSize:
            fileParts = []
            index = 0
            for i in range(0, length, self.maxSize):
                self.hasher.reset()
                part_data = data[i:i + self.maxSize]
                self.hasher.addData(part_data)
                hashStr = bytes(self.hasher.result().toHex()).decode('UTF-8')
                fileParts.append({
                    'part_hash': hashStr,
                    'start': i,
                    'count': self.maxSize,
                    'sent': index*self.maxSize
                })
                index += 1
            fileParts[-1]['count'] = length-i
            fileInfo['parts'] = fileParts

        self.queue.put(toJson(fileInfo))