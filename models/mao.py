class Mao:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def calcular_pontos(self):
        pontos = 0
        ases = 0
        for carta in self.cartas:
            val = carta.valor_numerico()
            pontos += val
            if carta.valor == 'A':
                ases += 1

        # Ajusta Ás de 11 para 1 se estourar
        while pontos > 21 and ases:
            pontos -= 10
            ases -= 1

        return pontos

    def __repr__(self):
        return f"{self.cartas}"
