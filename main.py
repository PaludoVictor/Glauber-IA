import os
import cv2
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class Neuronio:
    """Classe que representa um neurônio para reconhecimento de números, armazenando pesos e processando imagens."""

    def importar_matriz(caminho):
        """Lê um arquivo de texto contendo uma matriz 28x28 de pesos e a converte em uma lista de inteiros."""
        a = open(caminho)
        b = a.readlines()
        matriz = []
        for c in b:
            c = c[1:-2]
            matriz.append(c.split(', '))
        for d in range(28):
            for e in range(28):
                matriz[d][e] = int(matriz[d][e])
        a.close()
        return matriz
    
    def calcular(neuronio, matriz_formatada, n_coluna, n_linha):
        """Calcula o valor do neurônio com base na matriz formatada e nas dimensões fornecidas."""
        valor = 0
        for a in range(28-n_linha, 28):
            for b in range(28-n_coluna, 28):
                if matriz_formatada[a][b] == 1:
                    valor += neuronio[a][b]
        return valor

    def __init__(self, arq_neuronio, matriz_formatada, n_coluna, n_linha):
        self.neuronio = Neuronio.importar_matriz(arq_neuronio)
        self.arq_neuronio = arq_neuronio
        self.matriz_formatada = matriz_formatada
        self.valor2 = Neuronio.calcular(self.neuronio, self.matriz_formatada, n_coluna, n_linha)

class Main:
    """Classe que processa imagens e realiza o reconhecimento de números usando neurônios."""

    def __init__(self, entr):
        """Inicializa o processamento da imagem e realiza o reconhecimento."""
        try:
            aaa = entr
            if not os.path.exists(aaa):
                Main.log = "Arquivo não encontrado"
                return
            a = cv2.imread(aaa, cv2.IMREAD_GRAYSCALE)
            if a is None:
                Main.log = "Formato de imagem inválido"
                return
            if a.shape != (28, 28):
                a = cv2.resize(a, (28, 28), interpolation=cv2.INTER_AREA)

            for x in range(28):
                for y in range(28):
                    if a[x][y] == 255:
                        a[x][y] -= 1

            Main.excluir_linha(a)
            Main.excluir_coluna(a)
            a, n_linhas, n_colunas = Main.alocar(a)
            matriz_de_resposta = []

            for b in range(10):
                for d in range(3):
                    neu = Neuronio(os.path.join(os.getcwd(), "neuronios", f"neuronio{b}_{d}.txt"), a, n_colunas, n_linhas)
                    matriz_de_resposta.append(neu.valor2)
            Main.log = str(matriz_de_resposta.index(max(matriz_de_resposta))//3)

        except TypeError:
            Main.log = "Endereço inválido"
        except Exception as e:
            Main.log = f"Erro: {str(e)}"

    def excluir_linha(matriz):
        """Remove linhas vazias ou irrelevantes da matriz da imagem."""
        for a in range(28):
            teste = True
            for b in range(28):
                if matriz[a][b] > 24 and matriz[a][b] != 255:
                    teste = False
            if teste:
                for c in range(28):
                    matriz[a][c] = 255
            else:
                break

        for a in range(27, -1, -1):
            teste = True
            for b in range(28):
                if matriz[a][b] > 24 and matriz[a][b] != 255:
                    teste = False
            if teste:
                for c in range(28):
                    matriz[a][c] = 255
            else:
                break
        return matriz
    
    def excluir_coluna(matriz):
        """Remove colunas vazias ou irrelevantes da matriz da imagem."""
        for a in range(28):
            teste = True
            for b in range(28):
                if matriz[b][a] > 24 and matriz[b][a] != 255:
                    teste = False
            if teste:
                for c in range(28):
                    matriz[c][a] = 255
            else:
                break

        for a in range(27, -1, -1):
            teste = True
            for b in range(28):
                if matriz[b][a] > 24 and matriz[b][a] != 255:
                    teste = False
            if teste:
                for c in range(28):
                    matriz[c][a] = 255
            else:
                break
    
    def definir_linhas(matriz):
        """Determina o número de linhas relevantes na matriz."""
        n_linha = 0
        lixo_linha = 0
        for a in range(28):
            count = 0
            for b in range(28):
                if matriz[a][b] != 255:
                    count += 1
            if count > 0:
                n_linha = count
                break
            lixo_linha += 1
        return n_linha, lixo_linha
    
    def definir_colunas(matriz):
        """Determina o número de colunas relevantes na matriz."""
        lixo_coluna = 0
        n_coluna = 0
        for a in range(28):
            count = 0
            for b in range(28):
                if matriz[b][a] != 255:
                    count += 1
            if count > 0:
                n_coluna = count
                break
            lixo_coluna += 1
        return n_coluna, lixo_coluna

    def alocar(matriz_formatada):
        """Reorganiza a matriz para centralizar o conteúdo relevante."""
        n_linha, lixo_coluna = Main.definir_colunas(matriz_formatada)
        n_coluna, lixo_linha = Main.definir_linhas(matriz_formatada)
        count_lin = 27
        count_col = 27
        n_coluna2 = n_coluna
        n_linha2 = n_linha 
        
        for a in range(n_linha):
            for b in range(n_coluna):
                if matriz_formatada[count_lin][count_col] != matriz_formatada[n_linha2-1+lixo_linha][n_coluna2-1+lixo_coluna]:
                    matriz_formatada[count_lin][count_col] = matriz_formatada[n_linha2-1+lixo_linha][n_coluna2-1+lixo_coluna]
                    matriz_formatada[n_linha2-1+lixo_linha][n_coluna2-1+lixo_coluna] = 255
                count_col -= 1
                n_coluna2 -= 1
            count_lin -= 1
            n_linha2 -= 1
            count_col = 27
            n_coluna2 = n_coluna

        for a in range(28):
            for b in range(28):
                try:
                    if 255 > matriz_formatada[a][b] > 24:
                        matriz_formatada[a][b] = 1
                    elif 255 > matriz_formatada[a][b]:
                        matriz_formatada[a][b] = 0
                except:
                    continue
        return matriz_formatada, n_linha, n_coluna

class Interface:
    """Classe que cria a interface gráfica para o projeto Glauber, permitindo carregar e reconhecer números em imagens."""

    def __init__(self):
        """Inicializa a janela principal e os elementos da interface."""
        self.janela = tk.Tk()
        self.janela.title("GLAUBER")
        self.janela.state('zoomed')  # Janela maximizada, como no original
        self.janela.configure(bg='black')

        # Título
        self.titulo_label = Label(self.janela, text="GLAUBER", font=('Arial', 40, 'bold'), bg='black', fg='white')
        self.titulo_label.place(relx=0.5, rely=0.05, anchor='n')

        # Área para exibir a imagem (esquerda)
        self.imagem_label = Label(self.janela, bg='black', width=400, height=400)
        self.imagem_label.place(relx=0.05, rely=0.3)

        # Área central para entrada e botões
        self.central_frame = Frame(self.janela, bg='black')
        self.central_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.entrada_label = Label(self.central_frame, text="Selecione uma imagem (28x28, fundo preto, número branco)", font=('Arial', 12), bg='black', fg='white')
        self.entrada_label.pack(pady=10)

        self.entrada_user = Entry(self.central_frame, width=50, font=('Arial', 12))
        self.entrada_user.pack(pady=10)

        self.botao_abrir_arquivo = Button(self.central_frame, text="Abrir Imagem", command=self.abrir_explorador, font=('Arial', 12), bg='white', fg='black', relief='raised', width=15)
        self.botao_abrir_arquivo.pack(pady=10)

        self.botao_verificar = Button(self.central_frame, text="Reconhecer Número", command=self.comando, font=('Arial', 12), bg='white', fg='black', relief='raised', width=15)
        self.botao_verificar.pack(pady=10)

        # Área para exibir o resultado (direita)
        self.resultado_label = Label(self.janela, text="", anchor='center', bg='black', fg='white', font=('Arial', 40), width=10, height=2)
        self.resultado_label.place(relx=0.75, rely=0.5, anchor='center')

        self.janela.mainloop()

    def comando(self):
        """Processa a imagem selecionada e exibe o número reconhecido."""
        self.pegar_entrada = self.entrada_user.get()
        Main(self.pegar_entrada)
        self.resultado_label.config(text=Main.log if Main.log.isdigit() else Main.log)

    def abrir_explorador(self):
        """Abre o explorador de arquivos para selecionar uma imagem."""
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if caminho_arquivo:
            self.entrada_user.delete(0, tk.END)
            self.entrada_user.insert(0, caminho_arquivo)

            imagem = Image.open(caminho_arquivo)
            imagem = imagem.resize((400, 400))  # Tamanho fixo, como no original
            imagem_tk = ImageTk.PhotoImage(imagem)
            self.imagem_label.config(image=imagem_tk)
            self.imagem_label.image = imagem_tk

Interface()