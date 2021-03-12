from ecommerce.classes.Produto import Produto
import pytest


class TestProduto:
    def test_class_declared(self):
        objeto = Produto()
        assert isinstance(objeto, Produto)

    def test_instanciar_objeto_somente_ean(self):
        objeto = Produto(ean='12345678911')
        assert objeto.ean, '12345678911'
        assert objeto._preco == 0

    def test_instanciar_objeto_preco_negativo(self):
        with pytest.raises(ValueError) as error:
            Produto(ean='12345678911', preco=-1)
        assert str(error.value) == 'Preço negativo'

    def test_setters(self):
        objeto = Produto(ean='123')
        assert objeto.ean == '123'
        assert objeto.preco == 0
        objeto.preco = 100
        assert objeto.preco == 100

    def test_str_repr(self):
        objeto = Produto(ean='123')
        assert str(objeto) == '123'
        assert repr(objeto) == 'Produto:123'
