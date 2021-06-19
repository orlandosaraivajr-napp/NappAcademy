from projeto.Abstracao import *
from projeto.Arquivo import *
from projeto.Busca import *
import pytest
import unittest

class TestAbstracaoCaseSentive(unittest.TestCase):

    def test_instanciar_objeto_ok(self):
        objeto = Abstracao(**{'metodo_de_busca':'sensitive', 'arquivo':'txt'})
        assert isinstance(objeto, Abstracao)

    def test_arquivo_nao_implementado(self):
        msg_erro = 'Formato de relatório não implementado'
        with pytest.raises(Exception) as error:
            Abstracao(**{'metodo_de_busca':'sensitive', 'arquivo':'sqlite3'})
        assert str(error.value) == msg_erro
    
    def test_metodo_de_busca_nao_implementado(self):
        msg_erro = 'Metodo de busca não implementado'
        with pytest.raises(Exception) as error:
            Abstracao(**{'metodo_de_busca':'blablabla', 'arquivo':'txt'})
        assert str(error.value) == msg_erro
    
    def test_metodo_procura_palavra_txt(self):
        objeto = Abstracao(**{'metodo_de_busca':'sensitive', 'arquivo':'txt'})
        assert isinstance(objeto.procura_palavra('napp'), list)
    
    def test_metodo_procura_palavra_csv(self):
        objeto = Abstracao(**{'metodo_de_busca':'sensitive', 'arquivo':'csv'})
        assert isinstance(objeto.procura_palavra('napp'), list)



class TestAbstracaoCaseInsentive(unittest.TestCase):

    def test_instanciar_objeto_ok(self):
        objeto = Abstracao(**{'metodo_de_busca':'insensitive', 'arquivo':'txt'})
        assert isinstance(objeto, Abstracao)

    def test_arquivo_nao_implementado(self):
        msg_erro = 'Formato de relatório não implementado'
        with pytest.raises(Exception) as error:
            Abstracao(**{'metodo_de_busca':'insensitive', 'arquivo':'sqlite3'})
        assert str(error.value) == msg_erro
    
    def test_metodo_de_busca_nao_implementado(self):
        msg_erro = 'Metodo de busca não implementado'
        with pytest.raises(Exception) as error:
            Abstracao(**{'metodo_de_busca':'blablabla', 'arquivo':'txt'})
        assert str(error.value) == msg_erro
    
    def test_metodo_procura_palavra_txt(self):
        objeto = Abstracao(**{'metodo_de_busca':'insensitive', 'arquivo':'txt'})
        assert isinstance(objeto.procura_palavra('napp'), list)
    
    def test_metodo_procura_palavra_csv(self):
        objeto = Abstracao(**{'metodo_de_busca':'insensitive', 'arquivo':'csv'})
        assert isinstance(objeto.procura_palavra('napp'), list)

