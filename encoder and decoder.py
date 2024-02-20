# ceasar cypher decoder
def decoder(message, offset):
    list1 = []
    for i in message:
        asciiNum = ord(i)
        if asciiNum >= 97 and asciiNum <= 123:
            asciiNum = asciiNum + offset
            if asciiNum > 122:
                asciiNum = asciiNum - 26
        list1.append(chr(asciiNum))
    tempStr = ''.join(list1)
    print(tempStr)


# ceasar cypher encoder
def coder(message, offset):
    list1 = []
    for i in message:
        asciiNum = ord(i)
        if asciiNum >= 97 and asciiNum <= 123:
            asciiNum = asciiNum - offset
            if asciiNum < 97:
                asciiNum = asciiNum + 26
        list1.append(chr(asciiNum))
    tempStr = ''.join(list1)
    print(tempStr)


# keyword cypher decoder
def decoder1(message, keyword):
    messageLen = len(message)
    keywordLen = len(keyword)
    tempList = []
    for letter in keyword:
        tempList.append(letter)
    tempList1 = []
    for f in range(round(messageLen / keywordLen)):
        for x in keyword:
            tempList1.append(x)
    keyword = ''.join(tempList1)
    #print(message)
    #print(keyword)
    list1 = []
    not_ = 0
    for i in range(messageLen):
        asciiNum = ord(message[i])
        if asciiNum >= 97 and asciiNum <= 123:
            asciiNum = asciiNum - ord(keyword[i-not_]) + 97
            if asciiNum < 97:
                asciiNum = asciiNum + 26
        else:
            not_ = not_ + 1
        list1.append(chr(asciiNum))
    tempString = ''.join(list1)
    print(tempString)

# keyword cypher encoder
def coder1(message, keyword):
    messageLen = len(message)
    keywordLen = len(keyword)
    tempList = []
    for letter in keyword:
        tempList.append(letter)
    tempList1 = []
    for f in range(round(messageLen / keywordLen)):
        for x in keyword:
            tempList1.append(x)
    keyword = ''.join(tempList1)
    #print(message)
    #print(keyword)
    list1 = []
    not_ = 0
    for i in range(messageLen):
        asciiNum = ord(message[i])
        if asciiNum >= 97 and asciiNum <= 123:
            asciiNum = asciiNum + ord(keyword[i-not_]) - 97
            if asciiNum > 122:
                asciiNum = asciiNum - 26
        else:
            not_ = not_ + 1
        list1.append(chr(asciiNum))
    tempString = ''.join(list1)
    print(tempString)

stringToDecode = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
print(' decode 1:')
decoder(stringToDecode, 10)

message1 = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
print('\n decode 2:')
decoder(message1, 7)

stringToCode = 'ayyyy!'
print('\n code 1:')
coder(stringToCode, 5)

message1 = 'dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'
keyword1 = 'friends'
print('\n decode 3:')
decoder1(message1, keyword1)

message1 = 'hello there my fellow human!'
keyword1 = 'friends'
print('\n code 2:')
coder1(message1, keyword1)