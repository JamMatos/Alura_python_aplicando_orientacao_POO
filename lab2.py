import os

class Musica:
    def __init__(self, nome, artista, duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = int(duracao)

    def __str__(self):
        return f'nome {self.nome} | artista {self.artista} | duração {self.duracao}'
    
musica1 = Musica('Chocolate', 'Baekhyun', '184')
print(musica1)

"""
1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos."""
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro("Sedan", "Azul", 2023)

"""2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos."""
class Restaurante:
    def __init__(self, nome, categoria, ativo, faixa_preco, delivery):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.faixa_preco = faixa_preco
        self.delivery = delivery

restaurante1 = Restaurante("The Time", "Francesa", True, "$$$", False)

"""3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor."""
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False 

restaurante1 = Restaurante("The Time", "Francesa")

"""4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante."""
# input("Digite")
# os.system('cls')

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False 

    def __str__(self):
        return f'Nome {self.nome} | Categoria {self.categoria} | Ativo {self.ativo}'

restaurante1 = Restaurante("The Time", "Francesa")
print(restaurante1)

"""5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor."""
class Cliente:
    def __init__(self,nome,id,email,idade):
        self.nome = nome
        self.id = id
        self.email = email
        self.idade = idade
    
cliente1 = Cliente('Cliente1',1,'cliente1@gmail.com',25)
cliente2 = Cliente('Cliente2',2,'cliente2@gmail.com',22)
cliente3 = Cliente('Cliente3',3,'cliente3@gmail.com',27)