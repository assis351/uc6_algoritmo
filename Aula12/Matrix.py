import random
import time
import sys

# Script para stories: Efeito Matrix
# Copie e cole no terminal (funciona melhor no VS Code/Terminal Linux/Mac)

def efeito_matrix():
    # Caracteres que vão compor a "chuva"
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*"
    largura = 80
    
    # Cores ANSI
    verde = '\033[92m'
    brilhante = '\033[1m'
    reset = '\033[0m'
    
    print(verde + brilhante)
    
    try:
        while True:
            linha = ""
            for _ in range(largura):
                # Decide aleatoriamente se coloca um caractere ou espaço
                if random.random() > 0.95:
                    linha += random.choice(chars)
                else:
                    linha += " "
            print(linha)
            time.sleep(0.05) # Velocidade da chuva
    except KeyboardInterrupt:
        print(reset + "\nFim do efeito.")

if __name__ == "__main__":
    efeito_matrix()