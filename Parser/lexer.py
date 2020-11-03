#import sys
class Tag:
    "class tag to relate tag names with numbers for faster results with static variables representing each case"
    EOF = 65535
    NUMBER = 290
    ID = 291
    ERROR = 293

class Token:
    "class token gets the number id and returns string representation of the value"
    def __init__(self, tag=0):
        self.tag = tag

    def __str__(self):
        if self.tag == Tag.EOF:
            return "TOKEN, symbol = EOF"
        else:
            return "TOKEN, symbol = "+ chr(self.tag)

class Word(Token):
    "For storing reserved words, returning its lexeme in string representation"
    def __init__(self, lexeme, tag):
        self.tag = tag
        self.lexeme = lexeme
    def __str__(self):
        return "WORD, lexeme = " + self.lexeme

class Number(Token):
    "Data type Real for storing real numbers, this includes numbers with floating point"
    def __init__(self, value):
        self.tag = Tag.NUMBER
        self.value = value
    def __str__(self):
        return "NUMBER, value = " + str(self.value)

class Lexer:
    "Proccesing class that opens input and reads char by char"
    def __init__(self, filename):
        self.input = open(filename, "r")
        self.reading = True
        self.lastr = True
        self.peek = ''
        self.words = {}
        self.lineNumber = 1

    def readch(self):
        self.peek = self.input.read(1)
        if self.peek:
            return self.peek
        self.reading = False
        return self.peek

    def skipWhiteSpaces(self):
        while self.peek == " " or self.peek == "\t" or self.peek == "\n":
            if self.peek == '\n':
                self.lineNumber = self.lineNumber + 1
            self.readch()

    def scan2(self):
        mytoken = self.scan()
        print(mytoken)
        return mytoken


    def scan(self):
        self.skipWhiteSpaces()

        if self.peek.isdigit():
            st = ""+self.peek
            self.readch()
            while self.reading and (self.peek.isdigit() or self.peek == '.'):
                st = st + self.peek
                self.readch()
            return Number(float(st))

        elif self.peek.isalpha():
            st = ""+self.peek
            self.readch()
            while self.reading and (self.peek.isalpha() or self.peek.isdigit()):
                st = st + self.peek
                self.readch()
            st = st.lower()
            if st in self.words:
                return self.words[st]#Word(st, Tag.ID)
            w = Word(st, Tag.ID)
            self.words[st] = w
            return w

        else:
            if self.peek == '':
                return Token(65535)
            tok = Token(ord(self.peek))
            self.readch()
            return tok

#if len(sys.argv) != 2:
#    print("usage: lexer.py inputfile")
#else:
#    lex = Lexer(sys.argv[1])
#    lex.readch()
#    token = lex.scan()
#    while lex.reading:
#        print(token)
#        token = lex.scan()
#    print(token)
#    print(lex.words)
#    lex.input.close()
