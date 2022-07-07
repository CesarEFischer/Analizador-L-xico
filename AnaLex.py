from AFD import AFD
import Caracteres_Especiales as C_E
from AnaLexStatus import AnaLexStatus

finalCadena='\0'

class AnaLex:

    def __init__(self,automata,cadena):
        self.alfabeto=automata.alfabeto
        self.tabla=automata.tabla
        self.string=cadena+finalCadena
        self.simbPosA= 0
        self.edoAcept=False
        self.EdoActual=0
        self.token=-1
        self.lexem=""
        self.pila=[]
        self.inPosLex=0
        self.tePosLex=0
    
    def getToken(self):
        self.yylex()
        return self.token

    def getLexem(self):
        return self.lexem

    def getListaLexems(self):
        lexem = []
        res = self.yylex()
        print(self.lexem)

        while(res != C_E.END):
            lexem.append( (self.token,self.lexem) )
            res = self.yylex()
        
        self.validar_cadena(lexem)
        return lexem

    def returnToken(self):
        self.simbPosA = self.pila.pop()
    
    def getStatus(self):
        return AnaLexStatus(self.simbPosA, self.edoAcept, 
        self.EdoActual, self.inPosLex, self.tePosLex, self.pila.copy(), self.token, self.lexem)
        
    
    def setStatus(self,s):
        self.simbPosA = s.getActualSymbolPos()
        self.edoAcept = s.getReachedAccept()
        self.EdoActual = s.getActualState()
        self.inPosLex = s.getBeginLexPos()
        self.tePosLex = s.getEndLexPos()
        self.pila =  s.getStack()
        self.token = s.getToken()
        self.lexem = s.getLexem()
    
    def setSigma(self,sigma):
        a=AFD(self.tabla,self.alfabeto)
        return AnaLex(a,sigma)
    
    
    def validar_cadena(self,lexem):
        for lex in lexem:
            if lex[0]!=C_E.ERROR: self.edoAcept=True
            else: 
                self.edoAcept=False
                return

    def yylex(self):
        self.EdoActual = 0
        self.edoAcept = False

        if self.string[self.simbPosA]==finalCadena:
            self.token=C_E.END
            return self.token

        self.pila.append(self.simbPosA)
        self.inPosLex=self.simbPosA

        while self.string[self.simbPosA] != finalCadena:
            charActual=self.string[self.simbPosA]
            indexAlf=-1
          
            if charActual in self.alfabeto:
                indexAlf=self.alfabeto.index(charActual)+1
               
            if indexAlf==-1:
                if self.edoAcept==False:
                    self.lexem= self.string[self.simbPosA:self.simbPosA+1]
                    self.simbPosA = self.inPosLex+1
                    self.token = C_E.ERROR
                    return C_E.ERROR
                
                self.lexem =self.string[self.inPosLex:self.tePosLex+1]
                self.simbPosA=self.tePosLex+1
                return self.token
            
            self.EdoActual = self.tabla[self.EdoActual][indexAlf]
          
            if self.EdoActual!=-1:
                if self.tabla[self.EdoActual][len(self.tabla[self.EdoActual])-1]!=-1:
                    self.token =self.tabla[self.EdoActual][len(self.tabla[self.EdoActual])-1]
                    self.edoAcept=True
                self.tePosLex=self.simbPosA
                self.simbPosA+=1
                self.lexem= self.string[self.inPosLex:self.tePosLex+1]
      
            else:
                if self.edoAcept==False:
                    self.lexem = self.string[self.simbPosA:self.simbPosA+1]
                    self.simbPosA= self.inPosLex+1
                    self.token= C_E.ERROR
                    return self.token

                self.lexem = self.string[self.inPosLex:self.tePosLex+1]
                self.simbPosA = self.tePosLex+1

                return self.token

