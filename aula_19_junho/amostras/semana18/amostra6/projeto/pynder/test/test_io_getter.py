from io import TextIOWrapper
from pynder.io_getter import (
    IoGetter,
    GenericIoGetter
)
import pytest

# testes cosiderando estar no diretorio /semana18/projeto se não pytest não contra os arquivos


class TestIoGetter:
    def test_instanciar_classe_abstrata(self):
        msg_erro = "Can't instantiate abstract class IoGetter with abstract methods get_io"
        with pytest.raises(Exception) as error:
            IoGetter()
        assert str(error.value) == msg_erro


class TestGenericIoGetter:
    def test_instanciar_classe(self):
        objeto = GenericIoGetter()
        assert isinstance(objeto, IoGetter)
        assert isinstance(objeto, GenericIoGetter)

    def test_metodo_get_io_txt(self):
        objeto = GenericIoGetter()
        with objeto.get_io('./pynder/test/data/testFile.txt') as fileopend:
            assert type(fileopend) == TextIOWrapper

    def test_metodo_get_io_csv(self):
        objeto = GenericIoGetter()
        with objeto.get_io('./pynder/test/data/testFile.csv') as fileopend:
            assert type(fileopend) == TextIOWrapper
