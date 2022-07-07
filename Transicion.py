from Estado import Estado
import Caracteres_Especiales as C_E

class Transicion:
  
#Constructor
    
    def __init__(self,simbolo1=None,simbolo2=None, estado=None):
        if simbolo1 != None and  simbolo2 != None:
            self.simbInf = simbolo1
            self.simbSup = simbolo2
            self.edoAcep = estado
        elif simbolo1 != None and simbolo2== None:
            self.simbInf = simbolo1
            self.simbSup = simbolo1
            self.edoAcep = estado

#getters
    def getSimboloInf(self):
        return self.simboloInf
    def getSimboloSup(self):
        return self.simboloSup
    def getEstado(self, simb):
       if simb>=self.simbInf and simb<=self.simbSup:
           return self.edoAcep
       return None

#setters
    def setTransicion(self,simbolo,estado):
        self=Transicion(simbolo,estado)
    def setTransicion(self,simbolo1,simbolo2,estado):
        self=Transicion(self,simbolo1,simbolo2,estado)
    def setSimboloInf(self,nSimb):
        self.simboloInf=nSimb
    def setSimboloSup(self,nSimb):
        self.simboloSup=nSimb

    def __str__(self):
        if(self.simbSup == self.simbInf):
             return str(self.simbInf)
        else:
            return str(self.simbInf + ' ' + self.simbSup)
          
