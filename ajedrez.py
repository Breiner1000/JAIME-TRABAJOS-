
# def newTabla (numF,numC,valor,valor2):
    
#    tabla=[]
#    for i in range(numF):
#        tabla.append([])
#        for j in range(numC):
           
#            if i % 2 == 0:
#                if j % 2 == 0:
#                    tabla[i].append(valor)
#                else:
#                    tabla[i].append(valor2)
               
#            else:
#                if j % 2 != 0:
#                    tabla[i].append(valor)
#                else:
#                    tabla[i].append(valor2)
            
#    return tabla

def newTabla (bla,neg):
    
    tabla=[]
    for i in range(4):
       tabla.append([])
       for j in range(4):
           
           
            if i % 2 == 0:
                
                tabla[i].append(bla)
                tabla[i].append(neg)
            else:
                
                tabla[i].append(neg)
                tabla[i].append(bla)
            
    return tabla

def seeTabla (tabla):
    
    for fil in tabla:
        for col in i:
            
            
    return tabla

ta=newTabla("B","N")

print(ta)
 