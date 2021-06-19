import os
import glob
from projeto.Abstracao import *

def palavra_no_arquivo(palavra, arquivo):
    with open(arquivo, 'r') as f:
        for line in f:
            return palavra in line
    return False

def todos_arquivos_txt():
    looking_for = '**/*.txt'
    matched = glob.glob(looking_for, recursive=True)
    return matched

def encontrar_palavra(palavra):
    encontrado_em = []
    arquivos = todos_arquivos_txt()
    for arquivo in arquivos:
        if palavra_no_arquivo(palavra, arquivo):
            encontrado_em.append(arquivo)
    return encontrado_em

busca_napp1 = encontrar_palavra('napp')
busca_napp2 = encontrar_palavra('NaPp')
print(busca_napp1)
print(busca_napp2)
print(Abstracao(**{'metodo_de_busca':'sensitive', 'arquivo':'txt'}).procura_palavra('napp'))
print(Abstracao(**{'metodo_de_busca':'insensitive', 'arquivo':'txt'}).procura_palavra('NaPp'))