# Questão 1
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu sou {self.profissao}."


# Questão 2
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Titular: {self._titular}, Saldo: {self._saldo:.2f}"

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True


# Questão 3
conta1 = ContaBancaria("Lucas", 2500.00)
conta2 = ContaBancaria("Mariana", 3500.75)

print(conta1)
print(conta2)


# Questão 4
conta = ContaBancaria("Fernanda", 4500.00)
ContaBancaria.ativar_conta(conta)
print(conta.ativo)


# Questão 5
# Refatoração já foi feita na questão 2 com a utilização de propriedades.

# Questão 6
print(conta.titular)


# Questão 7
class ClienteBanco:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone


# Instanciando três objetos da classe ClienteBanco
cliente1 = ClienteBanco("Beatriz", 29, "111.222.333-44", "Avenida Central, 101", "(11) 98765-4321")
cliente2 = ClienteBanco("Eduardo", 42, "555.666.777-88", "Rua das Flores, 202", "(21) 12345-6789")
cliente3 = ClienteBanco("Carla", 37, "999.888.777-66", "Praça da Liberdade, 303", "(31) 99999-8888")


# Questão 8
class ClienteBanco:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def criar_cliente(cls, nome, idade, cpf, endereco, telefone):
        return cls(nome, idade, cpf, endereco, telefone)


# Utilizando o método de classe para criar um novo cliente
novo_cliente = ClienteBanco.criar_cliente("Ricardo", 33, "222.333.444-55", "Travessa dos Pássaros, 404", "(41) 77777-6666")
print(vars(novo_cliente))
