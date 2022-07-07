from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import Operaciones as op


class ventana:
    conjAutomatas=[]
    conjAFD=[]
    nombre=''

    def __init__(self, name=None, tam="350x400"):
        self.wind=Tk()
        self.wind.title(str(name))
        self.wind.geometry(tam) #da el espacio a la ventana
    
    def imprimir_titulo(self,titulo,fila=0,columna=1, separacion=15,metodo='grid'):
        t= Label(self.wind, text=titulo)
        t.config(font=("Arial",14))
        if metodo!='grid': t.pack(pady=40)
        else: t.grid(pady=separacion, row=fila, column=columna)
    
    def entry(self, titulo, fila, columna, metodo='grid'):
        txt=Entry(self.wind)
        if metodo!='grid':
            Label(self.wind, text=titulo).pack()
            txt.pack()
        else: 
            txt.grid(row=fila,column=columna+1)
            Label(self.wind, text=titulo).grid(pady=5, row=fila, column=columna)
        return txt
    
    def botones(self, accion,fila, columna, separacion=0, metodo='grid'): 
        b = Button(self.wind,text=accion)
        b.config(font=("Arial",12))
        if metodo!='grid':b.pack(pady=separacion)
        else: b.grid(row=fila,column=columna, pady=separacion) 
        return b 
    
    def listados(self,automatas,fila,columna, metodo='grid'):
        caja = Combobox(self.wind,values = automatas)
        if metodo!='grid':caja.pack()
        else: caja.grid(row=fila,column=columna,padx=10,pady=10)
        return caja

# ---------------------------------------------------------------------
#                       ANALIZADOR LEXICO
# ---------------------------------------------------------------------

    def crear_basico(self):
        v=ventana("CREAR BASICO","400x200")
        v.imprimir_titulo("CREAR BASICO")
        e1 = v.entry("Simbolo Inferior: ",1,0)
        e2 = v.entry("Simbolo Superior: ",2,0)

        def crear():
            v.wind.lower()# baja de nivel la ventana para que se pueda ver el mensaje
            simbI = e1.get() #obtenemos el contenido de los entrys
            simbS = e2.get()
           
            a = op.crear(simbI,simbS)#crea mi automata

            if a != None:
                self.conjAutomatas.append(a)

            e1.delete(0,"end")
            e2.delete(0,"end")
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal
        
        v.botones("Crear",3,1,10).config(command=crear) #Boton que crea el AFN 
        v.wind.mainloop()
    
    def unir(self):
        v = ventana("UNIR","460x200")
        v.imprimir_titulo("UNION",columna=2)
        
        #listados
        l1 = v.listados(self.conjAutomatas,1,1)
        Label(v.wind,text="unir con ").grid(row=1,column=2,pady=10)
        l2 = v.listados(self.conjAutomatas,1,3)

        def union():
            v.wind.lower()# baja la ventana de nivel
            op.union(l1.current(),l2.current(),self.conjAutomatas) #realiza la union
            v.wind.destroy() #eleva la ventana para evitar que sea vea la principal

        v.botones("Unir",3,2,10).config(command=union) #Realiza la union de AFN
        v.wind.mainloop()
    
    def concatenar(self):
        v = ventana("CONCATENAR","550x200")
        v.imprimir_titulo("CONCATENACION",columna=2)
        
        #listados
        l1 = v.listados(self.conjAutomatas,1,1)
        Label(v.wind,text="concatenar con").grid(row=1,column=2,pady=5)
        l2 = v.listados(self.conjAutomatas,1,3)

        def concatenacion():
            v.wind.lower()# baja la ventana de nivel
            op.concatenar(l1.current(),l2.current(), self.conjAutomatas) #operacion concatenar
            v.wind.destroy() #eleva la ventana para evitar que sea vea la principal


        v.botones("Concatenar",3,2,10).config(command=concatenacion) #Realiza la concatenacion de AFN
        v.wind.mainloop()

    def cerradura_transitiva(self):
        v = ventana("CERRADURA TRANSITIVA",'350x250')
        v.imprimir_titulo("CERRADURA +",metodo='pack')
        
        #listados
        l1 = v.listados(self.conjAutomatas,0,0,metodo='pack')

        def cerradura_T():
            v.wind.lower()# baja la ventana de nivel
            op.cerradura_t(l1.current(),self.conjAutomatas)
            v.wind.destroy() #destruye la ventana 

        v.botones("Cerradura +",0,0,10,metodo='pack').config(command=cerradura_T) #Realiza la concatenacion de AFN
        v.wind.mainloop()
    
    def cerradura_kleen(self):
        v = ventana("CERRADURA DE KLEEN",'350x250')
        v.imprimir_titulo("CERRADURA *",metodo='pack')
        
        #listados
        l1 = v.listados(self.conjAutomatas,1,2,metodo='pack')

        def cerradura_K():
            v.wind.lower()# baja la ventana de nivel
            op.cerradura_k(l1.current(),self.conjAutomatas)
            v.wind.destroy() #destruye la ventana 

        v.botones("Cerradura *",0,0,10,metodo='pack').config(command=cerradura_K) #Realiza la concatenacion de AFN
        v.wind.mainloop()
    
    def opcional_i(self):
        v = ventana("OPCIONAL","350x250")
        v.imprimir_titulo("OPCIONAL !",metodo='pack')
        
        #listados
        l1 = v.listados(self.conjAutomatas,1,2,metodo='pack')

        def opc():
            v.wind.lower()# baja la ventana de nivel
            op.opcional(l1.current(),self.conjAutomatas)
            v.wind.destroy() #destruye la ventana 

        v.botones("Opcional !",0,0,10,metodo='pack').config(command=opc) #Realiza la concatenacion de AFN
        v.wind.mainloop()

    def er_afn(self):

        v = ventana("ER->AFN","400x200")
        v.imprimir_titulo("ER->AFN")
        e1 = v.entry("ID: ",1,1)
        e2 = v.entry("ER: ",2,1)

        def transformar():
            v.wind.lower()# baja la ventana de nivel
            exp=str(e1.get())
            #print(exp)
            a=op.ER_a_AFN(exp,e2.get())
            if a!=None:
                self.conjAutomatas.append(a)
            
            e1.delete(0,"end")
            e2.delete(0,"end")
            
            v.wind.destroy() #eleva la ventana para evitar que sea vea la principal

        v.botones("Crear",3,1,10).config(command=transformar) #Boton que crea el AFN 
        v.wind.mainloop()

    def union_especial(self):
        v = ventana("UNION ESPECIAL","500x550")
        conjAuto=[]
        tokens=[]
        items=[]

        #listado
        Label(v.wind, text='Seleccionar automatas:').grid(row=0, column=0)
        l = v.listados(self.conjAutomatas,2,0)
        e1=v.entry("Token: ", 2, 1)

        #tabla
        tabla=ttk.Treeview(v.wind,columns='Token',height=1)
        tabla.column('#0',minwidth=0,width=80)
        tabla.heading('#0',text='ID AFN')
        tabla.heading('Token',text='Token')
        tabla.column('Token',minwidth=0,width=80 )
        tabla.grid(row=6,column=0,padx=20,pady=10)

        def cargar():
            v.wind.lower()# baja la ventana de nivel
            a=op.cargar(l.current(),self.conjAutomatas,int(e1.get()))

            if a!=None:
                conjAuto.append(a)
                l1.configure(values=conjAuto)
                tabla.config(height=len(conjAuto))
                items.append(tabla.insert("",END,text=a[0],values=int(a[1])))
            
            e1.delete(0,"end")
            
            v.wind.lift()
        v.botones("Cargar",3,0,0).config(command=cargar)

        Label(v.wind, text='Eliminar automata').grid(row=4, column=0)
        
        l1 = v.listados(conjAuto,4,0)

        def eliminar():
            tabla.delete(items[l1.current()])
            items.pop(l1.current())
            conjAuto.pop(l1.current())
            
        v.botones("Eliminar Elemento",5,0,0).config(command=eliminar)

        def union_e():
            v.wind.lower()# baja la ventana de nivel
            op.union_especial(self.conjAutomatas,conjAuto)
            v.wind.destroy() #destruye la ventana 

        v.botones("Unir ",7,0,0).config(command=union_e)
    
    def convertir_AFN(self):
        v = ventana("CONVERTIR AFN a AFD","500x200")
       
        nombre=v.entry("Nombre del archivo:", 1,0)
        Label(v.wind, text='Seleccionar automata:').grid(row=3, column=0,padx=10)
        ID = v.entry("ID del AFD: ",2,0)
        l = v.listados(self.conjAutomatas,3,0)

        def convertir():
            v.wind.lower()# baja la ventana de nivel
            a=op.convertir_a_AFD(self.conjAutomatas,l.current(), nombre.get(),ID.get())
            if a!=None:
             self.conjAFD.append(a)
            v.wind.destroy() #destruye la ventana 

        v.botones("Convertir",4,0,0).config(command=convertir)
        v.wind.mainloop()
    
    def evaluar_cadena(self):
        v = ventana("EVALUAR CADENA","500x400")

        def seleccionar_AFD():
            name=op.seleccionar(".//AFDs")
            self.nombre=name
            Label(v.wind,text=f'Archvo seleccionado: {name}').grid(row=2,column=1)
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal

        Label(v.wind, text='Cargar AFD').grid(row=0, column=0,padx=30)
        ID=v.entry("ID:",1,0)
        v.botones("Seleccionar Archivo",2,0,0).config(command=seleccionar_AFD)
      
        def cargar_AFD():
            v.wind.lower()# baja la ventana de nivel
            a=op.cargar_AFD(self.nombre,str(ID.get()))
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal
            if a != None: 
                self.conjAFD.append(a)
            l.configure(values=self.conjAFD)
            
        v.botones("Cargar",3,0,5).config(command=cargar_AFD)

        Label(v.wind, text='Evaluar cadena').grid(row=4, column=0,padx=30)
        l=v.listados(self.conjAFD,5,0)
        cadena=v.entry("Cadena a evaluar:",5,1)

    
        def evaluar():
            recorrido=op.evaluar(self.conjAFD,l.current(), cadena.get())
            if len(recorrido)!=0:

                #tabla de recorridos
                f=open(self.conjAFD[0].archivo)

                informacion=f.readlines()#Obtenemos el contenido en una sola linea
                contenido=[]

                #Separamos la información
                for i in informacion:
                    aux=i.split(',')
                    if informacion.index(i)==0:
                        aux=aux[1:len(aux)]
                    contenido.append(aux)

                    tabla1 = ttk.Treeview(v.wind,columns=contenido[0],height=len(contenido)-1)

                    tabla1.column('#0',minwidth=0,width=50)
                    for e in contenido[0]:
                        tabla1.heading(e,text=e, anchor=CENTER)
                        tabla1.column(e,minwidth=0,width=50)

                    for t in contenido[1:len(aux)]:
                        tabla1.insert("",END, text=t[0],values=t[1:len(t)])
                    tabla1.grid(row=8,column=1)


                #tabla de recorridos
                Label(v.wind, text='Recorrido dado').grid(row=7, column=0,padx=10)
             
                tabla=ttk.Treeview(v.wind,columns='Estado',height=1)
                tabla.column('#0',minwidth=0,width=80)
                tabla.heading('#0',text='Lexema')
                tabla.heading('Estado',text='Estado')
                tabla.column('Estado',minwidth=0,width=80)
                tabla.grid(row=8,column=0,padx=20,pady=10)

                tabla.config(height=len(recorrido))
    
                for i  in range(len(recorrido)):
                    tabla.insert("",END,text=recorrido[i][0],values=recorrido[i][1])

        v.botones("Evaluar",6,0,10).config(command=evaluar)
    
# ---------------------------------------------------------------------
#                       ANALIZADOR SINTACTICO
# ---------------------------------------------------------------------

    def ll1(self):
        v = ventana("ANALIZADOR SINTACTICO LL(1)","500x400")
        a=None

        def seleccionar_Gramatica():
            name=op.seleccionar(".//Gramaticas")
            self.nombre=name
            Label(v.wind,text=f'Archvo seleccionado: {name}').grid(row=2,column=1)
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal

        Label(v.wind, text='Cargar Gramatica').grid(row=1, column=0,padx=30)
        v.botones("Seleccionar Archivo",2,0,0).config(command=seleccionar_Gramatica)
      
        def cargar_Gram():
            v.wind.lower()# baja la ventana de nivel
            a=op.cargar_Gramatica(self.nombre)
    
            if a==None:v.wind.destroy()

            v.wind.lift() #eleva la ventana para evitar que sea vea la principal
            
        v.botones("Cargar",3,0,5).config(command=cargar_Gram)

        Label(v.wind, text='Cargar Analizador Lexico').grid(row=4, column=0,padx=30)

        def seleccionar_AFD():
            name=op.seleccionar(".//AFDs")
            self.nombre=name
            Label(v.wind,text=f'Archvo seleccionado: {name}').grid(row=5,column=1)
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal

        v.botones("Seleccionar Archivo",5,0,0).config(command=seleccionar_AFD)
        ID=v.entry("ID:",6,0)
      
        def cargar_AFD():
            v.wind.lower()# baja la ventana de nivel
            a=op.cargar_AFD(self.nombre,str(ID.get()))
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal
            if a != None: 
                self.conjAFD.append(a)
            l.configure(values=self.conjAFD)
            
        v.botones("Cargar",7,0,5).config(command=cargar_AFD)

        l=v.listados(self.conjAFD,8,0)
        cadena=v.entry("Cadena a Analizar:",8,1)
    
        def analizar_ll1():
            op.analisis_ll1(l.current(),a,cadena.get())

        v.botones("Analizar",9,0,10).config(command=analizar_ll1)

    def lr0(self):
        v = ventana("ANALIZADOR SINTACTICO LR(0)","500x400")
        a=None

        def seleccionar_Gramatica():
            name=op.seleccionar(".//Gramaticas")
            self.nombre=name
            Label(v.wind,text=f'Archvo seleccionado: {name}').grid(row=2,column=1)
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal

        Label(v.wind, text='Cargar Gramatica').grid(row=1, column=0,padx=30)
        v.botones("Seleccionar Archivo",2,0,0).config(command=seleccionar_Gramatica)
      
        def cargar_Gram():
            v.wind.lower()# baja la ventana de nivel
            a=op.cargar_Gramatica(self.nombre)
    
            if a==None:v.wind.destroy()

            v.wind.lift() #eleva la ventana para evitar que sea vea la principal
            
        v.botones("Cargar",3,0,5).config(command=cargar_Gram)

        Label(v.wind, text='Cargar Analizador Lexico').grid(row=4, column=0,padx=30)

        def seleccionar_AFD():
            name=op.seleccionar(".//AFDs")
            self.nombre=name
            Label(v.wind,text=f'Archvo seleccionado: {name}').grid(row=5,column=1)
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal

        v.botones("Seleccionar Archivo",5,0,0).config(command=seleccionar_AFD)
        ID=v.entry("ID:",6,0)
      
        def cargar_AFD():
            v.wind.lower()# baja la ventana de nivel
            a=op.cargar_AFD(self.nombre,str(ID.get()))
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal
            if a != None: 
                self.conjAFD.append(a)
            l.configure(values=self.conjAFD)
            
        v.botones("Cargar",7,0,5).config(command=cargar_AFD)

        l=v.listados(self.conjAFD,8,0)
        cadena=v.entry("Cadena a Analizar:",8,1)
    
        def analizar_lr0():
            op.analisis_lr0(l.current(),a,cadena.get())

        v.botones("Analizar",9,0,10).config(command=analizar_lr0)

    def lr1(self):
        v = ventana("ANALIZADOR SINTACTICO LR(1)","500x400")
        a=None

        def seleccionar_Gramatica():
            name=op.seleccionar(".//Gramaticas")
            self.nombre=name
            Label(v.wind,text=f'Archvo seleccionado: {name}').grid(row=2,column=1)
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal

        Label(v.wind, text='Cargar Gramatica').grid(row=1, column=0,padx=30)
        v.botones("Seleccionar Archivo",2,0,0).config(command=seleccionar_Gramatica)
      
        def cargar_Gram():
            v.wind.lower()# baja la ventana de nivel
            a=op.cargar_Gramatica(self.nombre)
    
            if a==None:v.wind.destroy()

            v.wind.lift() #eleva la ventana para evitar que sea vea la principal
            
        v.botones("Cargar",3,0,5).config(command=cargar_Gram)

        Label(v.wind, text='Cargar Analizador Lexico').grid(row=4, column=0,padx=30)

        def seleccionar_AFD():
            name=op.seleccionar(".//AFDs")
            self.nombre=name
            Label(v.wind,text=f'Archvo seleccionado: {name}').grid(row=5,column=1)
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal

        v.botones("Seleccionar Archivo",5,0,0).config(command=seleccionar_AFD)
        ID=v.entry("ID:",6,0)
      
        def cargar_AFD():
            v.wind.lower()# baja la ventana de nivel
            a=op.cargar_AFD(self.nombre,str(ID.get()))
            v.wind.lift() #eleva la ventana para evitar que sea vea la principal
            if a != None: 
                self.conjAFD.append(a)
            l.configure(values=self.conjAFD)
            
        v.botones("Cargar",7,0,5).config(command=cargar_AFD)

        l=v.listados(self.conjAFD,8,0)
        cadena=v.entry("Cadena a Analizar:",8,1)
    
        def analizar_lr1():
            op.analisis_lr1(l.current(),a,cadena.get())

        v.botones("Analizar",9,0,10).config(command=analizar_lr1)




    def opciones(self):
        barraMenu = Menu(self.wind)
        self.wind.config(menu=barraMenu)
        
        #Menus Principales
        menuAFN = Menu(barraMenu)
        menuAnaSintactico=Menu(self.wind)

        #Sub Menus

        #Analizador Lexico
        barraMenu.add_cascade(label="Analizador Lexico",menu=menuAFN)
        menuAFN.add_command(label="Crear Basico",command=self.crear_basico)
        menuAFN.add_command(label="Unir", command = self.unir)
        menuAFN.add_command(label="Concatenar", command = self.concatenar)
        menuAFN.add_command(label ="Cerradura Transitiva", command =self.cerradura_transitiva)
        menuAFN.add_command(label="Cerradura de Kleen", command=self.cerradura_kleen)
        menuAFN.add_command(label="Opcional", command=self.opcional_i)
        menuAFN.add_command(label="ER->AFN",command=self.er_afn)
        menuAFN.add_command(label="Unión para Analizador Lexico ", command=self.union_especial)
        menuAFN.add_command(label="Convertir AFN a AFD", command=self.convertir_AFN)
        menuAFN.add_command(label="Evaluar cadena",command=self.evaluar_cadena)

        #Analisis Sintactico
        barraMenu.add_cascade(label="Analizador Sintactico",menu=menuAnaSintactico)
        menuAnaSintactico.add_command(label="LL1", command=self.ll1)
        menuAnaSintactico.add_command(label="LR0",command=self.lr0)
        menuAnaSintactico.add_command(label="LR1",command=self.lr1)

a = ventana("Compiladores")
a.opciones()
a.wind.mainloop()




