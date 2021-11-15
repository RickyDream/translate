



def isJavaCode(s, n=5):
    ks = ['public', 'private', 'void', 'main(', '()', ';','try','finally',"throws",'close', 'from', 'import', 'sys', 'print'
          ,'class','def ']
    for k in ks:
        if k in s:
            n -= 1
    return n<=0




