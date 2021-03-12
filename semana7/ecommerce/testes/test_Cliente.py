from ecommerce.classes.Cliente import Cliente


class TestCliente:
    def test_class_declared(self):
        objeto = Cliente('John Doe')
        assert isinstance(objeto, Cliente)

    def test_instanciar_objeto(self):
        objeto = Cliente('José da Silva')
        assert objeto.nome, 'José da Silva'

    def test_setter(self):
        objeto = Cliente('José da Silva')
        assert objeto.nome == 'José da Silva'
        objeto.nome = 'José da Silva Júnior'
        assert objeto.nome == 'José da Silva Júnior'

    def test_str_repr(self):
        cliente = Cliente('José da Silva')
        assert str(cliente) == 'José da Silva'
        assert repr(cliente) == 'Cliente => José da Silva'
