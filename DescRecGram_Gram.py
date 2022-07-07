from AnaLex import AnaLex
from Node import Node
from TokemGram_Gram import TokenGram_Gram

class DescRecGram_Gram:
    
    def __init__(self,afd,sigma):
        self.L=AnaLex(afd,sigma)
        self.arrReglas=[]
      
    def AnalizarGramatica(self):
        if(self.G()):
            return True
        return False
   
    def G(self):
        if self.ListasReglas():
            return True
        return False 

    def ListasReglas(self):
        if(self.Reglas()):
            token=self.L.getToken()
            if token==TokenGram_Gram.PC:
                if self.ListasReglasP():
                    return True
        return False

    def ListasReglasP(self):
        status=self.L.getStatus()

        if self.Reglas():
            token=self.L.getToken()
            if token==TokenGram_Gram.PC:
                if(self.ListasReglasP()):
                    return True
            return False
        self.L.setStatus(status)
        return True
  
    def Reglas(self):
        f=(False,None)
        f= self.LadoIzquierdo(f)
        if f[0]:
            token=self.L.getToken()
            if token==TokenGram_Gram.FLECHA:
                f=self.LadosDerechos(f)
                if f[0]:
                    return True
        return False

    def LadoIzquierdo(self,f):
        token=self.L.getToken()

        if token==TokenGram_Gram.SIMBOLO:
            return (True,self.L.getLexem())

        return (False,f[1])
    
    def LadosDerechos(self,f):
        N=(False,None)
        N=self.SecSimbolos(N)

        if N[0]:
            self.arrReglas.append(Node(f[1],N[1]))
            f=self.LadosDerechosP(f)

            if f[0]:
                return (True,f[1])

        return (False,f[1])
    
    def LadosDerechosP(self,f):
        token=self.L.getToken()

        if token==TokenGram_Gram.OR:
          
            N=(False,None)
            N=self.SecSimbolos(N)

            if N[0]:
                self.arrReglas.append(Node(f[1],N[1]))
                f=self.LadosDerechosP(f)
                
                if f[0]:
                    return (True,f[1])
            return (False,f[1])

        self.L.returnToken()
        return (True,f[1])
    

    def SecSimbolos(self,N):
        token=self.L.getToken()

        if token == TokenGram_Gram.SIMBOLO:
            N=(N[0],Node(self.L.getLexem(),None))
            
            N2 = (False, None)
            N2=self.SecSimbolosP(N2)

            if N2[0]:
                N[1].setNext(N2[1])
                return (True,N[1])
      
        return (False,N[1])

    def SecSimbolosP(self,N):
       
        token=self.L.getToken()

        if token == TokenGram_Gram.SIMBOLO:
            N=(N[0],Node(self.L.getLexem(),None))

            N2 = (False, None)
            N2=self.SecSimbolosP(N2)

            if(N2[0]):
                N[1].setNext(N2[1])
                return (True, N[1])

            return (False, N[1])
        
        self.L.returnToken()
        return (True, None)