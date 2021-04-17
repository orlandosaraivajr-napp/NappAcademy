class CheckoutStrategy:
    def calculo(self, valor_compra, dados):
        if dados.cartao == 'ouro' and dados.profissao == 'professor':
            return valor_compra * 0.5
        if dados.profissao == 'professor':
            return valor_compra * 0.9
        if dados.profissao == 'estudante':
            return valor_compra * 0.5
        if dados.cartao == 'ouro':
            return valor_compra * 0.75
        if dados.cupom == 'napp2021':
            return valor_compra * 0.7
        if dados.cupom == 'napp21':
            return valor_compra * 0.8
        return valor_compra

class CarrinhoCompra:
    def checkout(self, valor_compra, dados):
        checkout = CheckoutStrategy()
        return checkout.calculo(valor_compra, dados)

class DadosCliente:
    def __init__(self):
        self._cartao_fidelidade = None
        self._profissao = None
        self._cupom = None
    
    @property
    def cartao(self):
        return self._cartao_fidelidade

    @cartao.setter
    def cartao(self, value):
        self._cartao_fidelidade = value
    
    @property
    def profissao(self):
        return self._profissao

    @profissao.setter
    def profissao(self, value):
        self._profissao = value

    @property
    def cupom(self):
        return self._cupom

    @cupom.setter
    def cupom(self, value):
        self._cupom = value


carrinho = CarrinhoCompra()
dados = DadosCliente()
assert(carrinho.checkout(1000, dados) == 1000)
dados.profissao = 'professor'
assert(carrinho.checkout(1000, dados) == 900)
dados.profissao = 'estudante'
assert(carrinho.checkout(1000, dados) == 500)
dados.profissao = None
dados.cupom = 'napp2021'
assert(carrinho.checkout(1000, dados) == 700)
dados.cupom = 'napp21'
assert(carrinho.checkout(1000, dados) == 800)
dados.cupom = None
dados.cartao = 'ouro'
assert(carrinho.checkout(1000, dados) == 750)
dados.cartao = 'ouro'
dados.profissao = 'professor'
assert(carrinho.checkout(1000, dados) == 500)
