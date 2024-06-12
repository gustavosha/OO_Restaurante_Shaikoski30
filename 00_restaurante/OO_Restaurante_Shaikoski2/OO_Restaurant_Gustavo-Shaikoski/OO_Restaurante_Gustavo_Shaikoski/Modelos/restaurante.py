#Criando uma classe em PY
#class Restaurante:
    #nome=""
    #categoria=""
    #ativo=False

#Questao 3

class Restaurante:
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo


#2 Criando uma instancia da clase Restaurante

restaurante_praca=Restaurante()


#restaurante_praca.nome='Praça'
#Questao 5
restaurante_praca.nome='Bistrô'
#restaurante_praca.categoria='Gourmet'

#Questao 1

restaurante_praca.categoria='Italiana'

#Questao 6
restaurante_pizza=Restaurante()
restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'
#Questao 8
restaurante_pizza.ativo=True


#3Consumindo os objetos criados


restaurantes=[restaurante_praca,restaurante_pizza]

#print(restaurante_praca.nome,restaurante_pizza.categoria)

print(dir(restaurante_praca))
print('')
print(vars(restaurante_praca))

#Questao 2

print(restaurante_praca.nome)

#Questao 7

print(restaurante_pizza.categoria)

#Questao 9
print(vars(restaurante_pizza.nome,restaurante_pizza.categoria))

#Questao 4
print(vars(restaurante_praca.categoria))