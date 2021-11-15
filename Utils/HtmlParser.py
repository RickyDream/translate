# -*- encoding:"utf-8"-*-
from lxml import etree
from bs4 import BeautifulSoup,Tag,PageElement
import json
from urllib.parse import urlparse


def getList(prefix, listXPaths, content):
    items = []
    parentNodes, XPaths = getParentNodesAndXPaths(prefix, listXPaths, content)
    # print("getList:", parentNodes, XPaths)

    for parentNode in parentNodes:
        item = getFields(parentNode, XPaths)
        items.append(item)

    return items



def getFields(parentNode, XPaths):
    item = {}
    for fieldName in XPaths:
        value: dict = XPaths[fieldName]
        fieldMatchExp = value.get('fieldMatchExp')
        vType = value.get('vType')
        typ = 'txtNoTag'
        v = None
        if vType:
            typ, v = vType
        fieldElems = parentNode.xpath(fieldMatchExp) if fieldMatchExp else [parentNode]
        if fieldElems:
            fieldElem = fieldElems[0]
            fieldValue = None
            if typ == 'txtAndTag':
                fieldValue = etree.tostring(fieldElem, with_tail=False, encoding='utf-8', method='html').decode()
            elif typ == 'txtNoTag':
                fieldValue = fieldElem.xpath('string(.)')
                fieldValue = fieldValue and fieldValue.strip()
            elif typ == 'attr' and v:
                fieldValue = fieldElem.attrib.get(v)
            item.setdefault(fieldName, fieldValue)
    return item

def getParentNodesAndXPaths(prefix, XPaths, content):
    tree = etree.HTML(content)
    parentNodes = [tree]
    if prefix:
        parentNodes = tree.xpath(prefix)
    return parentNodes, XPaths

def getRealUrl(detailUrl:str, listUrl:str):
    realUrl = detailUrl
    res = urlparse(detailUrl)
    if not res.netloc:
        if detailUrl.startswith('/'):
            result = urlparse(listUrl)
            realUrl = f"{result.scheme}://{result.netloc}{detailUrl}"
        elif detailUrl.startswith('.'):
            suffix = listUrl.split('/')[-1]
            prefix = listUrl.rstrip(suffix)
            realUrl = prefix + detailUrl
    if not res.scheme and detailUrl.startswith("//"):
        scheme = urlparse(listUrl).scheme
        realUrl = f'{scheme}:{detailUrl}'
    if not urlparse(realUrl).netloc:
        realUrl = getRealUrl('/' + realUrl, listUrl)

    return realUrl
def getDetail(prefix, detailXPaths, content):
    fieldDic = {}
    parentNodes, XPaths = getParentNodesAndXPaths(prefix, detailXPaths, content)
    # print("detailKw:", parentNodes, XPaths)
    if parentNodes:
        fieldDic = getFields(parentNodes[0], XPaths)

    return fieldDic

def cleanWebChars(htmlStr:str):
    charList = ['&nbsp;','&amp;','&lt;','&gt;','&quot;','&qpos;']
    for charStr in charList:
        htmlStr = htmlStr.replace(charStr, '')
    return htmlStr
def delTagsExceptImg(htmlStr, imgAttr='src'):
    body = cleanWebChars(htmlStr)
    soup = BeautifulSoup(body, 'lxml')
    imgs = soup.find_all(name='img')
    for img in imgs:
        img:Tag
        data_src = img.get(imgAttr)
        s = f'###p***###img src="{data_src}"***###/p***'
        img.append(s)
    res = soup.get_text(separator="<p>", strip=True)
    res = res.strip('<p>')
    # 首行缩进
    # res = res.replace('<p>', '</p><p style="text-indent: 2em;">')
    res = res.replace('<p>', '</p><p>')
    res = res.replace('###', '<')
    res = res.replace('***', '>')
    return res

if __name__ == '__main__':
    body = """<p style="text-indent: 2em; text-align: justify;">今年二季度，人民银行依法对18家拒收现金的单位及相关责任人作出经济处罚，处罚金额从1000元至10万元人民币不等。被处罚的单位包括公共服务机构、医院、景区、停车场及保险公司等。</p><p style="text-indent: 2em; text-align: justify;">据悉，今年以来，人民银行坚持宣传引导与严肃惩治相结合，持续推进整治拒收人民币现金工作。对核实为拒收人民币现金的，人民银行将依法处罚并定期予以曝光，切实保护消费者的合法权益，维护人民币法定地位。</p><p style="text-indent: 2em; text-align: justify;">人民银行表示，社会公众遇到拒收现金行为，可依据《中国人民银行公告》（2020年第18号），依法维权。广大经营主体应强化法治观念、维护人民币法定地位，诚信经营、尊重公众支付选择权，提升服务、共同打造现金和谐流通环境。</p><p class="app-image-container"><img src="https://rmrbcmsonline.peopleapp.com/upload/ueditor/image/20210722/1626948908922784.jpg?x-oss-process=style/w10" alt="4.jpg?x-oss-process=style/w10" class="app-image"/></p><p class="app-image-container"><img src="https://rmrbcmsonline.peopleapp.com/upload/ueditor/image/20210722/1626948916774562.jpg?x-oss-process=style/w10" alt="5.jpg?x-oss-process=style/w10" class="app-image"/></p>
    """
    data = delTagsExceptImg(body)
    print(json.dumps(data, ensure_ascii=False))
    # print(data)




