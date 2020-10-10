numero=0
Abinario = ""
eleccion=int(input("""Bienvenido a la calculadora Binaria.Introduce tu eleccion
1.Para sumar
2.Para Restar
3.Para Multiplicar
4.Para dividir
(PD:Recuerda que no se admiten numeros negativos,Gracias.)"""))
def conversorbinario(numero,Abinario):
    if (numero>0):
        while (numero>0):
            if (numero%2==0):
                Abinario="0"+Abinario
            else:
                Abinario="1"+Abinario
            numero=int(numero//2)
    else:
        if (numero==0):
            Abinario="0"
        else:
            Abinario="te lo dije antes, no se admiten negativos"
    print("Dale " +Abinario)
    return (numero,Abinario)

if (eleccion<=0 or eleccion<=5):
    numero1=int(input("Mete el numero1: "))
    numero2=int(input("Introduce el numero 2: "))
    if (eleccion==1):
        numero=numero1+numero2
        conversorbinario(numero,Abinario)
    elif (eleccion==2):
        numero=numero1-numero2
        conversorbinario(numero,Abinario)
    elif (eleccion==3):
        numero=numero1*numero2
        conversorbinario(numero,Abinario)
    elif (eleccion==4):
        numero=numero1/numero2
        conversorbinario(numero,Abinario)
else:
    print("Eleccion incorrecta")


