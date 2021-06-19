from projeto.Arquivo import ArquivoCSV, ArquivoTXT
from projeto.Busca import BuscaInsensitive, BuscaSensitive

metodos_de_busca = {
    'sensitive': BuscaSensitive(),
    'insensitive':BuscaInsensitive()
}
arquivos = {
    'txt':ArquivoTXT(),
    'csv':ArquivoCSV()
}

class Abstracao:
    def __init__(self, **kwargs):
        try:
            self.metodo_de_busca = metodos_de_busca[kwargs['metodo_de_busca'].lower()]
        except KeyError:
            raise Exception('Metodo de busca não implementado')
        try:
            self.arquivo = arquivos[kwargs['arquivo'].lower()]
        except KeyError:
            raise Exception('Formato de relatório não implementado')
    

    def procura_palavra(self, palavra):
        lista_de_arquivos = self.arquivo.pega_arquivos()
        encontrado_em = []        
        for arquivo in lista_de_arquivos:
            if self.metodo_de_busca.busca_palavra(arquivo, palavra):
                encontrado_em.append(arquivo)
        return encontrado_em