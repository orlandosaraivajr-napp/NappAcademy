class Cliente:
    def __init__(self, nome):
        self._name = nome

    @property
    def nome(self):
        return self._name

    @nome.setter
    def nome(self, value):
        self._name = value

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Cliente => ' + self._name
