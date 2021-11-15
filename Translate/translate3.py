# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/11/2 3:59
# __fileName__ : html2tree translate3.py
# __devIDE__ : PyCharm
import requests

from urllib.parse import urlencode

##TIMEOUT = 30
TIMEOUT = 3
MAGICHEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

class ResponseError(Exception):
    pass

def get_translation_url(sentance, tolanguage, fromlanguage='auto'):
    """Return the url you should visit to get sentance translated to language tolanguage."""
    query = {'client': 'gtx',
             'dt'    : 't',
             'sl'    : fromlanguage,
             'tl'    : tolanguage,
             'q'     : sentance}
    url = 'https://translate.googleapis.com/translate_a/single?'+urlencode(query)
    return url

def translate(sentance, tolang, fromlang='auto'):
    """Use the power of sneeky tricks to do translation."""
    # Get url from function, which uses urllib to generate proper query
    url = get_translation_url(sentance, tolang, fromlang)
    try:
        # Make a get request to translate url with magic headers
        # that make it work right cause google is smart and looks at that.
        # Also, make request result be json so we can look at it easily
        request_result = requests.get(url, headers=MAGICHEADERS).json()
    except Exception as ex:
        # If it broke somehow, try again
        # NOTE: could cause indefinite recursion
        return translate(sentance, tolang, fromlang)
    # After we get the result, get the right field of the response and return that.
    # If result field not in request result
    def get_parts(lst):
        usefull = []
        for i in lst:
            if isinstance(i, list):
                usefull += get_parts(i)
            elif i:
                usefull.append(i)
        return usefull
    return get_parts(request_result)[0]

if __name__ == '__main__':
    test = """
    Other messaging systems consider the cluster the highest level from an administrative
and deployment perspective, which necessitates managing and configuring each cluster
as an independent system. Fortunately, Pulsar provides an even higher level of
abstraction known as a Pulsar instance, which is comprised of one or more Pulsar clusters
that act together as a single unit and can be administered from a single location,
as shown in figure 2.1
    """
    testStr = ' '.join(list([v.strip() for v in test.split()]))
    print(testStr)
    ts = testStr.split('.')
    for t in ts:
        res = translate(t, tolang='zh-CN')
        print(res)
