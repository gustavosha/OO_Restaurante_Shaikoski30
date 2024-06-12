#1 Criando uma classe usando construtor
class Restaurante:
    def __init__ (self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False

    def __str__(self):
        #return self.nome
        return F"{self.nome}|{self.categoria}|{self.ativo}"
#2 Criando uma instancia da classe Restaurante com construtor

#restaurante_praca=Restaurante('Praça','Gourmet')
#restaurante_praca.nome='Praça'
#restaurante_praca.categoria='Gourmet'
restaurante_pizza=Restaurante()
#3Consumindo os objetos criado

#restaurante=[restaurante_praca,restaurante_pizza]

#print(restaurante_prac.nome,restaurante_praca.categoria)






#print(dir(restaurante_praca))
#print("")
#print(vars(restaurante_praca))
#print('')
#print(restaurante_praca)
