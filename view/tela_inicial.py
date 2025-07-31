import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from view.interface_tk import InterfaceBlackjack

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack 21 - Menu")
        self.root.geometry("600x400")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#121212')
        style.configure('Titulo.TLabel', font=('Segoe UI Black', 28), foreground='#FFD700', background='#121212')
        style.configure('TButton', font=('Segoe UI', 18, 'bold'), padding=15)

        self.frame = ttk.Frame(root, padding=30)
        self.frame.pack(expand=True)

        self.label_titulo = ttk.Label(self.frame, text="Bem-vindo ao Blackjack 21", style='Titulo.TLabel')
        self.label_titulo.pack(pady=(0, 40))

        self.btn_iniciar = ttk.Button(self.frame, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.btn_iniciar.pack(ipadx=20, ipady=10)

        self.btn_sair = ttk.Button(self.frame, text="Sair", command=self.root.quit)
        self.btn_sair.pack(pady=20, ipadx=20, ipady=10)

    def iniciar_jogo(self):
        self.root.withdraw()  # esconde a tela inicial
        janela_jogo = tk.Toplevel()
        InterfaceBlackjack(janela_jogo)
        janela_jogo.protocol("WM_DELETE_WINDOW", self.fechar_jogo)

    def fechar_jogo(self):
        self.root.deiconify()  # mostra a tela inicial novamente
        

if __name__ == "__main__":
    root = tk.Tk()
    TelaInicial(root)
    root.mainloop()
