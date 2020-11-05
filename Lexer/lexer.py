import sys

class Tag:
    "class tag to relate tag names with numbers for faster results with static variables representing each case"
    EOF = 65535
    SEMICOLON = 256
    DOT = 257
    PROGRAM = 258
    IDENTIFIER = 259
    OPARENTHESIS = 260
    CPARENTHESIS = 261
    CONSTANT = 262
    EQUALS = 263
    VAR = 264
    DOUBLEDOT = 265
    BEGIN = 266
    END = 267
    INTEGER = 268
    REAL = 269
    BOOLEAN = 270
    STRING = 271
    COMA = 272
    ASSIGN = 273
    WRITELN = 274
    NUMBER = 275
    READLN = 276
    WHILE = 277
    DO = 278
    REPEAT = 279
    UNTIL = 280
    FOR	= 281
    TO = 282
    DOWNTO = 283
    IF = 284
    THEN = 285
    ELSE = 286
    PLUS = 297
    MINUS = 288
    NOT	= 289
    NEQ = 290
    GE = 291
    GEQ = 292
    LE = 293
    LEQ = 294
    FALSE = 295
    TRUE = 296
    OR = 297
    MULT = 298
    DIV = 299
    MOD = 300
    AND = 301
    COMMMENTS = 303
    ERROR = 304

class Token:
    "class token gets the number id and returns string representation of the value"
    def __init__(self, tag=0):
        self.tag = tag

    def __str__(self):
        if self.tag == Tag.PROGRAM:
            return "PROGRAM"
        elif self.tag == Tag.CONSTANT:
            return "CONSTANT"
        elif self.tag == Tag.VAR:
            return "VAR"
        elif self.tag == Tag.BEGIN:
            return "BEGIN"
        elif self.tag == Tag.END:
            return "END"
        elif self.tag == Tag.INTEGER:
            return "INTEGER"
        elif self.tag == Tag.REAL:
            return "REAL"
        elif self.tag == Tag.BOOLEAN:
            return "BOOLEAN"
        elif self.tag == Tag.STRING:
            return "STRING"
        elif self.tag == Tag.WRITELN:
            return "WRITELN"
        elif self.tag == Tag.READLN:
            return "READLN"
        elif self.tag == Tag.WHILE:
            return "WHILE"
        elif self.tag == Tag.DO:
            return "DO"
        elif self.tag == Tag.REPEAT:
            return "REPEAT"
        elif self.tag == Tag.UNTIL:
            return "UNTIL"
        elif self.tag == Tag.FOR:
            return "FOR"
        elif self.tag == Tag.TO:
            return "TO"
        elif self.tag == Tag.DOWNTO:
            return "DOWNTO"
        elif self.tag == Tag.IF:
            return "IF"
        elif self.tag == Tag.THEN:
            return "THEN"
        elif self.tag == Tag.ELSE:
            return "ELSE"
        elif self.tag == Tag.NOT:
            return "NOT"
        elif self.tag == Tag.DIV:
            return "DIV"
        elif self.tag == Tag.MOD:
            return "MOD"
        elif self.tag == Tag.AND:
            return "AND";
        elif self.tag == Tag.OR:
            return "OR"
        elif self.tag == Tag.EQUALS:
            return "=="
        elif self.tag == Tag.NEQ:
            return "<>"
        elif self.tag == Tag.LE:
            return "<="
        elif self.tag == Tag.GE:
            return ">="
        elif self.tag == Tag.MINUS:
            return "-"
        elif self.tag == Tag.ASSIGN:
            return ":="
        elif self.tag == Tag.IDENTIFIER:
            return "ID"
        elif self.tag == Tag.EOF:
            return "EOF"
        elif self.tag == Tag.COMMMENTS:
            return "TOKEN - VALUE = COMMMENTS"
        else:
            return "TOKEN - VALUE = "+ str(self.tag)
    def rvalue(self):
        if self.tag == Tag.PROGRAM:
            return "program"
        elif self.tag == Tag.CONSTANT:
            return "constant"
        elif self.tag == Tag.VAR:
            return "var"
        elif self.tag == Tag.BEGIN:
            return "begin"
        elif self.tag == Tag.END:
            return "end"
        elif self.tag == Tag.INTEGER:
            return "integer"
        elif self.tag == Tag.REAL:
            return "number"
        elif self.tag == Tag.BOOLEAN:
            return "boolean"
        elif self.tag == Tag.STRING:
            return "string"
        elif self.tag == Tag.WRITELN:
            return "writeln"
        elif self.tag == Tag.READLN:
            return "readln"
        elif self.tag == Tag.WHILE:
            return "while"
        elif self.tag == Tag.DO:
            return "do"
        elif self.tag == Tag.REPEAT:
            return "repeat"
        elif self.tag == Tag.UNTIL:
            return "until"
        elif self.tag == Tag.FOR:
            return "for"
        elif self.tag == Tag.TO:
            return "to"
        elif self.tag == Tag.DOWNTO:
            return "downto"
        elif self.tag == Tag.IF:
            return "if"
        elif self.tag == Tag.THEN:
            return "then"
        elif self.tag == Tag.ELSE:
            return "else"
        elif self.tag == Tag.NOT:
            return "not"
        elif self.tag == Tag.DIV:
            return "DIV"
        elif self.tag == Tag.MOD:
            return "mod"
        elif self.tag == Tag.AND:
            return "and";
        elif self.tag == Tag.OR:
            return "or"
        elif self.tag == Tag.EQ:
            return "="
        elif self.tag == Tag.NEQ:
            return "<>"
        elif self.tag == Tag.LE:
            return "<="
        elif self.tag == Tag.GE:
            return ">="
        elif self.tag == Tag.MINUS:
            return "-"
        elif self.tag == Tag.ASSIGN:
            return ":="
        elif self.tag == Tag.ID:
            return "identifier"
        elif self.tag == Tag.EOF:
            return "$"
        elif self.tag == Tag.CHARACTERSTRING:
            return "string"
        elif self.tag == Tag.COMMMENTS:
            return "TOKEN - VALUE = COMMMENTS"
        else:
            return str(self.tag)

class Word(Token):
    "For storing reserved words, returning its lexeme in string representation"
    def __init__(self, lexeme, tag):
        self.tag = tag
        self.lexeme = lexeme
    def __str__(self):
        return "WORD - LEXEME = " + self.lexeme

eq = Word("==", Tag.EQUALS)
ne = Word("<>", Tag.NEQ)
le = Word("<=", Tag.LEQ  )
ge = Word(">=", Tag.GEQ )
minus = Word("minus", Tag.MINUS )
assing = Word(":=", Tag.ASSIGN )
true = Word("true",  Tag.TRUE  )
false = Word("false", Tag.FALSE )

class Real(Token):
    "Data type Real for storing real numbers, this includes numbers with floating point"
    def __init__(self, value):
        self.tag = Tag.REAL
        self.value = value
    def __str__(self):
        return "REAL - VALUE = " + str(self.value)

class Integer(Token):
    "Data type Integer for storing integer values"
    def __init__(self, value):
        self.tag = Tag.INTEGER
        self.value = value
    def __str__(self):
        return "INTEGER - VALUE = " + str(self.value)

class CharacterString(Token):
    "Data type CharacterString for storing string values"
    def __init__(self, value):
        self.tag = Tag.STRING
        self.value = value
    def __str__(self):
        return "STRING - VALUE = " + self.value

class Lexer:
    "Proccesing class that opens input and reads char by char"
    def __init__(self, filename):
        self.input = open(filename, "r")
        self.reading = True
        self.peek = ''
        self.words = {}
        self.lineNumber = 0

    def reserve(self, w):
        self.words[w.lexeme] = w

    def isReserved(self, t):
        return (t in self.words)

    def readch(self):
        self.peek = self.input.read(1)
        if self.peek:
            #print("scanned "+str(self.peek))
            return self.peek
        self.reading = False
        return self.peek

    def bolReadch(self, c):
        self.readch()
        if self.peek == c:
            return True
        return False

    def start(self):
        self.reserve(Word("program", Tag.PROGRAM))
        self.reserve(Word("constant", Tag.CONSTANT) )
        self.reserve(Word("var", Tag.VAR) )
        self.reserve(Word("begin", Tag.BEGIN) )
        self.reserve(Word("end", Tag.END) )
        self.reserve(Word("integer", Tag.INTEGER) )
        self.reserve(Word("real", Tag.REAL) )
        self.reserve(Word("boolean", Tag.BOOLEAN) )
        self.reserve(Word("string", Tag.STRING) )
        self.reserve(Word("writeln", Tag.WRITELN) )
        self.reserve(Word("readln", Tag.READLN) )
        self.reserve(Word("while", Tag.WHILE) )
        self.reserve(Word("do", Tag.DO) )
        self.reserve(Word("repeat", Tag.REPEAT) )
        self.reserve(Word("until", Tag.UNTIL) )
        self.reserve(Word("for", Tag.FOR) )
        self.reserve(Word("to", Tag.TO) )
        self.reserve(Word("downto", Tag.DOWNTO) )
        self.reserve(Word("if", Tag.IF) )
        self.reserve(Word("then", Tag.THEN) )
        self.reserve(Word("else", Tag.ELSE) )
        self.reserve(Word("not", Tag.NOT) )
        self.reserve(Word("div", Tag.DIV) )
        self.reserve(Word("mod", Tag.MOD) )
        self.reserve(Word("and", Tag.AND) )
        self.reserve(Word("or", Tag.OR) )

    def skipWhiteSpaces(self):
        while self.peek == " " or self.peek == "\t" or self.peek == "\n":
            if self.peek == "\n":
                self.lineNumber = self.lineNumber + 1
            self.readch()

    def readCharacterString(self):
        cs = ""+self.peek
        self.readch()
        while self.peek != '"' and self.reading:
            cs = cs + self.peek
            self.readch()
        cs = cs + self.peek
        self.readch()
        return CharacterString(cs)

    def readComments(self):
        prev = self.peek
        self.readch()
        while self.reading:
            if prev == '*' and self.peek == ')':
                self.readch()
                break
            prev = self.peek
            self.readch()
        return Token(Tag.COMMMENTS);

    def scan(self):
        self.skipWhiteSpaces()
        if self.peek == '(':
            self.readch()
            if self.peek =='*':
                return self.readComments()
            return Token('(')
        elif self.peek == '<':
            self.readch()
            if self.peek == '=':
                lex.readch()
                return le
            elif self.peek == '>':
                lex.readch()
                return ne
            else:
                return Token('<')
        elif self.peek == '>':
            self.readch()
            if self.peek == '=':
                lex.readch()
                return le
            elif self.peek == '>':
                lex.readch()
                return ne
            else:
                return Token('<')
        elif self.peek == '=':
            self.readch()
            if self.peek == '=':
                lex.readch()
                return eq
            else:
                return Token('=')
        elif self.peek == ':':
            self.readch()
            if self.peek == '=':
                lex.readch()
                return assing
            else:
                return Token(':')
        elif self.peek == '"':
            return self.readCharacterString()

        elif self.peek.isdigit():
            real = False
            st = ""+self.peek
            self.readch()
            while self.reading and (self.peek.isdigit() or self.peek == '.'):
                if self.peek == '.':
                    real = True
                st = st + self.peek
                self.readch()
            if real:
                return Real(float(st))
            return Integer(int(st))

        elif self.peek.isalpha():
            st = ""+self.peek
            self.readch()
            while self.reading and (self.peek.isalpha() or self.peek.isdigit()):
                st = st + self.peek
                self.readch()
            st = st.lower()
            if st in self.words:
                return self.words[st]#Word(st, Tag.ID)
            w = Word(st, Tag.IDENTIFIER)
            self.reserve(w)
            return w

        else:
            if self.peek == '':
                return Token(65535)
            tok = Token(self.peek)
            self.readch()
            return tok



if len(sys.argv) != 2:
    print("usage: lexer.py inputfile")
else:
    lex = Lexer(sys.argv[1])
    lex.start()
    lex.readch()
    token = lex.scan()
    while lex.reading:
        print("" + str(token))
        token = lex.scan()
    print("" + str(token))
    lex.input.close()
