from BancoNapp.contas.Conta import Conta
import pytest


class TestConta:
    """ Teste para a classe Conta """
    def test_class_declared(self):
        objeto = Conta()
        assert isinstance(objeto, Conta)

    def test_instanciar_objeto_somente_nome(self):
        objeto = Conta(nome='John Doe')
        assert objeto.nome, 'John Doe'
        assert objeto.saldo == 0
        assert objeto.limite == 500

    def test_instanciar_objeto_saldo_negativo(self):
        with pytest.raises(ValueError) as error:
            objeto = Conta(saldo=-20)
            assert objeto.nome, ''
            assert objeto.saldo == 0
            assert objeto.limite == 500
        assert str(error.value) == 'Saldo negativo'
