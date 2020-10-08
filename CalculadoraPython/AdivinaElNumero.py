'''
Created on 30 sept. 2020

@author: fran
'''
import random;
def AdivinaNumero():
    numeroAleatorio=random.randrange(0,10)
    intentos=0
    numeroIntroducido=0;
    while numeroIntroducido!=69:
        print("Para salir pulsa e")
        numeroIntroducido=input("Introduce un numero entre el 0-10")
        intentos+=1
        if numeroIntroducido==69:
            print("El numero aleatorio era",str(numeroAleatorio))
            break
        elif int(numeroIntroducido)<(numeroAleatorio):
            print("El numero introducido es muy pequeno")
        elif int(numeroIntroducido)>(numeroAleatorio):
            print("El numero que introduciste es muy grande")
        else:
            print("Enhorabuena, acertaste")
            print("Acertaste el numero",str(numeroAleatorio)," en",str(intentos),"intentos")
            break
    AdivinaNumero()
print(AdivinaNumero())