from pynder.finder import (
    Pynder
)
import pytest

# testes cosiderando estar no diretorio /semana18/projeto se não pytest não contra os arquivos


class TestPynder:
    def test_instanciar_classe(self):
        objeto = Pynder()
        assert isinstance(objeto, Pynder)

    def test_metodo_search_all_files_txt_noresults(self):
        myFinder = Pynder()
        result = myFinder.search_all_files(
            text='google',
            extension='txt',
            path='./pynder/test/data/',
        )
        assert len(result) == 1
        assert len(result[0].get('findInLines')) == 0

    def test_metodo_search_all_files_txt(self):
        myFinder = Pynder()
        result = myFinder.search_all_files(
            text='napp',
            extension='txt',
            path='./pynder/test/data/',
        )
        assert len(result) == 1
        assert type(result[0]) == dict
        assert len(result[0].get('findInLines')) == 113

    def test_metodo_search_all_files_csv_noresults(self):
        myFinder = Pynder()
        result = myFinder.search_all_files(
            text='google',
            extension='csv',
            path='./pynder/test/data/',
        )
        assert len(result) == 1
        assert len(result[0].get('findInLines')) == 0

    def test_metodo_search_all_files_csv(self):
        myFinder = Pynder()
        result = myFinder.search_all_files(
            text='napp',
            extension='csv',
            path='./pynder/test/data/',
        )
        assert len(result) == 1
        assert type(result[0]) == dict
        assert len(result[0].get('findInLines')) == 2

    def test_metodo_search_all_files_invalid_extension(self):
        myFinder = Pynder()
        msg_erro = "INVALIDA Extension Not Implemented in Getter values"
        with pytest.raises(Exception) as error:
            myFinder.search_all_files(
                text='napp',
                extension='INVALIDA',
                path='./pynder/test/data/',
            )
        assert str(error.value) == msg_erro

    def test_metodo_search_in_file_txt(self):
        myFinder = Pynder()
        result = myFinder.search_in_file(
            text='napp',
            extension='txt',
            file_name='./pynder/test/data/testFile.txt',
        )
        assert type(result) == dict
        assert len(result.get('findInLines')) == 113

    def test_metodo_search_in_file_csv(self):
        myFinder = Pynder()
        result = myFinder.search_in_file(
            text='napp',
            extension='csv',
            file_name='./pynder/test/data/testFile.csv',
        )
        assert type(result) == dict
        assert len(result.get('findInLines')) == 2

    def test_metodo_search_in_file_invalid_extension(self):
        myFinder = Pynder()
        msg_erro = "INVALIDA Extension Not Implemented in Getter values"
        with pytest.raises(Exception) as error:
            result = myFinder.search_in_file(
                text='napp',
                extension='INVALIDA',
                file_name='./pynder/test/data/testFile.csv',
            )
        assert str(error.value) == msg_erro
