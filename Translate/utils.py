
"""
全角即：Double Byte Character，简称：DBC
半角即：Single Byte Character，简称：SBC
"""



def DBC2SBC(ustring):
    # ' 全角转半角 ”'
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if not (0x0021 <= inside_code and inside_code <= 0x7e):
            rstring += uchar
            continue
        rstring += chr(inside_code)
    return rstring.replace('”','"').replace('“','"')


def SBC2DBC(ustring):
    # ' 半角转全角 ”'
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x0020:
            inside_code = 0x3000
        else:
            if not (0x0021 <= inside_code and inside_code <= 0x7e):
                rstring += uchar
                continue
        inside_code += 0xfee0
        rstring += chr(inside_code)
    return rstring

if __name__ == '__main__':
    s = "”kjhjk“（nihao）"
    print(DBC2SBC(s))