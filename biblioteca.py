from lab4 import Livro
livro1 = Livro('Seu corpo é o mar por onde quero navegar', 'Inarai', '1998', disponivel=True)
livro1.emprestar()
Livro.verificar_disponibilidade(1999)