class TransferOp(object):
    result = {}
def add_op(cls,fields,code):
    def innerTransfer(self, kwargs):
        for k in kwargs:
            locals().setdefault(k, kwargs[k])
        exec(code.strip())
        for field in fields:
            self.result[field] = locals().get(field)
    innerTransfer.__name__ = f"transfer"
    setattr(cls,innerTransfer.__name__,innerTransfer)

def testOp(fields, opCode, kwargs):
    op = TransferOp()
    add_op(TransferOp, fields, opCode.strip())
    getattr(op, 'transfer')(kwargs)
    logStr = ''
    for k in op.result:
        logStr += f'{k}:{op.result[k]}\n'
    print(logStr)
    return logStr

if __name__ == '__main__':
    opTestCode = """
tmpList = other and other.split("|")
title = tmpList[0]
author = tmpList[1]
    """
    testOp(['title', 'author'], opTestCode.strip(), {'other': "wbj | mumu"})