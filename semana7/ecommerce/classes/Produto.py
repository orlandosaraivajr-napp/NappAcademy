class Produto:
    def __init__(self, **kwargs):
        if kwargs.get('preco', 0) < 0:
            raise ValueError('Preço negativo')
        self._codigo_ean = kwargs.get('ean', '')
        self._preco = kwargs.get('preco', 0)

    @property
    def preco(self):
        return self._preco

    @property
    def ean(self):
        return self._codigo_ean

    @preco.setter
    def preco(self, value):
        self._preco = value

    def __str__(self):
        return self._codigo_ean

    def __repr__(self):
        return 'Produto:' + self._codigo_ean
