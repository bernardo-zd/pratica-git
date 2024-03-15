from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    os.system("cls")
    print(valores)
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    plt.title('Gráfico de linhas')
    plt.plot(valores)
    plt.show()


main()