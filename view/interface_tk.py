import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from controller.jogo_blackjack import JogoBlackjack

class InterfaceBlackjack:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack 🃏")
        self.root.geometry("900x600")
        self.root.state('zoomed')
        self.root.minsize(700, 500)
        self.root.configure(bg="#121212")

        self.jogo = JogoBlackjack()
        self.jogo.iniciar_jogo()
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0

        self.imagens_cartas = {}
        self.carregar_imagens()

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#121212')
        self.style.configure('TLabel', background='#121212', foreground='#FFD700', font=('Segoe UI', 14))
        self.style.configure('Titulo.TLabel', font=('Segoe UI Black', 36), foreground='#FFD700', background='#121212')
        self.style.configure('Placar.TLabel', font=('Segoe UI', 16))
        self.style.configure('TButton', font=('Segoe UI', 14, 'bold'), padding=10)

        # Layout frames
        self.frame_principal = ttk.Frame(root, padding=20)
        self.frame_principal.pack(fill='both', expand=True)

        self.label_titulo = ttk.Label(self.frame_principal, text="Blackjack 21", style='Titulo.TLabel')
        self.label_titulo.pack(pady=(0, 25))

        self.frame_maos = ttk.Frame(self.frame_principal)
        self.frame_maos.pack(fill='x', expand=True)

        self.frame_jogador = ttk.LabelFrame(self.frame_maos, text="Sua mão", padding=15)
        self.frame_jogador.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        self.frame_dealer = ttk.LabelFrame(self.frame_maos, text="Mão do dealer", padding=15)
        self.frame_dealer.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        self.frame_botoes = ttk.Frame(self.frame_principal)
        self.frame_botoes.pack(pady=15)

        self.btn_pedir = ttk.Button(self.frame_botoes, text="🃏 Pedir Carta", command=self.pedir_carta)
        self.btn_pedir.pack(side='left', padx=20)

        self.btn_parar = ttk.Button(self.frame_botoes, text="⏹️ Parar", command=self.parar)
        self.btn_parar.pack(side='left', padx=20)

        self.btn_nova_rodada = ttk.Button(self.frame_botoes, text="🔄 Nova Rodada", command=self.nova_rodada)
        self.btn_nova_rodada.pack(side='left', padx=20)
        self.btn_nova_rodada.config(state='disabled')

        self.label_placar = ttk.Label(self.frame_principal, text="Vitórias: 0 | Derrotas: 0 | Empates: 0",
                                     style='Placar.TLabel')
        self.label_placar.pack(pady=10)

        self.atualizar_interface()
        self.habilitar_botoes(True)

    def carregar_imagens(self):
        base = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cartas')
        valores = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', 'J':'jack', 'Q':'queen', 'K':'king', 'A':'ace'}
        naipes = {'♠':'spades', '♥':'hearts', '♦':'diamonds', '♣':'clubs'}

        for v in valores:
            for n in naipes:
                nome = f"{valores[v]}_of_{naipes[n]}.png"
                caminho = os.path.join(base, nome)
                if os.path.exists(caminho):
                    img = Image.open(caminho).resize((80,120))
                    self.imagens_cartas[f"{v}{n}"] = ImageTk.PhotoImage(img)

        verso_path = os.path.join(base, 'back.png')
        if not os.path.exists(verso_path):
            verso_path = os.path.join(base, 'back_red.png')
        if os.path.exists(verso_path):
            img = Image.open(verso_path).resize((80,120))
            self.imagens_cartas['verso'] = ImageTk.PhotoImage(img)

    def atualizar_interface(self, revelar_dealer=False):
        for widget in self.frame_jogador.winfo_children():
            widget.destroy()
        for widget in self.frame_dealer.winfo_children():
            widget.destroy()

        for carta in self.jogo.mao_jogador.cartas:
            chave = f"{carta.valor}{carta.naipe}"
            img = self.imagens_cartas.get(chave)
            if img:
                lbl = ttk.Label(self.frame_jogador, image=img)
                lbl.image = img
                lbl.pack(side='left', padx=5)

        for idx, carta in enumerate(self.jogo.mao_dealer.cartas):
            if not revelar_dealer and idx > 0:
                img = self.imagens_cartas.get('verso')
            else:
                chave = f"{carta.valor}{carta.naipe}"
                img = self.imagens_cartas.get(chave)
            if img:
                lbl = ttk.Label(self.frame_dealer, image=img)
                lbl.image = img
                lbl.pack(side='left', padx=5)

    def habilitar_botoes(self, habilitar: bool):
        estado = 'normal' if habilitar else 'disabled'
        self.btn_pedir.config(state=estado)
        self.btn_parar.config(state=estado)

    def atualizar_placar(self):
        self.label_placar.config(text=f"Vitórias: {self.vitorias} | Derrotas: {self.derrotas} | Empates: {self.empates}")

    def pedir_carta(self):
        carta = self.jogo.turno_jogador_pedir_carta()
        self.atualizar_interface()

        pontos = self.jogo.pontos_jogador()

        if pontos > 21:
            self.habilitar_botoes(False)
            self.atualizar_interface(revelar_dealer=True)
            messagebox.showinfo("Fim de jogo", "Você estourou! Dealer vence.")
            self.derrotas += 1
            self.atualizar_placar()
            self.btn_nova_rodada.config(state='normal')

        elif pontos == 21 and len(self.jogo.mao_jogador.cartas) == 2:
            self.habilitar_botoes(False)
            self.atualizar_interface(revelar_dealer=True)
            messagebox.showinfo("Fim de jogo", "Blackjack! Você venceu!")
            self.vitorias += 1
            self.atualizar_placar()
            self.btn_nova_rodada.config(state='normal')

    def parar(self):
        self.jogo.turno_dealer()
        resultado = self.jogo.verificar_vencedor()
        self.atualizar_interface(revelar_dealer=True)
        self.habilitar_botoes(False)
        messagebox.showinfo("Resultado", resultado)

        resultado_lower = resultado.lower()
        if "jogador vence" in resultado_lower or "jogador venceu" in resultado_lower:
            self.vitorias += 1
        elif "dealer vence" in resultado_lower or "dealer venceu" in resultado_lower:
            self.derrotas += 1
        elif "empate" in resultado_lower:
            self.empates += 1

        self.atualizar_placar()
        self.btn_nova_rodada.config(state='normal')

    def nova_rodada(self):
        self.jogo = JogoBlackjack()
        self.jogo.iniciar_jogo()
        self.habilitar_botoes(True)
        self.atualizar_interface()
        self.btn_nova_rodada.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    InterfaceBlackjack(root)
    root.mainloop()
