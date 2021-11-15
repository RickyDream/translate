# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/11/2 3:27
# __fileName__ : html2tree translate2.py
# __devIDE__ : PyCharm
import requests
from googletrans import Translator
from googletrans.models import Translated
from translatepy import Translator as Translator2
import json
word = 'hello'
url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=en&q=" + word
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

default_dest_lang = 'zh-CN'

def google2(s):
    s = preProcess(s)
    translator = Translator(service_urls=[
      'translate.google.cn'
    ])
    t:Translated = translator.translate(s, dest=default_dest_lang)

    return t




def translate(testStr):

    translator = Translator2()
    result = translator.translate(testStr, 'zh')
    print(result.result)


def google1():

    request_result = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=fr&q=Hello")
    translated_text = json.loads(request_result.text)[0][0][0]
    print(translated_text)




"""
l = language
s = sentence
"""
def trans1(l, s):
    return \
    requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl={l}&q={s}").json()[0][
        0][0]


def trans2(l, s):
    return requests.get(f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl={l}&q={s}").json()[
        "sentences"][0]["trans"]

def preProcess(s):
    return ' '.join([v.strip() for v in s.split() if v.strip()])

def google():
    request_result = requests.get(url, headers=headers, proxies={
        'http': '127.0.0.1:10809'
    }).json()

    print(request_result)
    print('[In English]: ' + request_result['alternative_translations'][0]['alternative'][0]['word_postproc'])
    print('[Language Dectected]: ' + request_result['src'])

def bing():
    import requests

    url = 'https://cn.bing.com/ttranslatev3'

    post_header = {}
    post_header['Host'] = 'www.bing.com'
    post_header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    post_header['Accept'] = '*/*'
    post_header['Accept-Language'] = 'en-US,en;q=0.5'
    post_header['Accept-Encoding'] = 'gzip, deflate'
    post_header['Referer'] = 'https://www.bing.com/'
    post_header['Content-Type'] = 'application/x-www-form-urlencoded'
    post_header['Connection'] = 'keep-alive'

    parameters_payload = {'IG': '839D27F8277F4AA3B0EDB83C255D0D70', 'IID': 'translator.5033.3'}
    data_payload = {'text': 'Platypus', 'fromLang': 'en', 'to': 'zh-CN'}
    resp = requests.post(url, headers=post_header, params=parameters_payload, data=data_payload)

    print(resp.content.decode())

if __name__ == '__main__':
    test = """
        Other messaging systems consider the cluster the highest level from an administrative
    and deployment perspective, which necessitates managing and configuring each cluster
    as an independent system. Fortunately, Pulsar provides an even higher level of
    abstraction known as a Pulsar instance, which is comprised of one or more Pulsar clusters
    that act together as a single unit and can be administered from a single location,
    as shown in figure 2.1
        """
    testStr = ' '.join([v.strip() for v in test.split()])
    print(testStr)
    google2(testStr)
    # translate(testStr)
    # google2()
