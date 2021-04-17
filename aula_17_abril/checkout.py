class CarrinhoCompra:
    def checkout(self, valor_compra, cartao_fidelidade, profissao, cupom):
        if cartao_fidelidade == 'ouro' and profissao == 'professor':
            return valor_compra * 0.5
        if profissao == 'professor':
            return valor_compra * 0.9
        if profissao == 'estudante':
            return valor_compra * 0.5
        if cartao_fidelidade == 'ouro':
            return valor_compra * 0.75
        if cupom == 'napp2021':
            return valor_compra * 0.7
        if cupom == 'napp21':
            return valor_compra * 0.8
        return valor_compra


carrinho = CarrinhoCompra()
assert(carrinho.checkout(1000, None, None, None) == 1000)
assert(carrinho.checkout(1000, None, 'professor', None) == 900)
assert(carrinho.checkout(1000, None, 'estudante', None) == 500)
assert(carrinho.checkout(1000, None, None, 'napp2021') == 700)
assert(carrinho.checkout(1000, None, None, 'napp21') == 800)
assert(carrinho.checkout(1000, 'ouro', None, None) == 750)
assert(carrinho.checkout(1000, 'ouro', 'professor', None) == 500)
