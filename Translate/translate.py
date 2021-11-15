# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/11/2 1:36
# __fileName__ : html2tree translate.py
# __devIDE__ : PyCharm
# from pygoogletranslation import Translator
# translator = Translator()
# translator.translate('Good Morning', dest='zh-CN')
# # <Translated src=ko dest=ta text=காலை வணக்கம். pronunciation=Good evening.>
# translator.translate('안녕하세요.', dest='ja')
# # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
# translator.translate('veritas lux mea', src='la')
# # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

from googletrans import Translator
translator = Translator()
print(translator.translate('Sunday', dest='zh-CN').text)