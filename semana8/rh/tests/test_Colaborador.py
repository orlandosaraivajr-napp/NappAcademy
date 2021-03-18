from rh.classes.Colaborador import Colaborador
from datetime import date, timedelta
import pytest


class TestColaborador:
    def test_class_declared(self):
        objeto = Colaborador('John Doe', 15, 4, 1995)
        assert isinstance(objeto, Colaborador)

    def test_class_declared_fail(self):
        msg_erro = "Informe dia, mês e ano"
        with pytest.raises(TypeError) as error:
            Colaborador('John Doe')
        assert str(error.value) == msg_erro

    def test_instanciar(self):
        objeto = Colaborador('José da Silva', 20, 10, 2000)
        assert objeto.nome, 'José da Silva'
        assert objeto.aniversario, '2000-10-20'

    def test_str_repr(self):
        pessoa = Colaborador('José da Silva', 15, 4, 1995)
        assert str(pessoa) == 'José da Silva'
        assert repr(pessoa) == 'Colaborador: José da Silva'

    def test_setters(self):
        pessoa = Colaborador('José da Silva', 15, 4, 1995)
        assert pessoa.nome == 'José da Silva'
        pessoa.nome = 'José da Silva Júnior'
        assert pessoa.nome == 'José da Silva Júnior'

    def test_aniversario_hoje(self):
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        pessoa1 = Colaborador('Birth', hoje.day, hoje.month, 2000)
        pessoa2 = Colaborador('not Birth', dt1.day, dt1.month, 2000)
        assert pessoa1.aniversario_hoje() is True
        assert pessoa2.aniversario_hoje() is False
