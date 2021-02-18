import random

class Rotor():

    def __init__(self, abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):

        self.abecedario = abecedario
        self.rotor = []
        self.rotorC = self.rotor[:]
        otrasLetras = self.abecedario

        for letra in self.abecedario:
            n = random.randrange(len(otrasLetras))
            self.rotor.append((letra, otrasLetras[n]))
            otrasLetras = otrasLetras[:n] + otrasLetras[(n+1):]

    def code(self, letra):
        posLetra = self.abecedario.index(letra)
        Lcode = self.rotorC[posLetra][1]
        self.rotar()
        return Lcode         

    def initialPos(self, letra):
            position = self.abecedario.index(letra)
            self.rotorC = self.rotor[position:] + self.rotor[:position]

    def rotar(self):
        self.rotorC = self.rotorC[1:] + self.rotorC[0 : 1]

