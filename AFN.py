from Estado import Estado
from Transicion import Transicion
from AFD import AFD
from AnaLex import AnaLex
import Caracteres_Especiales as C_E

idAFN=0
class AFN:

    def __init__(self):
        global idAFN
        idAFN+=1
        self.idAFN=idAFN
        self.edoInicial=None
        self.edosAFN=[]
        self.edosAcept=[]
        self.alfabeto=[]
        self.seAgregoAFNUnionLexico= False
        self.isAFD=False
    
    #Setter
    def cambiar_id(self, nID):
        self.idAFN = nID

    def listar_estados(self, lista, estados):
        for e in estados:
            lista.append(e)

    #Operaciones Basicas de un AFN
    def crear_AFN_Basico(self,simbolo1,simbolo2=None):

        edo1 = Estado()
        edo2 = Estado()

        
        if(simbolo2==None or simbolo1==simbolo2):#Verificamos si es de un solo simbolo
            trans = Transicion(simbolo1,estado=edo2)
            self.alfabeto.append(simbolo1)
        else:
            #verificamos que el simbolo 1 no sea el mayor
            if ord(simbolo1)>ord(simbolo2):
                aux=simbolo1
                simbolo1=simbolo2  
                simbolo2=aux

            trans = Transicion(simbolo1,simbolo2,edo2)

            for i in range(ord(simbolo1),ord(simbolo2)+1):
                self.alfabeto.append(chr(i))

        edo1.trans.append(trans)#agregamos las transiciones

        self.edoInicial=edo1 #incicamos su estado inicial
        self.edosAFN.append(edo1)

        edo2.edoAcep = True #lo volvemos estado de aceptacion
        self.edosAcept.append(edo2)
        self.seAgregoAFNUnionLexico = False
    
        return self

    def unir_Automata(self,a2):
        
        e1=Estado()
        e2=Estado()
        e1.trans.append(Transicion(C_E.epsilon,estado=self.edoInicial))#agregamos su transicion con a1
        e1.trans.append(Transicion(C_E.epsilon,estado=a2.edoInicial))#agregamos su transicion con 2
        
        aux=[]

        '''Le quitamos todos los estados de aceptación al automata 1
        y creamos las transiciones al nuevo estado final e2'''
        for e in self.edosAcept:
            e.trans.append(Transicion(C_E.epsilon, estado=e2)) #agregamos la nueva transicion
            e.edoAcep=False #le quita el estado de aceptacion
            self.edosAFN.append(e) #lo agregamos como un estado

        '''Le quitamos todos los estados de aceptación al automata 2
        y creamos las transiciones al nuevo estado final e2'''
        for e in a2.edosAcept:
            e.trans.append(Transicion(C_E.epsilon, estado=e2))#agregamos la nueva transicion
            e.edoAcep=False #le quita el estado de aceptacion
            a2.edosAFN.append(e) #lo agregamos como un estado
     
        #Quitamos los estados de aceptacion de los conjuntos
        self.edosAcept.clear()
        a2.edosAcept.clear()
        
        #Creamos una  copia para que se tenga en orden los estados
        for e in self.edosAFN:
            aux.append(e)
            
        self.edosAFN.clear() # borramos sus estados 
        self.edoInicial=e1 #Indicamos su estado inicial

        #agregamos los estados
        self.edosAFN.append(e1)
        self.listar_estados(self.edosAFN,aux)
        self.listar_estados(self.edosAFN,a2.edosAFN)
        
        e2.edoAcep=True #Indicamos que es el nuevo estado de aceptacion
        self.edosAcept.append(e2)#lo agregamos a la lista de edoAcep

        if self.alfabeto not in a2.alfabeto:
            self.alfabeto.extend(a2.alfabeto)
        
        return self

    def concatenar_Automata(self,a2):

        for t in a2.edoInicial.trans:#obtenemos la transicion del a2
            for e in self.edosAcept:
                e.edoAcep=False
                e.trans.append(t) 
                if e not in self.edosAFN:
                    self.edosAFN.append(e)


        a2.edosAFN.remove(a2.edoInicial) #Eliminamos el estado inicial de a2     
        self.edosAcept=a2.edosAcept#actulizamos el estado de aceptacion
        self.listar_estados(self.edosAFN,a2.edosAFN) #agrupamos los estados
        self.alfabeto.extend(a2.alfabeto)

        return self

    def cerradura_transitiva(self):
        aux=[]
        #Estado 1
        e1=Estado()
        e1.trans.append(Transicion(C_E.epsilon, estado=self.edoInicial))

        #Estado 2
        e2=Estado()
        e2.edoAcep=True

        for e in self.edosAcept:
            e.trans.append(Transicion(C_E.epsilon,estado=self.edoInicial)) #enlazamos el estado final con el estado inicial
            e.trans.append(Transicion(C_E.epsilon,estado=e2)) #enlazamos el estado final con el nuevo edoAcep 
            e.edoAcep=False
            self.edosAFN.append(e)

        
        for e in self.edosAFN: #Copiamos todos los estados
            aux.append(e)

        self.edoInicial=e1 #incicamos el nuevo estado inicial
        self.edosAcept.clear()
        self.edosAcept.append(e2) #incicamos el nuevo estado final
        self.edosAFN.clear()# borramos los datos
        #Cargamos los estados acomodados

        self.edosAFN.append(e1)
        self.listar_estados(self.edosAFN,aux)
   
        return self

    def cerradura_Kleen(self):
        aux=[]
        #Estado 1
        e1=Estado()
        e1.trans.append(Transicion(C_E.epsilon, estado=self.edoInicial))
        
        #Estado 2
        e2=Estado()
        e2.edoAcep=True

        for e in self.edosAcept:
            e.edoAcep=False
            e.trans.append(Transicion(C_E.epsilon,estado=self.edoInicial)) #enlazamos el estado final con el estado inicial
            e.trans.append(Transicion(C_E.epsilon,estado=e2)) #enlazamos el estado final con el nuevo edoAcep 
            self.edosAFN.append(e)
        
        for e in self.edosAFN: #Copiamos todos los estados
            aux.append(e)
      
        self.edoInicial=e1 #incicamos el nuevo estado inicial
        self.edosAcept.clear()# borramos los datos
        self.edosAcept.append(e2) #incicamos el nuevo estado final
        e1.trans.append(Transicion(C_E.epsilon,estado=e2))#conectamos el nuevo estado inicial con el final

        self.edosAFN.clear()# borramos los datos

        #Cargamos los estados acomodados
        self.edosAFN.append(e1)
        self.listar_estados(self.edosAFN,aux)
        
        return self

    def opcional(self):
        aux=[]
        #Estado 1
        e1=Estado()
        e1.trans.append(Transicion(C_E.epsilon, estado=self.edoInicial))

        #Estado 2
        e2=Estado()
        e2.edoAcep=True

        for e in self.edosAcept:
            e.trans.append(Transicion(C_E.epsilon,estado=e2)) #enlazamos el estado final con el nuevo edoAcep 
            e.edoAcep=False
            self.edosAFN.append(e)

        
        for e in self.edosAFN: #Copiamos todos los estados
            e.setIdEstado(e.idEstado+1)
            aux.append(e)

        self.edoInicial=e1 #incicamos el nuevo estado inicial
        self.edosAcept.clear()
        self.edosAcept.append(e2) #incicamos el nuevo estado final
        self.edosAFN.clear()# borramos los datos

        #Cargamos los estados acomodados
        self.edosAFN.append(e1)
        self.listar_estados(self.edosAFN,aux)
       
        return self
    
    def union_especial(self,a, token):

        for edo in a.edosAcept:
                edo.token=token
                self.edosAcept.append(edo)

        if self.seAgregoAFNUnionLexico==False:
            e = Estado()
            e.trans.append(Transicion(C_E.epsilon,estado=a.edoInicial))
            self.edoInicial = e
            self.seAgregoAFNUnionLexico = True
        else:
            self.edoInicial.trans.append(Transicion(C_E.epsilon,estado = a.edoInicial))
        
        for c in a.alfabeto:
            if c not in self.alfabeto:
                self.alfabeto.append(c)

    def cerradura_e(self, estado):
        conjEstados=[]
        pila = []
        pila.append(estado) 

        while len(pila)!=0: #la pila no este vacia
            aux=pila.pop()
            conjEstados.append(aux)
            for t in aux.trans:
                edo = t.getEstado(C_E.epsilon)# si no tiene transcisiones epsilon
                if edo != None:
                    if edo not in pila: # si no esta en la pila
                        pila.append(edo)
        
        return conjEstados
    
    def cerradura_e1(self, estados):
        conjEstados=[]
        pila = []

        for e in estados:
            pila.append(e)

        while len(pila)!=0: #la pila no este vacia

            aux=pila.pop()
            if aux not in conjEstados:
                conjEstados.append(aux)

            for t in aux.trans:
                edo = t.getEstado(C_E.epsilon)# si no tiene transcisiones epsilon
                if edo != None:
                    if edo not in pila: # si no esta en la pila
                        pila.append(edo)
           
        return conjEstados

    def mover(self, estado, simbolo):
        conjEdos=[]

        if estado==None:
            return conjEdos

        for t in estado.trans:
            aux =t.getEstado(simbolo)
            if aux!=None:
                conjEdos.append(aux)

        return conjEdos

    def mover1(slef,estados, simbolo):
        conjEdos=[]

        for e in estados:
            for t in e.trans:
                aux = t.getEstado(simbolo)
                if aux!=None:
                    if aux not in conjEdos:
                        conjEdos.append(aux)
        
        return conjEdos
    
    def ir_a(self, estados, simbolo):
        conjEdos = []
        aux=self.mover1(estados,simbolo)
        conjEdos = self.cerradura_e1(aux)
        return conjEdos

    def trans(self):
        transiciones=[]
        for i in range(len(self.alfabeto)+2):
            transiciones.append(-1)
        return transiciones

    def listar_conj(self,automatas):
        conj=[]
        for e in automatas:
            conj.append(e.idEstado)
        return conj
    
    def convertir_AFN_a_AFD(self):
        conjIrA=[]
        conjEst=[]
        irA=[]
        tabla=[]
        estados=[]

        #calculamos la cerradura epsilon del estado inicial
        conjIrA.append(self.cerradura_e(self.edoInicial))
        conjEst.append(self.listar_conj(conjIrA[0]).sort)
    
        #calculamos los demas conjuntos
        for conj in conjIrA:
            for a in self.alfabeto:
                irA=self.ir_a(conj,a)
                if len(irA)!=0:
                    aux=self.listar_conj(irA)
                    aux.sort()
                    if aux not in conjEst:
                        conjEst.append(aux)
                        conjIrA.append(irA)

        #agregamos las transiciones
        for conj in conjIrA:
            trans=self.trans()
            for ch in self.alfabeto:
                irA=self.ir_a(conj,ch)
                aux=self.listar_conj(irA)
                aux.sort()
                if aux in conjEst:
                    trans[self.alfabeto.index(ch)+1]=conjEst.index(aux)
            
            for e in self.edosAcept:
                if e in conj:
                    trans[len(trans)-1]=e.token
                    break
            
            trans[0]=conjIrA.index(conj)
            tabla.append(trans)
           
        #creamos el AFD
        afd=AFD(tabla,self.alfabeto)
        return afd

    
    #toString
    def __str__(self):
        return str(self.idAFN)
        

    '''def cargar_AFD(self, nombre):

         #Extraemos la información del archivo
        f=open(f'.//AFDs//{nombre}', 'r')
        informacion=f.readlines()#Obtenemos el contenido en una sola linea
        contenido=[]

        #Separamos la información
        for i in informacion:
            contenido.append(i.split(','))
           
        if len(contenido)==0:
            print("El archivo esta vacio")
            return 
        
        #Cargamos el alfabeto
        for a in contenido[0][1:len(contenido[0])-1]:
            self.alfabeto.append(a)
        
        #obtenemos el número de estados
        estados=[]
        for e in contenido[1:len(contenido)]:
           edo=Estado()
           edo.setIdEstado(int(e[0]))
           self.edosAFN.append(edo)
           estados.append(e[0])

        #agregamos transiciones a cada uno de los estados
        for edo in self.edosAFN:
            for a in self.alfabeto:
                i=self.edosAFN.index(edo)+1
                j=self.alfabeto.index(a)+1
                if contenido[i][j]!='-1':
                    indice=estados.index(contenido[i][j])
                    edo.trans.append(Transicion(a,estado=self.edosAFN[indice]))
        
            if contenido[i][len(contenido)-1]=='1':# establecemos el estado de aceptación
               self.edosAcept.append(self.edosAFN[i-1])
               self.edosAFN.pop(i-1)
        
        self.edoInicial=self.edosAFN[0]#establecemos el estado
        self.archivo=f'.//AFDs//{nombre}'
        self.isAFD=True
    
        return self
                    
    def convetir_AFN_a_AFD(self,nombre,ID):
        conjIrA=[]
        irA=[]
        estados=[]
        conjEstados=[]

        #se calcula la cerradura epsilon del estado inicial (I0)
        cerradura=self.cerradura_e(self.edoInicial)
        conjEstados.append(self.listar_conj(cerradura).sort())
        conjIrA.append(cerradura)
       

        #calculamos los demas conjuntos
        for conj in conjIrA:
            for a in self.alfabeto:
                irA=self.ir_a(conj,a)
                if len(irA)!=0: 
                    aux=self.listar_conj(irA)
                    aux.sort()
                    if aux not in conjEstados:
                        edo=Estado()
                        conjEstados.append(aux)
                        conjIrA.append(irA)
                        for e in self.edosAcept:
                            if e in irA:
                               edo.token=e.token
                        estados.append(edo)

        #Eliminamos los estados del AFN
        self.edoInicial=None
        self.edosAFN.clear()

        #Indicamos las transiciones para cada estado obtenido por el conjunto
        transiciones=[]
        nEdosAcept=[]

        for conj in conjIrA:
            trans=self.trans()
            trans[0]=estados[conjIrA.index(conj)].idEstado
            for ch in self.alfabeto:
                irA=self.ir_a(conj,ch)
                aux=self.listar_conj(irA)
                aux.sort()
                if aux in conjEstados:
                    estados[conjIrA.index(conj)].trans.append(Transicion(ch,estado=estados[conjEstados.index(aux)]))
                    trans[self.alfabeto.index(ch)+1]=estados[conjEstados.index(aux)].idEstado
                    self.edosAFN.append(estados[conjIrA.index(conj)])
        
            for e in self.edosAcept:
                if e in conj:
                    trans[len(trans)-1]=1
                    nEdosAcept.append(estados[conjIrA.index(conj)])
        
            transiciones.append(trans)

        self.edoInicial=self.edosAFN[0]  #indicamos el Estado inicial
        self.edosAcept=nEdosAcept
        self.cambiar_id(ID)#cambiamos el ID
        self.archivo=f'.//AFDs//{nombre}'
        self.isAFD=True

        #Creamos el archivo
        f=open(f'.//AFDs//{nombre}',"w")
        f.write('  ,')#separacion de la columna
        for a in self.alfabeto:
            f.write(f'{a},')
        f.write("Edo. Acept\n")

        for t in transiciones:
            for i in range(len(t)):
              f.write(f'{t[i]},')
            f.write('\n')
        
        return self  
      
    def evaluar_con_AFD(self,cadena):
        i=0
        edos=[]
        nEdo=self.edoInicial

        while i<len(cadena)-1:
            edos=self.mover(nEdo, cadena[i])
            if len(edos)!=0:
                nEdo=edos.pop()
                i+=1
            else:
                nEdo=self.edoInicial

            if cadena[i] not in self.alfabeto:
                break
       
        if nEdo in self.edosAcept:
            print("Cadena Aceptada")
'''
