import requests
import json
from selenium import webdriver
from lxml import etree
import time
import datetime
from Utils.Contants import chromedriver
import chardet


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8', 'ignore')
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class SpiderRequest:
    def get(self, url, isAllow302=True, isUsingProxy=False, isSplash=False, **kwargs):
        coding = ('encoding' in kwargs and kwargs.pop('encoding')) or None
        if isSplash:
            return self.splash(url=url), coding
        else:
            content = requests.get(url, **kwargs).content
            ds = chardet.detect(content)
            encoding = ds['encoding']
            # latin1
            print("当前检测到的编码为:", encoding)
            return content.decode(encoding=coding or encoding, errors='ignore'),encoding



    def splash(self, url):


        # 无头浏览器设置（*********增加爬取效率）
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # 无头浏览器需要传入参数在实例化的浏览器对象中*****
        driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
        # 让浏览器指定url发起请求 经测试它有动态加载数据
        driver.get(url)
        return driver.page_source

    def post(self, url, isAllow302=True, isUsingProxy=False, isSplash=False,**kwargs):
        coding = (kwargs.get('encoding') and kwargs.pop('encoding')) or None
        content = requests.post(url,  **kwargs).content
        ds = chardet.detect(content)
        encoding = ds['encoding']
        # latin1
        print("当前检测到的编码为:", encoding)
        return content.decode(encoding=coding or encoding, errors='ignore'), encoding


    @classmethod
    def toJson(cls, data,**kwargs):
        return json.dumps(data, ensure_ascii=False, cls=MyEncoder, **kwargs)
    @classmethod
    def fromJson(cls, data, encoding='utf-8', **kwargs):
        return json.loads(data, encoding=encoding, **kwargs)


spiderRequest = SpiderRequest()
