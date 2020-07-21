'''
Created on 20 jul. 2020

@author: darkanon
'''
print("1.Para sumar \n2.Para restar \n3.Para multiplicar \n4.Para obtener consciente de la division \n5.Para obtener resto de la division")
eleccion=input("Que opcion elige?")
num1=input("Introduce el primer numero")
num2=input("Introduce el segundo numero")
if eleccion==1:
    resultado=num1+num2
    print("La suma da: ",resultado)
if eleccion==2:
    resultado=num1-num2
    print("La resta da: ",resultado)
if eleccion==3:
    resultado=num1*num2
    print("La multiplicacion da: ",resultado)
if eleccion==4:
    resultado=num1/num2
    print("La division da: ",resultado)
if eleccion==5:
    resultado=num1%num2
    print("El resto da: ",resultado)








