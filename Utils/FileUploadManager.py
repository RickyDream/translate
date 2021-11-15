# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/5/8 16:24
# __fileName__ : GoldenCoordinateV2 FileUploadManager.py
# __devIDE__ : PyCharm

from PySide2 import QtWidgets as qtw
from PySide2 import QtCore as qtc
from PySide2 import QtGui as qtg
from Utils.Contants import baseUrl
from PySide2 import QtNetwork as qtn
from Components.MessageBox import MessageBox
from Utils.Helper import fromJson, toJson
import traceback
import queue


class FileUploadManager(qtc.QObject):

    finished = qtc.Signal()
    progress = qtc.Signal(str, float)
    def __init__(self):
        super().__init__()
        # self.progressTimer = qtc.QTimer(self)
        # self.progressTimer.setInterval(1000)
        # self.progressTimer.timeout.connect(self.update_status)
        self.auth = None
        self.baseUrl = baseUrl
        self.fileDic = {}
        self.__replies = {}
        self.hasher = qtc.QCryptographicHash(
            qtc.QCryptographicHash.Md5)
        self.maxSize = 30*1024*1024
        self.__networkManager = qtn.QNetworkAccessManager()
        self.__networkManager.finished.connect(self.__uploadFileDone)

        self.isIdle = True

    def setAuth(self, auth):
        self.auth = auth

    def uploadFiles(self,fileList,api='/upload/public'):
        """
        Private slot to download the selected plugins.
        """
        url = qtc.QUrl(self.baseUrl + api)
        self.filesDownloaded = []
        self.filesToDownload = {}

        self._api = api
        fileStartDic = {}

        for file in fileList:
            tmp = file.split('.')
            ext = tmp[-1] if len(tmp)>1 else ''
            self.hasher.reset()
            with open(file, 'rb') as fh:
                data = fh.read()
            length = len(data)
            print(f'hashing {file},大小为: {length}')
            self.hasher.addData(data)
            hash_string = bytes(self.hasher.result().toHex()).decode('UTF-8')
            file_hash = hash_string if not ext else f"{hash_string}.{ext}"
            if file_hash in self.fileDic:
                continue

            if length > self.maxSize:
                fileParts = {}
                for i in range(0, length, self.maxSize):
                    self.hasher.reset()
                    part_data = data[i:i + self.maxSize]
                    self.hasher.addData(part_data)
                    hashStr = bytes(self.hasher.result().toHex()).decode('UTF-8')
                    fileParts.setdefault(hashStr, {
                        'file_hash': file_hash,
                        'content': part_data,
                        'part_hash': hashStr,
                        'start': i,
                        'file_size': length,
                        'parent_hash': hash_string,
                        'url': url
                    })
                    self.filesToDownload.setdefault(file_hash, {'parts': fileParts})

            else:
                self.filesToDownload.setdefault(file_hash, {
                    'file_hash': file_hash,
                    'content': data,
                    'part_hash': hash_string,
                    'start': 0,
                    'file_size': length,
                    'url': url
                })
            # {'file_hash':'asd','part_hash':'aasd','start':1,'file_size':1123}
            fileStartDic.setdefault(hash_string , {
                'file_hash': file_hash,
                'content': b"",
                'part_hash': "d41d8cd98f00b204e9800998ecf8427e",
                'start': 0,
                'file_size': length,
                'url': url
            })


        self.initUploadFiles(fileStartDic)
            # self.uploadFile(url, file)
        # if not self.progressTimer.isActive():
        #     self.progressTimer.start()
        print("url",url)
    def initUploadFiles(self, fileStartDic):
        for fileHash in fileStartDic:
            self.uploadFile(fileStartDic[fileHash])

    def uploadFile(self, fileInfo,api='/upload/public',doneMethod=None):
        """
        Private slot to download the given file.

        @param url URL for the download (string)
        @param filename local name of the file (string)
        @param doneMethod method to be called when done
        """
        url = qtc.QUrl(self.baseUrl + api)
        self._api = api
        self.isIdle = False
        self.fileInfo = fileInfo
        request = qtn.QNetworkRequest(url)
        request.setRawHeader('api'.encode('utf-8'), self._api.encode('utf-8'))
        if getattr(self, 'auth'):
            request.setRawHeader('auth'.encode('utf-8'), self.auth.encode('utf-8'))
        # request.setAttribute(qtn.QNetworkRequest.CacheLoadControlAttribute,
        #                      qtn.QNetworkRequest.AlwaysNetwork)
        multipart = qtn.QHttpMultiPart(qtn.QHttpMultiPart.FormDataType)


        for key, value in fileInfo.items():
            http_part = qtn.QHttpPart()
            http_part.setHeader(
                qtn.QNetworkRequest.ContentDispositionHeader,
                f'form-data; name="{key}"'
            )
            http_part.setBody(str(value).encode('utf-8'))
            multipart.append(http_part)

        fileHash = fileInfo['file_hash']
        partHash = fileInfo['part_hash']
        filePath = fileInfo['file_path']
        charCount = fileInfo.get('count')
        start = fileInfo.get('start')
        with open(filePath, 'rb') as fr:
            if charCount:
                fr.seek(start)
                content = fr.read(charCount)
            else:
                content = fr.read()
        file_part = qtn.QHttpPart()

        file_part.setHeader(
            qtn.QNetworkRequest.ContentDispositionHeader,
            f'form-data; name="attachment"; filename="{fileHash}"'
        )
        file_part.setBody(content)
        multipart.append(file_part)
        reply = self.__networkManager.post(request, multipart)
        reply.uploadProgress.connect(self.__uploadProgress)

        self.__replies.setdefault(partHash, reply)




    def __uploadFileDone(self, reply):
        """
        Private method called, after the file has been downloaded
        from the Internet.

        @param reply reference to the reply object of the download
        @type QNetworkReply
        @param fileName local name of the file
        @type str
        @param doneMethod method to be called when done
        @type func
        """


        fileInfo = {
            'status': True,
            'errMsg': 'ok'
        }

        self.isIdle = True
        if reply.error() != qtn.QNetworkReply.NoError:
            fileInfo = {
                'errMsg': reply.errorString(),
                'status': False
            }
        # self.fileDic[fileHash].update(fileInfo)
        api = str(reply.request().rawHeader('api'.encode()), 'utf-8')
        reply_bytes = reply.readAll()
        # reply_string = str(reply_bytes, 'unicode_escape')
        reply_string = str(reply_bytes, 'utf-8')
        print(reply_string)
        ret = fromJson(reply_string)

        # self.finished.emit()




    def __downloadCancel(self, reply=None):
        """
        Private slot to cancel the current download.

        @param reply reference to the network reply
        @type QNetworkReply
        """

        if reply is not None:
            reply.abort()

    def __uploadProgress(self, done, total):
        """
        Private slot to show the download progress.

        @param done number of bytes downloaded so far (integer)
        @param total total bytes to be downloaded (integer)
        """
        if total:
            file_hash = self.fileInfo['file_hash']
            desc = f"{file_hash}/{self.fileInfo['part_hash']}"
            sent = self.fileInfo.get('sent') or 0
            percent = round(done+sent//total, 2)*100
            self.progress.emit(file_hash, percent)
            print(desc,done, total, percent)



    def update_status(self):
        print("当前上传状态", self.fileDic)

    def closeEvent(self, event) -> None:
        if hasattr(self, 'restartTimer') and self.restartTimer.isActive():
            self.restartTimer.stop()
        if hasattr(self, 'restartTimer') and self.counterTimer.isActive():
            self.counterTimer.stop()

fileUploadManager = FileUploadManager()








