from enigma01 import Rotor, Reflector, Enigma

enigma = Enigma(mensaje = "Alan Turing", posRotorUno = "S", posRotorDos = "D", posRotorTres = "K")

print(enigma.codifica_mensaje())
