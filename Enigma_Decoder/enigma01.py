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

class Enigma():
    # une todas las partes de nuestra máquina

    def __init__(self, mensaje = "Alan Turing", posRotorUno = "A", posRotorDos = "B", posRotorTres = "C", abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.rotorUno = Rotor(abecedario = abecedario)
        self.rotorUno.initialPos(posRotorUno)
        self.rotorDos = Rotor(abecedario = abecedario, nRotor = 2)
        self.rotorDos.initialPos(posRotorDos)
        self.rotorTres = Rotor(abecedario = abecedario, nRotor = 3)
        self.rotorTres.initialPos(posRotorTres)
        # genera los tres rotores de nuestra máquina con sus posiciones iniciales respectivas y los abecedarios que van a utilizar
        self.reflector = Reflector()
        self.mensaje = mensaje


    def codifica_mensaje(self):
        
        codedMessage = ""

        for caracter in self.mensaje.upper():
            if caracter == " ":
                codedMessage += " "
            else:
                L1 = self.rotorTres.code_Mid01(self.rotorDos.code_Mid01(self.rotorUno.code_Init(caracter)))       
                L2 = self.reflector.refleja(L1)
                L3 = self.rotorUno.code_End(self.rotorDos.code_Mid02(self.rotorTres.code_Mid02(L2)))
                codedMessage += L3
                self.rotorUno.cuenta_vueltas()
                self.rotorDos.cuenta_vueltas()
                self.rotorTres.cuenta_vueltas()

            
        return codedMessage
