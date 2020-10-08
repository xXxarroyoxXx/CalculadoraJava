numero = int(input("Mete el numero"))
Abinario = ""
if (numero > 0):
    while (numero>0):
        if (numero%2 == 0):
            Abinario = "0"+Abinario
        else:
            Abinario = "1"+Abinario
        numero = int(numero//2)
else:
    if (numero == 0):
        Abinario = "0"
    else:
        Abinario = "Gilipollas no existen binarios negativos"
print("Dale "+Abinario)


