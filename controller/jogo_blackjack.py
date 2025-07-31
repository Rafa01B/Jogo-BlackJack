from models.baralho import Baralho
from models.mao import Mao

class JogoBlackjack:
    def __init__(self):
        self.baralho = Baralho()
        self.mao_jogador = Mao()
        self.mao_dealer = Mao()
        self.jogo_terminado = False

    def iniciar_jogo(self):
        # Distribui 2 cartas para jogador e dealer
        self.mao_jogador.adicionar_carta(self.baralho.distribuir())
        self.mao_jogador.adicionar_carta(self.baralho.distribuir())

        self.mao_dealer.adicionar_carta(self.baralho.distribuir())
        self.mao_dealer.adicionar_carta(self.baralho.distribuir())

        self.jogo_terminado = False

    def turno_jogador_pedir_carta(self):
        if not self.jogo_terminado:
            carta = self.baralho.distribuir()
            self.mao_jogador.adicionar_carta(carta)
            return carta
        return None

    def pontos_jogador(self):
        return self.mao_jogador.calcular_pontos()

    def pontos_dealer(self):
        return self.mao_dealer.calcular_pontos()

    def turno_dealer(self):
        # Dealer compra enquanto tiver menos que 17
        while self.mao_dealer.calcular_pontos() < 17:
            carta = self.baralho.distribuir()
            self.mao_dealer.adicionar_carta(carta)

    def verificar_vencedor(self):
        pontos_j = self.pontos_jogador()
        pontos_d = self.pontos_dealer()

        print(f"DEBUG: pontos jogador = {pontos_j}, dealer = {pontos_d}")

        if pontos_j > 21:
            self.jogo_terminado = True
            print("DEBUG: Jogador estourou")
            return "Jogador estourou! Dealer vence."

        if pontos_j == 21 and len(self.mao_jogador.cartas) == 2:
            self.jogo_terminado = True
            print("DEBUG: Blackjack jogador")
            return "Blackjack! Jogador vence!"

        if pontos_d == 21 and len(self.mao_dealer.cartas) == 2:
            self.jogo_terminado = True
            print("DEBUG: Blackjack dealer")
            return "Blackjack! Dealer vence."

        if pontos_d > 21:
            self.jogo_terminado = True
            print("DEBUG: Dealer estourou")
            return "Dealer estourou! Jogador vence."

        self.jogo_terminado = True
        if pontos_j > pontos_d:
            print("DEBUG: Jogador venceu por pontos")
            return "Jogador venceu!"
        elif pontos_j < pontos_d:
            print("DEBUG: Dealer venceu por pontos")
            return "Dealer venceu!"
        else:
            print("DEBUG: Empate")
            return "Empate!"

    def mostrar_maos(self, revelar_dealer=False):
        jogador_str = ', '.join(str(c) for c in self.mao_jogador.cartas)
        if revelar_dealer:
            dealer_str = ', '.join(str(c) for c in self.mao_dealer.cartas)
            dealer_pts = self.pontos_dealer()
        else:
            dealer_str = f"{self.mao_dealer.cartas[0]}, ?"
            dealer_pts = "?"

        return f"Sua mão: {jogador_str} ({self.pontos_jogador()} pontos)\n" \
               f"Mão do dealer: {dealer_str} ({dealer_pts} pontos)"
