8-+8++++++++++def __init__(self,valor=None,izq=None,der=None)
    self.valor = valor
    self.izq = izq
    self.der = der

    def __str__(self)
 return("%s" (%self.valor)

#1-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ArbolB:
     def __init__(self):
        self.raiz=None

    def agregar(self,dato):
      if(self.raiz==None)
          self.raiz=dato
      else:
          VAux=self.raiz
          padre=none
          while(VAux!=None):
              padre=VAux 
              if(dato.valor) >= (VAux.padre):
                    VAux = VAux.der
                else:          
                    VAux = VAux.izq

if __name__ = "__main__":
#2-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if(dato.valor)>=(padre.valor):
            padre.der= dato
        else:
            padre.izq= dato    
    def Preorden(self,dato):
        if dato!=None:
            print(dato)
            self.preorden(dato.izq)
            self.preorden(dato.der)   
    def getRaiz(self):
        return(self.raiz)
#3-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ar = ArbolB()

while true:
    print("programa Mi Arbol")
    print("1-agregar datos del arbol \n", "2-recorrido preorden \n")
    op = int(input("digite su opaba"))
    
    if(op=1):
        valor =input("digite su Dato:")
        nod=Nodo(valor)
        ar.agregar(nod)
    elif(op=2):
        print("recorrido Preorden")
        ar.preorden(ar.getRaiz())



