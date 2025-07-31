import random
from models.carta import Carta

class Baralho:
    def __init__(self):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        naipes = ['♠', '♥', '♦', '♣']
        self.cartas = [Carta(valor, naipe) for valor in valores for naipe in naipes]
        self.embaralhar()

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self):
        return self.cartas.pop() if self.cartas else None
