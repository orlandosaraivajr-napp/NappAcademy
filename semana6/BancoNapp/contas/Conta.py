class Conta:
    def __init__(self, **kwargs):
        """
        Construtor da classe Conta.
        Recebe por kwargs :
        - nome
        - limite
        - saldo

        Raises:
            ValueError: Caso o saldo seja menor ou igual a zero.
        """
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        self.saldo = 0
        saldo = kwargs.get('saldo', self.saldo)
        if saldo < 0:
            raise ValueError('Saldo negativo')
        self.saldo = saldo
        self.extrato.append(('I', saldo))
