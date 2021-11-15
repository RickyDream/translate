# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/13 23:32
# __fileName__ : GoldenCoordinateV2 Helper.py
# __devIDE__ : PyCharm
import json
import time
import string
import uuid
import requests
import hashlib
from urllib.parse import unquote

headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

def getUniqueData():
    return str(time.time())+str(uuid.uuid4())

def flatDict(data, reserveSection=False):
    ret = {}
    for key in data:
        if not isinstance(data[key], dict):
            ret.setdefault(key, data[key])
        else:
            if not reserveSection:
                ret.update(flatDict(data[key]))
            else:
                tmp = flatDict(data[key])
                for k in tmp:
                    ret.setdefault(f'{key}/{k}', tmp[k])
    return ret


def toJson(data):
    return json.dumps(data, ensure_ascii=False)


def fromJson(data, encoding='utf-8'):
    return json.loads(data, encoding=encoding)

def format_bytes(size):
    '''
    Convert bytes to a human-friendly units..
    '''
    if size < 0x400:
        return '{:d} B'.format(size)
    size = float(size) / 0x400
    for prefix in ('KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB'):
        if size < 0x400:
            return '{:0.02f} {}'.format(size, prefix)
        size /= 0x400
    return '{:0.02f} YiB'.format(size)


def getFileInfoByUrl(url):
    try:
        res = requests.head(url, headers=headers)
        file_size = format_bytes(int(res.headers['Content-Length']))
        file_name = str(res.headers['Content-Disposition'].split('"')[1].encode('ISO-8859-1'), encoding='gbk')
        print(file_size, file_name)
        ret = {
            'file_size': file_size,
            'file_name': file_name,
            'download_url': url,
            'file_hash': getMd5(file_name)
        }
    except:
        file_name = unquote(url.split('/')[-1])
        ret = {
            'file_size': format_bytes(0),
            'file_name': file_name,
            'download_url': url,
            'file_hash': getMd5(file_name)
        }
    return ret




def format_seconds(seconds):
    '''
    Convert seconds to hours, minutes and seconds.
    '''
    time_str = ''
    for base, char in (
        (60, 's'),
        (60, 'm'),
        (24, 'h')
    ):
        seconds, remainder = divmod(seconds, base)
        if seconds == 0:
            return '{:d}{}{}'.format(remainder, char, time_str)
        if remainder != 0:
            time_str = '{:02d}{}{}'.format(remainder, char, time_str)
    return '{:d}d{}'.format(seconds, string)

def getMd5(content):
    m = hashlib.md5()
    m.update(content.encode())
    return m.hexdigest()

if __name__ == '__main__':
    print(getFileInfoByUrl("http://shaoq.tpddns.cn:8099/static/cf9e8b17deb0075b5c928f8b38a86b03.pdf"))





