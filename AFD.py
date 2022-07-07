AFD_id=0

class AFD:

    #constructor
    def __init__(self,tabla, alfabeto):
       global AFD_id
       AFD_id+=1
       self.id = AFD_id
       self.tabla=tabla
       self.alfabeto=alfabeto
       self.archivo=""

    def imprimir_Tabla(self):
        print(f"ID: {self.id}")
        print(f"   {self.alfabeto} Token")
        for fila in self.tabla:
           print(fila)
    
    def crear_Archivo(self,nombre):
        f=open(f'.//AFDs//{nombre}.csv',"w")
        f.write('  ,')#separacion de la columna

        for a in self.alfabeto:
            f.write(f'{a},')
        f.write("Token\n")

        for t in self.tabla:
            for i in range(len(t)):
                f.write(f'{t[i]},')
            
            f.write('\n')
        self.archivo=".//AFDs//" + nombre+".csv"

        f.close()

    
    def cargarAFD(self,nombre):

        tabla=[]
        alfabeto=[]
      
        #Extraemos la información del archivo
        f=open(f'.//AFDs//{nombre}')
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
            alfabeto.append(a)
             
        #Cargamos la tabla
        for tab in contenido[1:len(contenido)]:
            aux=[]
            for e in tab[0:len(tab)-1]:
                aux.append(int(e))
            tabla.append(aux)
        
        a=AFD(tabla, alfabeto)
        a.archivo=".//AFDs//" + nombre

        return a
    
    def setId(self,id):
        self.id=id

    def __str__(self):
        return str(self.id)


