# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/5 11:26
# __fileName__ : GoldenCoordinate Request.py
# __devIDE__ : PyCharm


import sys
import os
from PySide2 import QtNetwork as qtn

from PySide2 import QtCore as qtc
import json
import requests


class Request(qtc.QObject):
    replyReceived = qtc.Signal(str, str)

    def __init__(self, baseUrl):
        super().__init__()
        self.baseUrl = baseUrl
        self._api = None
        self.nam = qtn.QNetworkAccessManager()
        self.nam.finished.connect(self.on_reply)

    def getBaseUrl(self):
        return self.baseUrl
    def setAuth(self, auth):
        self.auth = auth
    def on_reply(self, reply: qtn.QNetworkReply):
        # api = None
        # headerKeys = list(map(lambda headerName: str(headerName,'utf-8'),reply.request().rawHeaderList()))
        # if 'api' in headerKeys:
        #     api = str(reply.request().rawHeader('api'.encode()), 'utf-8')
        api = str(reply.request().rawHeader('api'.encode()), 'utf-8')
        reply_bytes = reply.readAll()
        # reply_string = str(reply_bytes, 'unicode_escape')
        reply_string = str(reply_bytes, 'utf-8')
        print(reply_string)
        if reply_string:
            dic = json.loads(reply_string, encoding='utf-8')
            if dic.get('errmsg') == '登陆成功':
                self.auth = dic.get('data') and dic['data'].get('auth') or None
        else:
            reply_string = json.dumps({'errcode':1001, "errmsg":"远程服务器已中断，请联系管理员"}, ensure_ascii=False)
        self.replyReceived.emit(api or self._api, reply_string)
        reply.deleteLater()

    def getSync(self, api:str, args=None):
        url = self.baseUrl+api
        data = requests.get(url,params=args, headers={
            'auth': self.auth
        })
        return data
    def postSync(self, api:str, args=None):
        url = self.baseUrl+api
        data = requests.post(url,json=args, headers={
            'auth': self.auth
        })
        return data
    def request(self,url, method='GET', **kwargs):
        headers = {
            'auth': self.auth
        }
        res = requests.request(method, url=url, headers=headers,**kwargs).json()
        return res


    def get(self, api:str, args=None):
        self._api = api
        url = qtc.QUrl(self.baseUrl+api)
        query = qtc.QUrlQuery()
        for key, value in (args or {}).items():
            query.addQueryItem(key, str(value))
        url.setQuery(query)
        self.request:qtn.QNetworkRequest = qtn.QNetworkRequest(url)
        attr: qtn.QNetworkRequest.Attribute
        self.request.setRawHeader('api'.encode('utf-8'), api.encode('utf-8'))

        if getattr(self, 'auth', None):
            self.request.setRawHeader('auth'.encode('utf-8'), self.auth.encode('utf-8'))
        return self.nam.get(self.request)
    def post(self, api:str, data, fileNames=None, ContentType="json"):
        self._api = api
        url = qtc.QUrl(self.baseUrl + api)
        self.request = qtn.QNetworkRequest(url)
        # self.request.setHeader(qtn.QNetworkRequest.ContentTypeHeader, "application/json")
        self.request.setRawHeader('api'.encode('utf-8'), api.encode('utf-8'))
        if getattr(self, 'auth', None):
            self.request.setRawHeader('auth'.encode('utf-8'), self.auth.encode('utf-8'))

        if ContentType == "json":
            self.request.setHeader(qtn.QNetworkRequest.ContentTypeHeader, "application/json")
            self.nam.post(self.request, json.dumps(data, ensure_ascii=False).encode(encoding='utf-8'))
        elif ContentType == "form":
            self.multipart = qtn.QHttpMultiPart(qtn.QHttpMultiPart.FormDataType)
            for key, value in data.items():
                http_part = qtn.QHttpPart()
                http_part.setHeader(
                    qtn.QNetworkRequest.ContentDispositionHeader,
                    f'form-data; name="{key}"'
                )
                http_part.setBody(str(value).encode('utf-8'))
                self.multipart.append(http_part)
            for filename in fileNames:
                with open(filename, 'rb') as fr:
                    filedata = fr.read()
                    file_part = qtn.QHttpPart()
                    file = qtc.QUrl.fromLocalFile(filename).fileName()
                    file_part.setHeader(
                        qtn.QNetworkRequest.ContentDispositionHeader,
                        f'form-data; name="attachment"; filename="{file}"'
                    )
                    file_part.setBody(filedata)
                    self.multipart.append(file_part)
            return self.nam.post(self.request, self.multipart)

    def uploadFile(self, api:str, fileInfo):

        self._api = api
        url = qtc.QUrl(self.baseUrl + api)
        self.request = qtn.QNetworkRequest(url)
        # self.request.setHeader(qtn.QNetworkRequest.ContentTypeHeader, "application/json")
        self.request.setRawHeader('api'.encode('utf-8'), api.encode('utf-8'))
        if getattr(self, 'auth', None):
            self.request.setRawHeader('auth'.encode('utf-8'), self.auth.encode('utf-8'))

        self.multipart = qtn.QHttpMultiPart(qtn.QHttpMultiPart.FormDataType)
        for key, value in fileInfo.items():
            http_part = qtn.QHttpPart()
            http_part.setHeader(
                qtn.QNetworkRequest.ContentDispositionHeader,
                f'form-data; name="{key}"'
            )
            http_part.setBody(str(value).encode('utf-8'))
            self.multipart.append(http_part)

        filePath = fileInfo['file_path']
        charCount = fileInfo.get('count')
        start = fileInfo.get('start')
        fileName = fileInfo['file_name']
        with open(filePath, 'rb') as fr:
            if charCount:
                fr.seek(start)
                filedata = fr.read(charCount)
            else:
                filedata = fr.read()


            file_part = qtn.QHttpPart()

            file_part.setHeader(
                qtn.QNetworkRequest.ContentDispositionHeader,
                f'form-data; name="attachment"; filename="{fileName}"'
            )
            file_part.setBody(filedata)
            self.multipart.append(file_part)

        return self.nam.post(self.request, self.multipart)




if __name__ == '__main__':
    baseUrl = "http://129.211.53.131:3000"
    app = qtc.QCoreApplication(sys.argv)


    request = Request(baseUrl)
    # request.make_request(qtc.QUrl(baseUrl), data={
    #     'id': 1,
    #     'name': 'wbj'
    # })
    request.get('/hooks/app-verify', args={
        'appVer': 1,
        'code': '3245346'
    })
    sys.exit(app.exec_())






