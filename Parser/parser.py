import sys
import lexer

class Parser:
    "Class to check gramar of the input and returns accepted or not"
    def __init__(self, filename):
        self.lexer = lexer.Lexer(filename)
        self.lexer.readch()

    def check(self, tag):
        if self.token.tag == tag:
            self.token = self.lexer.scan2()
        else:
            print("ERROR line"+str(self.lexer.lineNumber))
            sys.exit()

    def analyze(self):
        self.token = self.lexer.scan2()
        self.E()
        print("ACCEPTED")

    def E(self):
        self.T()
        self.EPrime()

    def T(self):
        self.F()
        self.TPrime()

    def EPrime(self):
        if self.token.tag == ord('+'):
            self.check(ord('+'))
            self.T()
            self.EPrime()
        elif self.token.tag == ord('-'):
            self.check(ord('-'))
            self.T()
            self.EPrime()
        else:
            pass

    def F(self):
        if self.token.tag == lexer.Tag.NUMBER:
            self.check(lexer.Tag.NUMBER)
        elif self.token.tag == lexer.Tag.ID:
            self.check(lexer.Tag.ID)
        elif self.token.tag == ord('('):
            self.check(ord('('))
            self.E()
            self.check(ord(')'))
        else:
            print("ERROR line "+str(self.lexer.lineNumber))
            sys.exit()

    def TPrime(self):
        if self.token.tag == (ord('*')):
            self.check(ord('*'))
            self.F()
            self.TPrime()
        elif self.token.tag == (ord('/')):
            self.check(ord('/'))
            self.T()
            self.EPrime()

if len(sys.argv) != 2:
    print("usage: parser.py inputfile")
else:
    pars = Parser(sys.argv[1])
    pars.analyze()
    #print(pars.lexer.words)
    #print("n lineas = "+ str(pars.lexer.lineNumber))
