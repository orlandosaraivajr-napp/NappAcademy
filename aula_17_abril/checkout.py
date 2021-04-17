class CheckoutStrategy:
    def calculo(self, valor_compra, dados):
        return valor_compra

class Cliente_outro_Strategy(CheckoutStrategy):
    def calculo(self, valor_compra, dados):
        return valor_compra * 0.75
    
class Cliente_estudante_Strategy(CheckoutStrategy):
    def calculo(self, valor_compra, dados):
        return valor_compra * 0.5

class Cliente_professor_Strategy(CheckoutStrategy):
    def calculo(self, valor_compra, dados):
        return valor_compra * 0.9
    
class Cliente_ouro_professor_Strategy(CheckoutStrategy):
    def calculo(self, valor_compra, dados):
        return valor_compra * 0.5

class cupom_napp_2121_Strategy(CheckoutStrategy):
    def calculo(self, valor_compra, dados):
        return valor_compra * 0.7
    
class cupom_napp_21_Strategy(CheckoutStrategy):
    def calculo(self, valor_compra, dados):
        return valor_compra * 0.8
    
class SemDescontoStrategy(CheckoutStrategy):
    def calculo(self, valor_compra, dados):
        return valor_compra

class CarrinhoCompra:
    def checkout(self, valor_compra, dados, estrategia):
        if issubclass(type(estrategia), CheckoutStrategy):
            return estrategia.calculo(valor_compra, dados)
        else:
            return 'Deu ruim'


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
estrategia = 'String não estratégia'
assert(carrinho.checkout(1000, dados, estrategia) == 'Deu ruim')



estrategia = SemDescontoStrategy()
dados.cartao = 'ouro'
dados.profissao = 'professor'
estrategia = Cliente_ouro_professor_Strategy()
assert(carrinho.checkout(1000, dados, estrategia) == 500)
estrategia = SemDescontoStrategy()
assert(carrinho.checkout(1000, dados, estrategia) == 1000)
estrategia = Cliente_professor_Strategy()
dados.profissao = 'professor'
assert(carrinho.checkout(1000, dados, estrategia) == 900)
dados.profissao = 'estudante'
estrategia = Cliente_estudante_Strategy()
assert(carrinho.checkout(1000, dados, estrategia) == 500)
dados.profissao = None
dados.cupom = 'napp2021'
estrategia = cupom_napp_2121_Strategy()
assert(carrinho.checkout(1000, dados, estrategia) == 700)
dados.cupom = 'napp21'
estrategia = cupom_napp_21_Strategy()
assert(carrinho.checkout(1000, dados, estrategia) == 800)
dados.cupom = None
dados.cartao = 'ouro'
estrategia = Cliente_outro_Strategy()
assert(carrinho.checkout(1000, dados, estrategia) == 750)

