from lib2to3.pgen2 import grammar
from os import sync
from AFN import AFN
from AFD import AFD
from AnaLex import AnaLex
from ER_AFN import ER_AFN
from DescRecGram_Gram import DescRecGram_Gram
from LL1 import LL1

gramatica="E->TEp;Ep->+Ep|-TEp|epsilon;T->*FTp;Tp->FTp|/FTp|epsilon;F->(E)|SIN(E)|num;"
afd=AFD([],[])
afd=afd.cargarAFD("AFDGram_Gram.csv")
SynGrammar=DescRecGram_Gram(afd,gramatica)
grammar=SynGrammar.AnalizarGramatica()

if grammar:
    print("Gramatica generada")
    for r in SynGrammar.arrReglas:
        r.displayRule()
        if(r.isLeftRecursive()):
            print("La gramatica es recursiva por la izquierda")


string="2.42*(87-SIN(14/12))"

afd1=AFD([],[])
afd1=afd.cargarAFD("LL(1).csv")

ana=AnaLex(afd1,string)
ll1=LL1(SynGrammar.arrReglas,ana)

if ll1.isLL1():
    print("La gramatica es compartible")
    res = ll1.analyze(string)
    ll1.displayTable(1)
               
    if(res):
        print("\n" + string + " pertenece a la gramatica\nRevise la tabla en la carpeta tablas")
                
    else:
        print("\n" + string + " no pertenece a")

        
        

