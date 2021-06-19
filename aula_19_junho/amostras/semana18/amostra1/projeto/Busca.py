from abc import ABC, abstractmethod


class Busca:

    @abstractmethod
    def busca_palavra(self, arquivo, palavra):
        pass


class BuscaInsensitive(Busca):

    def busca_palavra(self, arquivo, palavra):
        with open(arquivo, 'r') as f:
            for line in f:
                line_insensitve = line.upper()
                return palavra.upper() in line_insensitve
        return False

class BuscaSensitive(Busca):

    def busca_palavra(self, arquivo, palavra):
        with open(arquivo, 'r') as f:
            for line in f:
                return palavra in line
        return False