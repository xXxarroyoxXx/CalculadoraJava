'''
Created on 8 oct. 2020

@author: fran
'''
def DecimalABinario(numero):
    
    if numero>=1:
        DecimalABinario(numero//2)
        print(numero%2)

if __name__== '__main__':
    numero=int(input("Introduce un numero"))
    DecimalABinario(numero)