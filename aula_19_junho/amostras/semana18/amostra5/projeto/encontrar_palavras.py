import os
import glob

user_ext = input("Qual extensão de arquivo deseja buscar?: ")
user_word = input("Qual palavra deseja buscar?: ")
case_sensitive = input("Considerar maiúsculas e minúsculas? [S] ou [N]: ")

if str(case_sensitive).lower() == 'n':
    user_word.lower()

def palavra_no_arquivo(palavra, arquivo):
    with open(arquivo, 'r') as f:
        for line in f:
            if str(case_sensitive).lower() != 'n':
                return palavra in line
            else:                
                return palavra in line.lower()
    return False

def todos_arquivos():
    looking_for = f'**/*.{user_ext}'
    matched = glob.glob(looking_for, recursive=True)
    return matched

def encontrar_palavra(palavra):
    encontrado_em = []
    arquivos = todos_arquivos()
    for arquivo in arquivos:
        if palavra_no_arquivo(palavra, arquivo):
            encontrado_em.append(arquivo)
    return encontrado_em

busca_palavra = encontrar_palavra(user_word)

print(busca_palavra)