# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/13 9:59
# __fileName__ : GoldenCoordinateV2 IPv4Validator.py
# __devIDE__ : PyCharm


from PySide2 import QtGui as qtg


class IPv4Validator(qtg.QValidator):
    """Enforce entry of IPv4 Addresses"""

    def validate(self, string, index):
        # 1. Split the string on the dot character:
        octets = string.split('.')
        # 2. If there are more than 4 segments, the value is invalid:
        if len(octets) > 4:
            state = qtg.QValidator.Invalid
        # 3. If any populated segment is not a digit string, the value is invalid:
        elif not all([x.isdigit() for x in octets if x != '']):
            state = qtg.QValidator.Invalid
        # 4. If not every populated segment can be converted into an
        #         integer between 0 and 255, the value is invalid:
        elif not all([0 <= int(x) <= 255 for x in octets if x != '']):
            state = qtg.QValidator.Invalid
        # 5. If we’ve made it this far into the checks, the value is
        #         either intermediate or valid. If there are fewer than four
        #         segments, it’s intermediate:
        elif len(octets) < 4:
            state = qtg.QValidator.Intermediate
        # 6. If there are any empty segments, the value is intermediate:
        elif any([x == '' for x in octets]):
            state = qtg.QValidator.Intermediate
        # 7. If the value has passed all these tests, it’s acceptable. We can return our tuple:
        else:
            state = qtg.QValidator.Acceptable
        return (state, string, index)


