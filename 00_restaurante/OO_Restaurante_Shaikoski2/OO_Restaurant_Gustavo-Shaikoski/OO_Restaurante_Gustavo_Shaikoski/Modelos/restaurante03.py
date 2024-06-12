# 1. Inserir um decorator @property

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    @property
    def ativo(self):
        return "⊠" if self._ativo else "☐"

    def __str__(self):
        return f"{self.nome.ljust(20)}|{self.categoria.ljust(20)}|{self.ativo.ljust(20)}"

# 2. Criando uma instancia da classe Restaurante com construtor

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# 3. Consumindo os objetos criado

print("Nome                |Categoria           |Status")
for restaurante in Restaurante.restaurantes:
    print(restaurante)