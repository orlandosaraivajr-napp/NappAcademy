from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self,  **kwargs):
        self.profissao = kwargs.get('profissao', '')        
        super(ContaPoupanca, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 0)

    def saque(self, valor):
        if isinstance(valor, (float, int)):
            if valor > (self.saldo):
                raise ValueError('Valor do saque supera seu saldo.')
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')

    def rendimento_aniversario(self, juros):
         if juros < 0 or juros > 1:
            raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
         self.saldo += self.saldo * juros
