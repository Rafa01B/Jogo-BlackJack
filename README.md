# 🃏 Blackjack 21

---

## 📅 Sumário

* [Descrição](#descrição)
* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Instalação](#instalação)
* [Uso](#uso)
* [Tela Inicial](#tela-inicial)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Contato](#contato)

---

## 🔎 Descrição

O objetivo é simples: vencer o dealer fazendo o maior número de pontos possível, sem ultrapassar 21.
A interface permite partidas dinâmicas com cartas visuais e contagem de vitórias.

---

## 🎯 Funcionalidades

* Interface moderna com **imagens reais** das cartas.
* Lógica completa do jogo **Blackjack 21**.
* **Placar** de vitórias, derrotas e empates.
* Tela inicial com instruções.
* Suporte a **rodadas consecutivas**.

---

## 🤝 Tecnologias Utilizadas

* [Python 3.10+](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Pillow](https://pillow.readthedocs.io/) 

---

## 🚀 Instalação

1. Clone o repositório:

```bash
https://github.com/Rafa01B/Jogo-BlackJack
cd blackjack
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o jogo:

```bash
python main.py
```

---

## 🚚 Uso

* **🃏 Pedir Carta**: Recebe uma nova carta.
* **⏹️ Parar**: Finaliza seu turno, dealer joga.
* **🔄 Nova Rodada**: Inicia novo jogo após o fim da rodada.

---

## 📄 Tela Inicial

Após iniciar com `main.py`, você verá uma tela com:

* Título do jogo
* Instruções rápidas
* Botão **"Iniciar Jogo"**

A partir dela, o jogo é iniciado.

---

## 📁 Estrutura do Projeto

```
blackjack-python/
├── assets/
│   └── cartas/                  # Imagens das cartas
├── controller/
│   └── jogo_blackjack.py        # Lógica principal do jogo
├── models/
│   ├── baralho.py               # Baralho e embaralhamento
│   └── mao.py                   # Mão do jogador e dealer
├── view/
│   ├── interface_tk.py          # Interface gráfica
│   └── tela_inicial.py  
├── main.py                      # Tela inicial do jogo
├── requirements.txt             # Dependências do projeto
└── README.md                    # Este arquivo
```

---

## 📢 Contato

Desenvolvido por [Rafaela Bezerra Rodrigues](https://github.com/Rafa01B).
Email: [rafaelabezerra133@gmail.com](rafaelabezerra133@gmail.com)
