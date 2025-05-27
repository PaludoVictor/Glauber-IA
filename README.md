# Glauber - Reconhecimento de Dígitos com IA

**Glauber** é um projeto desenvolvido por alunos do IFSC - Campus Chapecó, durante a disciplina de Oficina de Integração II (2024). Foi apresentado na **Semana Nacional de Ciência e Tecnologia (SNCT)** e premiado com o **3º lugar** na categoria de projetos.

## 🧠 Sobre o projeto

O Glauber é uma inteligência artificial treinada para reconhecer dígitos de 0 a 9 em imagens de 28x28 pixels, com fundo preto e números em branco. Utilizamos Python e bibliotecas de aprendizado de máquina para treinar e testar a IA com conjuntos de dados similares ao MNIST.

## 🏆 Reconhecimento

O projeto conquistou o **3º lugar na SNCT 2024**, evento realizado no IFSC Campus Chapecó.

![Certificado](certificado_snct.pdf)

## 👥 Participantes

- João Vitor Boscatto Pierezan (Aluno)
- Luis Henrique Dos Santos (Aluno)
- Pedro Carbonari Prestes (Aluno)
- Samuel Luis Mittanck (Aluno)
- Victor MAier Paludo (Aluno)
- Prof. Fabiner de Melo Fugali (Orientador)

IFSC - Campus Chapecó
Disciplina: Oficina de Integração II - 2024

## 🧠 Descrição da Lógica

O **Glauber** é um projeto de Inteligência Artificial simples que reconhece dígitos de 0 a 9 a partir de imagens de **28x28 pixels**, com fundo preto e número branco.

### 🧩 Como funciona:

1. **Arquivos de neurônios**  
   Cada dígito (0 a 9) possui 3 arquivos `.txt`, cada um contendo uma matriz 28x28 com valores inteiros que funcionam como pesos.

2. **Processamento da imagem**  
   A imagem é:
   - Convertida para tons de cinza.
   - Redimensionada para 28x28 se necessário.
   - Limpa de bordas vazias (linhas e colunas sem conteúdo útil).
   - Centralizada e binarizada (1 para pixel ativo, 0 para fundo).

3. **Reconhecimento**  
   - Para cada número de 0 a 9, são utilizados 3 neurônios (totalizando 30 testes).
   - A imagem processada é comparada com cada neurônio.
   - Cada comparação gera um valor somando os pesos onde a imagem possui pixel ativo.
   - O número com o maior valor de ativação é o reconhecido e exibido.

4. **Interface Gráfica (Tkinter)**  
   - Interface intuitiva para carregar a imagem.
   - Exibe o número reconhecido na tela.


## 🚀 Como usar

### Requisitos

- Python 3.10+ instalado

### Passos

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/glauber-ai.git
cd glauber-ai


# Instale as dependências
pip install -r requirements.txt

# Rode o projeto
python main.py

```

## 📄 Licença
Este projeto é de livre uso para fins educacionais.
