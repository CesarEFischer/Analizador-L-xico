class Estado:
    __contador = 0
    
    def  __init__(self):
        self.__class__.__contador+=1
        self.idEstado =  self.__class__.__contador
        self.edoAcep = False
        self.token = -1
        self.trans = []
    
#getters
    def getIdEstado(self):
         return self.idEstado
    def getEdoAcep(self):
        return self.edoAcep
    def getToken(self):
        return self.token
    def getTrans(self):
        return self.trans

#setters
    def setIdEstado(self, nIdEstado):
        self.idEstado=nIdEstado
    def setEdoAcept(self,nEdoAcep):
        self.edoAcep=nEdoAcep
    def setToken(self,nToken):
        self.token=nToken
    def setTrans(self,nTrans):
        self.trans=nTrans

    def __str__(self):
        return str(self.idEstado)