from leitorarquivo import LeitorArquivo

import os

def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    os.system("cls")
    print(valores)


main()