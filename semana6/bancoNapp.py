from BancoNapp.contas.ContaPessoaFisica import ContaPessoaFisica
from BancoNapp.contas.ContaPessoaJuridica import ContaPessoaJuridica
from BancoNapp.contas.ContaPoupanca import ContaPoupanca


pessoa1 = ContaPessoaFisica(nome='Pessoa 1', saldo=500.00)
pessoa2 = ContaPessoaFisica(nome='Pessoa 2', saldo=1000.00, limite=1000)


pessoa1.deposito(pessoa2.saque(10))
pessoa1.deposito(pessoa2.saque(20))

