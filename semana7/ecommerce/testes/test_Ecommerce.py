from ecommerce.classes.Ecommerce import Loja
import pytest

class TestEcommerce:
    def test_class_declared(self):
        objeto = Loja('Lojão Tabajara')
        assert isinstance(objeto, Loja)

    def test_instanciar(self):
        objeto = Loja('Lojão Tabajara')
        assert objeto.nome, 'Lojão Tabajara'

    def test_setters(self):
        objeto = Loja('Lojão Tabajara')
        assert objeto.nome == 'Lojão Tabajara'
        objeto.nome = 'Lojão Tabajara Centro'
        assert objeto.nome == 'Lojão Tabajara Centro'
        assert objeto.estoque  == []

    def test_str_repr(self):
        objeto = Loja('Lojão Tabajara')
        assert str(objeto) == 'Lojão Tabajara'
        assert repr(objeto) == 'Nome da Loja => Lojão Tabajara'

    def test_metodo_add_estoque_ok(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('12345678911', 15, 1)
        assert len(loja.estoque) == 1

    def test_metodo_add_estoque_ok2(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('12345678911', 15, 3)
        loja.add_estoque('123', 12, 5)
        assert len(loja.estoque) == 8

    def test_quantidade_produtos(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 10)
        loja.add_estoque('1234', 20, 5)
        loja.add_estoque('12345', 20, -1)
        loja.add_estoque('123456', 20, 0)
        assert loja.quantidade_produtos('123') == 10
        assert loja.quantidade_produtos('1234') == 5
        assert loja.quantidade_produtos('12345') == 0
        assert loja.quantidade_produtos('123456') == 0

    def test_metodo_comprar_ok(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 3)
        assert len(loja.estoque) == 3
        loja.comprar('123')
        assert len(loja.estoque) == 2

    def test_metodo_comprar_sem_produto(self):
        loja = Loja('Lojão Tabajara')
        assert loja.comprar('9999999') is None

    def test_metodo_comprar_ok2(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 1)
        assert len(loja.estoque) == 1
        loja.comprar('123')
        assert len(loja.estoque) == 0
        assert loja.comprar('123') is None

