# Classe Carro
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"

# Criando uma instância da classe Carro
carro1 = Carro('Fusca', 'Azul', 1972)
print(carro1)

# Classe Restaurante
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = None
        self.capacidade = 0

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Capacidade: {self.capacidade}"

# Criando uma instância da classe Restaurante e atribuindo valores aos seus atributos
restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.endereco = 'Rua das Flores, 123'
restaurante1.capacidade = 100
print(restaurante1)

# Criando uma instância da classe Restaurante utilizando o construtor
restaurante2 = Restaurante('La Trattoria', 'Italiana')
print(restaurante2)

# Classe Cliente
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

# Instanciando 3 objetos da classe Cliente e atribuindo valores aos seus atributos
cliente1 = Cliente('João Silva', 'joao@example.com', '1234-5678', 'Rua A, 100')
cliente2 = Cliente('Maria Oliveira', 'maria@example.com', '8765-4321', 'Rua B, 200')
cliente3 = Cliente('Carlos Souza', 'carlos@example.com', '1122-3344', 'Rua C, 300')

print(cliente1)
print(cliente2)
print(cliente3)
