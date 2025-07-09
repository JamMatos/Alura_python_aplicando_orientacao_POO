"""1 - Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão."""
class Livro:
    def __init__(self,titulo,autor,ano_publicacao, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True


"""2 - Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias."""
class Livro:
    def __init__(self,titulo,autor,ano_publicacao, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f'Título {self.titulo.ljust(40)} | Autor {self.autor.ljust(25)} | Ano de Publicação {self.ano_publicacao}.'
    
livro1 = Livro('Seu corpo é o mar por onde quero navegar', 'Inarai', '1998', disponivel=True)
livro2 = Livro('Sorri Sou Rei', 'Natiruts', '1999', disponivel=True)
print(livro1)
print(livro2)

"""3 - Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não."""
class Livro:
    def __init__(self,titulo,autor,ano_publicacao, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f'Título {self.titulo.ljust(40)} | Autor {self.autor.ljust(25)} | Ano de Publicação {self.ano_publicacao}.'
    
    def emprestar(self):
        if self.disponivel == True:
            print(f"O livro {self.titulo} está disponível.")
        else:
            print(f"O livro {self.titulo} não está disponível.")
livro1 = Livro('Seu corpo é o mar por onde quero navegar', 'Inarai', '1998', chamado=True, disponivel=True)
livro1.emprestar()

"""4 - Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano."""
class Livro:
    livros = []
    def __init__(self,titulo,autor,ano_publicacao, disponivel = True):
        self._titulo = titulo.title()
        self.autor = autor
        self._ano_publicacao = ano_publicacao
        self.disponivel = disponivel
        Livro.livros.append(self)

    def __str__(self):
        return f'Título {self._titulo.ljust(40)} | Autor {self.autor.ljust(25)} | Ano de Publicação {self._ano_publicacao}.'
    
    def emprestar(self):
        if self.disponivel == True:
            print(f"O livro {self._titulo} está disponível.")
        else:
            print(f"O livro {self._titulo} não está disponível.")

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

livro1 = Livro('Seu corpo é o mar por onde quero navegar', 'Inarai', '1998', chamado=True)
livro2 = Livro('Sorri Sou Rei', 'Natiruts', '1999', chamado=True)
Livro.verificar_disponibilidade(1998)


"""5 - Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo."""

"""6 - No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo."""

"""7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico."""

"""8 - Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str."""