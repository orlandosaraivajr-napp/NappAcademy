from abc import ABC, abstractmethod


class Relatorios(ABC):
    @abstractmethod
    def criar_relatorio(self, lista):
        pass


class Relatorio_TXT(Relatorios):
    def criar_relatorio(self, lista, nome_arquivo):
        nome_arquivo = nome_arquivo + '.txt'
        with open(nome_arquivo, "w") as f:
            f.write('Relatório de Vendas\n')
            f.write(40 * '*' + '\n')
            f.write("DATA\t\t\t\t VALOR\n")
            for i in lista:
                f.write(str(i[0]) + 8 * " ")
                f.write(str(i[1]) + 7 * " ")
                f.write('\n')
            return True
