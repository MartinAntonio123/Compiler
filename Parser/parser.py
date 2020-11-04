import sys
import lexer

class Parser:
    "Class to check gramar of the input and returns accepted or not"
    def __init__(self, filename):
        self.lexer = lexer.Lexer(filename)
        self.pila = []
        self.pilaEstados = [0]
        self.inputstring = []
        self.tabla = {}
        self.fillAction("table2.csv")
        self.manualInputString()
        #self.fillInputString()

    def fillAction(self, table):
        arr = []
        file = open(table, 'r')
        Lines = file.readlines()
        mystate = 1
        keys = []
        vals = []
        for line in Lines:
            line = line.strip()
            line = str(line)
            if mystate == 1:
                keys = line.split(",")
                mystate = 2
            elif mystate == 2:
                x = line.split(",")
                for value in x:
                    vals.append([value])
                mystate = 3
            elif mystate == 3:
                x = line.split(",")
                for i in range(len(x)):
                    vals[i].append(x[i])
        for i in range(len(keys)):
            #print(i+1)
            #print(len(vals[i]))
            self.tabla[keys[i]] = vals[i]
        file.close()

    def manualInputString(self):
        self.inputstring = ['id','+','id','+','(','$']

    def fillInputString(self):
        self.lexer.start()
        self.lexer.readch()
        token = self.lexer.scan()
        self.inputstring.append(token)
        while self.lexer.reading:
            print("" + str(token))
            token = self.lexer.scan()
            self.inputstring.append(token)
        self.lexer.input.close()

    def analize(self):
        maxsteps = 0
        while maxsteps < 50:
            maxsteps = maxsteps + 1
            state = self.pilaEstados[-1]
            entrada = self.inputstring[0]
            action = self.tabla[entrada][state]
            print(self.pilaEstados)
            print(self.inputstring)
            print(self.pila)
            print(action)
            if action == '':
                print("ERROR ")
                sys.exit()
            elif action == 'acc':
                print("accepted")
                sys.exit()
            elif action[0] == 's':
                print("shift")
                action = action.replace('s', '')
                action = int(action)
                self.pilaEstados.append(action)
                self.pila.append(entrada)
                self.inputstring.pop(0)
            elif action[0] == 'r':
                print("shift")
                action = action.replace('r', '')
                action = int(action)
                file = open('gramar2.txt', 'r')
                lines = file.readlines()
                file.close()
                count = 0
                reduce = ''
                for line in lines:
                    if count == action:
                        reduce = line
                        print(line)
                    count = count + 1
                reduce = reduce.strip()
                reduce = reduce.split(' ')#no se
                print(reduce)
                while reduce[-1] != '->':
                    self.pilaEstados.pop()
                    if reduce.pop() != self.pila.pop():
                        print("ERROR ")
                        sys.exit()
                reduce.pop()
                self.pila.append(reduce.pop())
                self.pilaEstados.append(int(self.tabla[self.pila[-1]][self.pilaEstados[-1]]))








if len(sys.argv) != 2:
    print("usage: parser.py inputfile")
else:
    parser = Parser(sys.argv[1])
    parser.analize()
