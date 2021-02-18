class Reflector():

    def __init__(self, conf = ["ABCDEFGHIJKLNÑMOPQRSTUVWXYZ", "ZYXWVUTSRQPOMÑNLKJIHGFEDCBA"]):
        self.configuracion = conf

    def refleja(self, letra_entrada):
        posE = self.configuracion[0].index(letra_entrada)
        return self.configuracion[1][posE]