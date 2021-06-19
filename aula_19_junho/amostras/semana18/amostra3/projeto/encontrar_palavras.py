import glob


def palavra_no_arquivo(palavra, arquivo, case_sensitive=False):
    with open(arquivo, 'r') as f:
        if not case_sensitive:
            for line in f:
                return palavra.lower() in line.lower()
        else:
            for line in f:
                return palavra in line
    return False


def encontrar_palavra(palavra, case=True):
    encontrado_em = []
    try:
        arquivos_ext = [glob.glob(f'**/*{type}', recursive=True) for type in ['.txt', '.csv']]
        arquivos = arquivos_ext[0] + arquivos_ext[1]
    except:
        print('Não foram encontrados arquivos com as extensões txt ou csv')
        return

    if case:
        for arquivo in arquivos:
            if palavra_no_arquivo(palavra, arquivo, case_sensitive=True):
                encontrado_em.append(arquivo)
        return encontrado_em

    for arquivo in arquivos[0]:
        if palavra_no_arquivo(palavra, arquivo):
            encontrado_em.append(arquivo)
    return encontrado_em


busca_napp1 = encontrar_palavra('napp')
print(busca_napp1)

busca_napp2 = encontrar_palavra('NaPp', case=True)
print(busca_napp2)
