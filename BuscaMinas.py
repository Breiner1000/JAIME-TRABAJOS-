# cont1, cont2, cont3, cont4, cont5, cont6  = 0, 0, 0, 0, 0, 0

# num = int(input("digite la cantidad de veces que va lanzar el dado: "))

# for i in range(num):
    
#     dado = random.randint(1,6)
    
#     if dado == 1:
#         cont1+=1
#     elif dado == 2:
#         cont2+=1
#     elif dado == 3:
#         cont3+=1
#     elif dado == 4:
#         cont4+=1
#     elif dado == 5:
#         cont5+=1
#     else:
#         cont6+=1

# print("El numero 1 salio",cont1);print(" veces.")
# print("El numero 2 salio",cont2);print(" veces.")
# print("El numero 3 salio",cont3);print(" veces.")
# print("El numero 4 salio",cont4);print(" veces.")
# print("El numero 5 salio",cont5);print(" veces.")
# print("El numero 6 salio",cont6);print(" veces.")

import random
 
def newTabla (numF,numC,valor):
    
   tabla=[]
   for i in range(numF):
       tabla.append([])
       for j in range(numC):
           tabla[i].append(valor)
            
   return tabla 
 
tablaf = newTabla (3,3,"f")
print(tablaf)

#print(type(tablaf))