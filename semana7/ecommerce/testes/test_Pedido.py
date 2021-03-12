from ecommerce.classes.Pedido import Pedido
from ecommerce.classes.Cliente import Cliente
from ecommerce.classes.Produto import Produto
import pytest


class TestPedido:
    def test_class_declared(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        assert isinstance(pedido, Pedido)
        assert pedido.itens == []

    def test_class_declared_fail(self):
        msg_erro = 'Não é possível instanciar um Pedido sem um cliente'
        with pytest.raises(TypeError) as error:
            Pedido('José da Silva')
        assert str(error.value) == msg_erro

    def test_str_repr(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        assert str(pedido) == 'Pedido de José da Silva'
        assert repr(pedido) == 'Pedido de José da Silva'

    def test_properties(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        assert pedido.cliente.nome == 'José da Silva'
        assert pedido.itens == []
        pedido.itens = [1]
        assert pedido.itens == [1]

    def test_metodo_add_item(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        produto = Produto(ean='12345678911')
        produto2 = Produto(ean='123546')
        pedido.add_item(produto)
        pedido.add_item(produto2)
        assert len(pedido.itens) == 2

    def test_metodo_add_item_fail(self):
        msg_erro = 'Não foi passado um objeto produto'
        with pytest.raises(TypeError) as error:
            cliente = Cliente('José da Silva')
            pedido = Pedido(cliente)
            pedido.add_item('string não produto')
        assert str(error.value) == msg_erro

    def test_quantidade_produto_no_pedido(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        pedido.add_item(Produto(ean='123'))
        pedido.add_item(Produto(ean='123546'))
        pedido.add_item(Produto(ean='123'))
        pedido.add_item(Produto(ean='123'))
        assert pedido.quantidade_produto_no_pedido('123') == 3
        assert pedido.quantidade_produto_no_pedido('123546') == 1
        assert pedido.quantidade_produto_no_pedido('9999') == 0

    def test_nota_fiscal(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        pedido.add_item(Produto(ean='123', preco=10))
        pedido.add_item(Produto(ean='123546', preco=5))
        pedido.add_item(Produto(ean='123', preco=10))
        nota_fiscal = pedido.nota_fiscal()
        assert len(nota_fiscal) == 2
        assert type(nota_fiscal[0]) == tuple

    def test_valor_total_pagar(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        pedido.add_item(Produto(ean='123', preco=20))
        pedido.add_item(Produto(ean='1234', preco=40))
        assert pedido.valor_total_pagar() == 60

    def test_valor_total_pagar_vazio(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        assert pedido.valor_total_pagar() == 0

    def test_checkout(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        pedido.add_item(Produto(ean='123', preco=10))
        pedido.add_item(Produto(ean='123546', preco=5))
        pedido.add_item(Produto(ean='123', preco=10))
        checkout = pedido.checkout('dinheiro')
        assert len(checkout) == 2
        assert checkout[1] == 25

    def test_checkout_fail(self):
        msg_erro = 'Forma de pagamento não aceita'
        with pytest.raises(Exception) as error:
            cliente = Cliente('José da Silva')
            pedido = Pedido(cliente)
            produto1 = Produto(ean='123', preco=10)
            pedido.add_item(produto1)
            pedido.checkout('marcar')
        assert str(error.value) == msg_erro

    def test_checkout_fail2(self):
        msg_erro = 'Informe um meio de pagamento'
        with pytest.raises(Exception) as error:
            pedido = Pedido(Cliente('José da Silva'))
            pedido.add_item(Produto(ean='123', preco=10))
            pedido.checkout()
        assert str(error.value) == msg_erro
