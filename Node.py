
#Cada Nodo que creemos sera una regla Gramatical

class Node:
    def __init__(self, symbol, next):
        self.symbol = symbol              
        self.next = next                   
        self.pointBefore = False            
        self.pointAfter = False             
        self.lr1Symbols = set([])           
        self.counter = 0                   

    def getNext(self):
        return self.next
      
    def setCounter(self, c):
        self.counter = c

  
    def getCounter(self):
        return self.counter

   
    def setNext(self, next):
        self.next = next
    
   
    def getSymbol(self):
        return self.symbol
    
  
    def setSymbol(self, symbol):
        self.symbol = symbol

   
    def getPointBefore(self):
        return self.pointBefore
    
  
    def setPointBefore(self, pointBefore):
        self.pointBefore = pointBefore

  
    def getPointAfter(self):
        return self.pointAfter
    
   
    def setPointAfter(self, pointAfter):
        self.pointAfter = pointAfter

    def getLR1Symbols(self):
        return self.lr1Symbols
    
 
    def setLR1Symbols(self, lr1Symbols):
        self.lr1Symbols = lr1Symbols

 
    def size(self):
        next = self.getNext()
        cont = 0
        while(next != None):
            if(next.getSymbol() == "epsilon"):
                return 0
            cont += 1
            next = next.getNext()
        return cont

    def isLeftRecursive(self):
        next = self.getNext()
        return next.getSymbol() == self.symbol

    def equals(self, other):
        if(self.symbol != other.getSymbol()):
            return False
        else:
            if(self.size() != other.size()):
                return False
            else:
                next = self.getNext()
                n = other.getNext()

                while(n != None and next != None):
                    if(next.getSymbol() != n.getSymbol()):
                        return False
                    else:
                        if(next.getPointBefore() != n.getPointBefore()):
                            return False
                        else:
                            if(next.getPointAfter() != n.getPointAfter()):
                                return False
                    next = next.getNext()
                    n = n.getNext()
        return True

    def getRule(self):
        rule = [self.symbol, "->"]
        next = self.getNext()

        while(next != None):
            rule.append(next.getSymbol())
            next = next.getNext()
        return rule

  
    def displayRule(self):
        print("{} ->".format(self.symbol), end = '')
        next = self.getNext()

        while(next != None):
            print(" {}".format(next.getSymbol()), end = '')
            next = next.getNext()
        print("")

    def displayItems(self):
        print("{} ->".format(self.symbol), end = '')
        next = self.getNext()

        while(next != None):
            if(next.getPointBefore()):
                print(" °{}".format(next.getSymbol()), end = '')
            elif(next.getPointAfter()):
                print(" {}°".format(next.getSymbol()), end = '')
            else:
                print(" {}".format(next.getSymbol()), end = '')
            next = next.getNext()
        print("")