def challengeUrlOpen(url, php = False):
    import webbrowser
    suffix = '.html'
    if php: suffix = '.php'
    webbrowser.open('http://www.pythonchallenge.com/pc/def/' + url + suffix)

def level0():
    '''
    http://www.pythonchallenge.com/pc/def/0.html
    The hint is 2^38
    '''
    a = 2 ** 38
    challengeUrlOpen(str(a))

def createTranslationTable():
    '''
    http://www.pythonchallenge.com/pc/def/map.html
    The hint is:
    K -> M
    O -> E
    E -> G

    It means we have to translate each letter by letter + 2 using
    each letter ascii code
    '''
    import string
    all = string.lowercase
    first = ord(all[0])
    size = len(all)
    newAll = ''
    for s in all:
        code = ord(s)
        letter = chr(code)
        newCode = (code - first + 2) % size        
        newLetter = chr(newCode + first)
        newAll += newLetter
    table = string.maketrans(all, newAll)
    return table

def level1():
    encodedStr = \
''' g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''
    table = createTranslationTable()
    newStr = encodedStr.translate(table)
    print newStr
    challengeUrlOpen('map'.translate(table))

def getLastComment(url, serialize = False):
    import urllib
    fo = urllib.urlopen(url)
    text = fo.read()

    first = text.rfind('<!--')
    last = text.rfind('-->')

    mess = text[first+len('<!--\n'):last-1]

    if serialize:
	    from tempfile import mkstemp
	    import os
	    (fd, name) = mkstemp()
	    print name
	    fo = os.fdopen(fd, 'w')
	    fo.write(mess)
	    fo.close()

    return mess
 
def level2():
    '''
    http://www.pythonchallenge.com/pc/def/ocr.html

    recognize the characters. maybe they are in the book, 
    but MAYBE they are in the page source.

    You have to fetch the html page. Within it you have two comments, 
    the first is:
    find rare characters in the mess below:
    the second is a mess of character. Both are the last comment of the document
    '''
    urlBase = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    mess = getLastComment(urlBase)
    assert mess[0] == '%'
    assert mess[-1] == '*'

    import string
    url = ''
    for c in mess:
        if c in string.lowercase: url += c

    # rare characters (using the lowercase filter, or using a dict and counting occurences) 
    # form the word 'equality'
    challengeUrlOpen(url)

def level3():
    ''' 
    http://www.pythonchallenge.com/pc/def/equality.html'
    One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
    We still have to parse the last piece of data at the end 
    '''
    urlBase = 'http://www.pythonchallenge.com/pc/def/equality.html'
    mess = getLastComment(urlBase, True)
    import string
    Up = string.uppercase
    Low = string.lowercase
    candidates = []
    url = ''

    for c in range(len(mess)):
	    if c+7 >= len(mess): continue
	    i,j,k,L,m,n,o = mess[c:c+7]
	    
	    if i in Up and j in Up and k in Up and L in Low and m in Up and n in Up and o in Up:
		     candidates.append(c) 

    for c in candidates:
	    if mess[c-1] in Low and mess[c+7] in Low:
		    url += mess[c+3]
    challengeUrlOpen(url, True)

class foo(Exception): pass
def nextNothing(id):
    import webbrowser
    from urllib import urlencode, urlopen
    url = urlencode([('nothing', str(id))])
    fo = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?' + url)
    line = fo.read()
    last = line.split()[-1]
    if not last.isdigit():
	    print line
	    raise foo
    else:
	    return int(last)

def level4():
    '''
    http://www.pythonchallenge.com/pc/def/linkedlist.php
    if we click on the pictures, which is at linkedlist.php?nothing=12345", we get a 92512
    <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->

    After a while, the php print peak.html ...
    '''
    i = 12345
    while True:
	    try:
		    i = nextNothing(i)
	    except foo:
	            i /= 2 

def level5):
    '''
    http://www.pythonchallenge.com/pc/def/peak.html
    '''
 
level5()