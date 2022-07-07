from AFD import AFD
from AFN import AFN
from AnaLex import AnaLex

class ER_AFN:

    def __init__(self,AnaLex):
        self.L=AnaLex
        self.result=None


    def IniConversion(self):
        automata=AFN()
        f=(False,automata)
        f=self.E(f)
        if f[0]:
            token=self.L.getToken()
            self.result=f[1]
            return True
        return False
    
    def E(self, f):
        f=self.T(f)
        if f[0]:
            f=self.Ep(f)
            if f[0] :
                return (True,f[1])
        return (False,f[1])
        
    def Ep(self,f):
        automata2=AFN()
        f2=(False,automata2)

        token=self.L.getToken()
        if token==10:#OR
            f2 = self.T(f2)
            if f2[0]:
                f[1].unir_Automata(f2[1])
                f=self.Ep(f)
                if f[0]:
                    return (True,f[1])
            return (False,f[1])

        self.L.returnToken()
        return (True,f[1])

    def T(self,f):
        f=self.C(f)
        if f[0]:
            f=self.Tp(f)
            if f[0]:
                return (True,f[1])
        return (False,f[1])
    
    def Tp(self,f):
        automata2=AFN()
        f2=(False,automata2)
        token=self.L.getToken()
        
        if token==20:#Amperson
            f2=self.C(f2)
            if f2[0]:
                f[1].concatenar_Automata(f2[1])
                f=self.Tp(f)
                if f[0]:
                    return (True,f[1])
            return (False,f[1])
        self.L.returnToken()
        return (True,f[1])

    def C(self,f):
        f=self.F(f)
        if f[0]:
            f=self.Cp(f)
            if f[0]:
                return (True,f[1])
        return (False,f[1])
    
    def Cp(self, f):
        token=self.L.getToken()

        if token==30: #Cerradura Transitiva
            f[1].cerradura_transitiva()
            f = self.Cp(f)
            if f[0]:
                return (True,f[1])
            return (False,f[0])

        elif token==40: #cerradura Kleen
            f[1].cerradura_Kleen()
            f = self.Cp(f)
            if f[0]:
                return (True,f[1])
            return (False,f[0])

        elif token==50: #opcional
            f[1].opcional()
            f = self.Cp(f)
            if f[0]:
                return (True,f[1])
            return (False,f[0])

        self.L.returnToken()
        return (True, f[1])

    def F(self,f):
        token=self.L.getToken()

        if token==60: #Par_izq

            f=self.E(f)
            if f[0]:
               token=self.L.getToken()
               if token==70: #Par_Der
                    return (True, f[1])
            return (False, f[1])

        elif token==80:#Corvh_Izq
            
            token=self.L.getToken()
            
            if token==110: #simbolo

                if self.L.lexem[0]== "\\":simbolo1= self.Lexema[1]
                else:simbolo1=self.L.lexem[0]
               
                token=self.L.getToken()

                if token== 100: #guion
                    
                    token=self.L.getToken()
                    
                    if token==110: #Simbolo

                        if self.L.lexem[0]== "\\": simbolo2 = self.L.lexem[1]
                        else: simbolo2=self.L.lexem[0]

                        token=self.L.getToken()
                        
                        if token==90: #corchete derecho
                            af=AFN()
                            af.crear_AFN_Basico(simbolo1,simbolo2)
                            return (True,af)

            return (False,f[1])

        elif token==110: #simbolo
                if self.L.lexem[0]== "\\":simbolo1= self.L.lexem[1]
                else:simbolo1=self.L.lexem[0]
              
                #af=AFN()
                f[1].crear_AFN_Basico(simbolo1)
                return (True,f[1])

        return (False ,f[1])       