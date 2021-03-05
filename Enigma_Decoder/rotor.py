import random

class Rotor():
    def __init__(self, abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", nRotor = 1):

        random.seed(123)
        self.abecedario = abecedario # introduce en nuestra máquina Enigma el abecedario a utilizar (default: Español)
        self.nRotor = nRotor
        self.rotor = []
        self.__Lcount = 0
        otrasLetras = self.abecedario

        for letra in self.abecedario:
            n = random.randrange(len(otrasLetras))
            self.rotor.append((letra, otrasLetras[n]))
            otrasLetras = otrasLetras[:n] + otrasLetras[(n+1):]
        # recorre nuestro abecedario letra a letra y añade a la lista(rotor) una tupla (letra: letra al azar de entre otrasLetras)

        self.rotorC = self.rotor[:]
        # copia nuestro rotor para poder rotarlo sin modificar el original
    
    def code_Init(self, letra):
        
        if letra not in self.abecedario:
            raise ValueError("{} no pertenece al abecedario".format(letra)) 
        else:
            posLetra = self.abecedario.index(letra)
            Lcode = self.rotorC[posLetra][1]
            return Lcode

    def code_Mid01(self, letra):

        for tupla in self.rotorC:
            if letra == tupla[0]:
                posLetra = self.rotorC.index(tupla)
                Lcode = self.rotorC[posLetra][1]
                return Lcode

    def code_Mid02(self, letra):

        for tupla in self.rotorC:
            if letra == tupla[1]:
                posLetra = self.rotorC.index(tupla)
                Lcode = self.rotorC[posLetra][0]
                return Lcode

    def code_End(self, letra):

        for tupla in self.rotorC:
            if letra == tupla[1]:
                posLetra = self.rotorC.index(tupla)
                Lcode = self.abecedario[posLetra]
                return Lcode

    def cuenta_vueltas(self):
        self.__Lcount += 1
        if self.nRotor == 1:
            self.rotar()
        elif self.nRotor != 1:
            if self.__Lcount < len(self.abecedario):
                pass
            elif self.__Lcount == len(self.abecedario)**(self.nRotor - 1):
                self.__Lcount = 0 
                self.rotar()

    def rotar(self):
            self.rotorC = self.rotorC[1:] + self.rotorC[0 : 1]
            # rota una posición el rotor

    def initialPos(self, letra):
            position = self.abecedario.index(letra)
            self.rotorC = self.rotor[position:] + self.rotor[:position]
        # fija la posición inicial de nuestro rotor