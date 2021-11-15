# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/14 10:15
# __fileName__ : GoldenCoordinateV2 RegExp.py
# __devIDE__ : PyCharm

import re

# PwdRegExp = "(?=^.{8,18}$)(?=(?:.*?\d){1})(?=.*[a-zA-Z])(?=(?:.*?[!@#$%*()_+^&}{:;?.]){1})(?!.*\s)[0-9a-zA-Z!@#$%*()_+^&.]*$"
PwdRegExp = "^(?=.*?\d)(?=.*?[a-zA-Z]).{6,}$"
# PhoneRegExp = "^0?(13[0-9]|14[5-9]|15[012356789]|166|17[0-8]|18[0-9]|19[8-9])[0-9]{8}$"
PhoneRegExp = "^0?(13[0-9]|14[0-9]|15[0-9]|16[0-9]|17[0-8]|18[0-9]|19[0-9])[0-9]{8}$"
PhoneCodeRegExp = "\d+"
pwdReg = re.compile(PwdRegExp)
phoneReg = re.compile(PhoneRegExp)
if __name__ == '__main__':

    pwd = "wb997@"
    phone = "15895829286"



    print(pwdReg.match(pwd))
    print(phoneReg.match(phone).string)
