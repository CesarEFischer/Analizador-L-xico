from queue import Empty
from tkinter import messagebox
from tkinter import filedialog
from AFN import AFN
from AFD import AFD
from AnaLex import AnaLex
from ER_AFN import ER_AFN
from DescRecGram_Gram import DescRecGram_Gram
from LL1 import LL1
from LR0 import LR0
from LR1 import LR1

def crear(simbI,simbS):
    a = AFN()

    #Casos 
    if simbI == '' and simbS=='':
            messagebox.showinfo('Aviso','No haz ingresado al menos un valor')
    elif simbI == '' and simbS != '':
        a.crear_AFN_Basico(simbS,simbS)
    elif simbI !='' and simbS == '':
        a.crear_AFN_Basico(simbI,simbI)
    else:
        a.crear_AFN_Basico(simbI,simbS)

    if len(a.edosAFN)>0:
        messagebox.showinfo('Aviso','Automata Creado')
        return a
    else:
        messagebox.showinfo('Exito','Automata no Creado')
        return None

def union(a1,a2,automatas):
    if a1==-1 and a2==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    elif a1>-1 and a2==-1:
        messagebox.showinfo('Aviso','No haz seleccionado el automata 2')
    elif a1==-1 and a2 >-1:
        messagebox.showinfo('Aviso','No haz seleccionado el automata 1')
    else:
        aux = automatas[a2]
        automatas[a1].unir_Automata(aux)
            
        if aux.idAFN != automatas[a1].idAFN:
            automatas.remove(aux)
    messagebox.showinfo('Exito!','El Automata ha sido creado')

def concatenar(a1,a2,automatas):
    if a1==-1 and a2==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    elif a1>-1 and a2==-1:
        messagebox.showinfo('Aviso','No haz seleccionado el automata 2')
    elif a1==-1 and a2 >-1:
        messagebox.showinfo('Aviso','No haz seleccionado el automata 1')
    else:
        aux = automatas[a2]
        automatas[a1].concatenar_Automata(aux)
                
        if aux.idAFN != automatas[a1].idAFN:
            automatas.remove(aux)
    messagebox.showinfo('Exito!','El Automata ha sido creado')

def cerradura_t(i,automatas):
    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    else: 
        automatas[i].cerradura_transitiva()
        messagebox.showinfo('Exito!','El Automata ha sido creado')

def cerradura_k(i,automatas):
    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    else: 
        automatas[i].cerradura_Kleen()
        messagebox.showinfo('Exito!','El Automata ha sido creado')

def opcional(i,automatas):
    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    else: 
        automatas[i].opcional()
        messagebox.showinfo('Exito!','El Automata ha sido creado')

def cargar(i, automatas,token):
    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
        return None
    else: 
        messagebox.showinfo('Exito!','El Automata ha sido creado')
        return(automatas[i],token)

def union_especial(conjAutomatas, automatas):
   
    if len(automatas)==0:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    elif len(automatas)==1:
        messagebox.showinfo('Aviso','Tienes un solo elemento o esta duplicado ')
    else:
        a =AFN()
        for aux in automatas:
            a.union_especial(aux[0],aux[1])
            if len(conjAutomatas)>0:
                conjAutomatas.remove(aux[0])

        conjAutomatas.append(a)

        if a!=None:
            messagebox.showinfo('Exito!','El automata fue transformado de manera correcta')
           
def convertir_a_AFD(automatas, i, nombre,ID):
    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
        return None
    else: 
        if len(nombre)==0:
           messagebox.showinfo('Aviso','No ha sido especificado el nombre del archivo')
           return 
        else:
            afd = automatas[i].convertir_AFN_a_AFD()
            afd.setId(ID)
            afd.crear_Archivo(nombre)
            messagebox.showinfo('Exito!','El automata fue transformado de manera correcta')
            return afd

def seleccionar(carpeta):
    nombre=''
    filename = filedialog.askopenfilename(initialdir = carpeta, 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
    if len(filename)!=0:
        name=filename.split('/')
        nombre=name[len(name)-1]
    
    return nombre
    
def cargar_AFD(nombre,ID):
    if len(nombre)==0:
        messagebox.showinfo("Aviso","No se ha seleccionado un archivo")
        return None
    else:
        afd=AFD([],[])
        afd=afd.cargarAFD(nombre)
        afd.setId(ID)
        messagebox.showinfo("Exito!","El automata fue cargado correctamente")
        return afd

def evaluar(automata,i, cadena):
    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    else:
        if len(cadena)!=0:
            recorrido=[]
            AnaLexico=AnaLex(automata[i],cadena)
            recorrido=AnaLexico.getListaLexems()
          
            if AnaLexico.edoAcept == True:
               messagebox.showinfo("Exito!","La cadena fue aceptada")
            else:
                messagebox.showinfo("Aviso","La cadena no fue aceptada")

            return recorrido

def ER_a_AFN(id,expresion):

    if len(expresion)==0:
        messagebox.showinfo('Aviso','La cadena esta vacia')
    else:
        afd=AFD([],[])
        afd=afd.cargarAFD("AFDER.csv") #cargamos el afd de expresiones regulares
        ana=AnaLex(afd,expresion)
        e=ER_AFN(ana)

        if e.IniConversion():
            if len(id)!=0:
                e.result.cambiar_id(id)
            messagebox.showinfo('Aviso','Automata Creado')
        else:
            messagebox.showinfo('Aviso','La cadena esta vacia')

        return e.result

def cargar_Gramatica(nombre):
    if len(nombre)==0:
        messagebox.showinfo("Aviso","No se ha seleccionado un archivo")
        return None
    else:
        f=open(f'.//Gramaticas//{nombre}')
        info = f.readlines()#Obtenemos el contenido en una sola linea

        if len(info)!=0:
            rules=""

            for r in info:
                aux = r.split("\n")
                rules+=aux[0]

            gramaticas_AFD=AFD([],[])
            gramaticas_AFD=gramaticas_AFD.cargarAFD("AFDGram_Gram.csv")

            syn = DescRecGram_Gram(gramaticas_AFD,rules)
          
            if syn.AnalizarGramatica():
               for r in syn.arrReglas:
                    if r.isLeftRecursive():
                        messagebox.showinfo("Aviso","La Gramatica es recursiva")
                        return None
                    else:
                        messagebox.showinfo("Aviso","La Gramatica es valida")
                        return syn
            else:
                messagebox.showinfo("Aviso","La Gramatica no es valida")
                return None

def analisis_ll1(i, AFDs,gramatica,string):

    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    else:
        if len(string)==0:
          messagebox.showinfo('Aviso','La cadena esta vacia')
        else:
            a=AFDs[i]
            Lex=AnaLex(a,string)
            ll1=LL1(gramatica.arrReglas,Lex)

            if(ll1.isLL1()):
                messagebox.showinfo('Aviso','Gramatica compatible con LL(1)')
                res = ll1.analyze(string)
                ll1.displayTable(1)
               
                if(res):
                    print("\n" + string + " pertenece a la gramatica\nRevise la tabla en la carpeta tablas")
                
                else:
                    print("\n" + string + " no pertenece a la gramatica")
                        
            else:
                messagebox.showinfo('Aviso','La gramatica no es compatible con LL(1)')
                ll1.displayTable(0)

def analisis_lr0(i, AFDs,gramatica,string):

    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    else:
        if len(string)==0:
          messagebox.showinfo('Aviso','La cadena esta vacia')
        else:
            a=AFDs[i]
            Lex=AnaLex(a,string)
            lr0=LR0(gramatica.arrReglas,Lex)

            if(lr0.isLR0()):
                messagebox.showinfo('Aviso','Gramatica compatible con LL(1)')
                res = lr0.analyze(string)
                lr0.displayTable(1)
               
                if(res):
                    print("\n" + string + " pertenece a la gramatica\nRevise la tabla en la carpeta tablas")
                
                else:
                    print("\n" + string + " no pertenece a la gramatica")
                        
            else:
                messagebox.showinfo('Aviso','La gramatica no es compatible con LL(1)')
                lr0.displayTable(0)
              
def analisis_lr1(i, AFDs,gramatica,string):

    if i ==-1:
        messagebox.showinfo('Aviso','No hay elementos o no haz seleccionado')
    else:
        if len(string)==0:
          messagebox.showinfo('Aviso','La cadena esta vacia')
        else:
            a=AFDs[i]
            Lex=AnaLex(a,string)
            lr1=LR1(gramatica.arrReglas,Lex)

            if(lr1.isLR1()):
                messagebox.showinfo('Aviso','Gramatica compatible con LL(1)')
                res = lr1.analyze(string)
                lr1.displayTable(1)
               
                if(res):
                    print("\n" + string + " pertenece a la gramatica\nRevise la tabla en la carpeta tablas")
                
                else:
                    print("\n" + string + " no pertenece a la gramatica")
                        
            else:
                messagebox.showinfo('Aviso','La gramatica no es compatible con LL(1)')
                lr1.displayTable(0)
                      
                                


