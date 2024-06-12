'''class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} paginas'
    
    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'
    
    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade'''

#QUESTÃO 1
'''class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao == "médico":
            return f"Olá, Dr. {self.nome}!"
        elif self.profissao == "engenheiro":
            return f"Olá, Eng. {self.nome}!"
        else:
            return f"Olá, {self.nome}!"

pessoa1 = Pessoa("Sirlei", 45, "Professora")
print(pessoa1)
pessoa1.aniversario()
print(pessoa1)
print(pessoa1.saudacao)'''

#QUESTÂO 2

class ContaBancaria:
    def __init__(self, titular, saldo=0,):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
        self.ativar_conta= True
        
#QUESTÃO 3

    def __str__(self):
        return f'O titular da conta é: {self.titular} Tem um saldo de R$ {self.saldo}'

pessoa1 = ContaBancaria ('josé',100)
pessoa2 = ContaBancaria ('Jeferson', 100)
print (pessoa1)
print (pessoa2)

#QUESTÃO 4
 

