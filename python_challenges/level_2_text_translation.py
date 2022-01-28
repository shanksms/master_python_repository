"""
Put https://www.pythonchallenge.com/pc/def/ocr.html
in the url to go to next level
"""

def decipher(cipher_text):
    text = []

    for c in cipher_text:
        if c.isalpha():
            _ord = ord(c) - 97
            _ord = (_ord + 2) % 26
            new_ord = _ord + 97
            text.append(chr(new_ord))
        else:
            text.append(c)
    return ''.join(text)

def decipher_method2(cipher_text):
    intab = "abcdefghijklmnopqrstuvwxyz"
    outtab = "cdefghijklmnopqrstuvwxyzab"
    trantab = str.maketrans(intab, outtab)
    return cipher_text.translate(trantab)
if __name__ == '__main__':
    url = "map"
    cipher_text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
     bmgle gr gl zw fylb gq glcddgagclr ylb
     rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
    """
    print(decipher(cipher_text))
    print(decipher_method2(cipher_text))
    print(decipher(url))
    print(decipher_method2(url))