import random

class Reflector():
    # genera el reflector de nuestra máquina Enigma

    def __init__(self, abecedario = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"):
        
        random.seed(123)
        self.abecedario = abecedario
        self.conexiones = []
        pares_letras = []
        
        numeros = [i for i in range(len(abecedario))]
        subset = random.sample(numeros, len(abecedario))

        for numero in subset:
            letra = abecedario[numero]            
            pares_letras.append(letra)             
            if len(pares_letras) == 2:
                self.conexiones.append(tuple(pares_letras))
                pares_letras = []
    
    def refleja(self, letra_entrada):
        for tupla in self.conexiones:
            if letra_entrada in tupla[0]:
                return tupla[1]   
            elif letra_entrada in tupla[1]:
                return tupla[0]