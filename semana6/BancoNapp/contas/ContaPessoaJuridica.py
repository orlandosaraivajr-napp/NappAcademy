from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    def __init__(self,  **kwargs):
        self.profissao = kwargs.get('profissao', '')        
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 1500)
        self.empresa = kwargs.get('empresa', '')

