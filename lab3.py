"""Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa."""
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome.title()
        self.idade = int(idade)
        self.profissao = profissao.title()

    def __str__(self):
        return f'Nome {self.nome} | Idade {self.idade} | Profissão {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        if self.profissao.lower() == 'dev':
            return "Parabéns por ser um dev."
    
pessoa1 = Pessoa('Jamil', 23, 'Dev')
#print(pessoa1)
pessoa1.aniversario()
#print(pessoa1)
#print(pessoa1.saudacao())

"""1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão."""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titula = titular
        self.saldo = saldo
        self.ativo = False

"""2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias."""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular.title()
        self.saldo = saldo
        self.ativo = False
    
    def __str__(self):
        return f'Olá {self.titular}, seja bem-vindo(a), o seu saldo atual é de {self.saldo}.'
    
conta1 = ContaBancaria('Jamil', 'R$100.000')
conta2 = ContaBancaria('Leon', 'R$90.000')
print(conta1)
print(conta2)

"""3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo."""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular.title()
        self.saldo = saldo
        self.ativo = False
    
    def __str__(self):
        return f'Olá {self.titular}, seja bem-vindo(a), o seu saldo atual é de {self.saldo}.'
    
    def ativar_conta(self):
        self.ativo = True
        return print(f"O estado de ativo da sua conta é {self.ativo}.")

conta3 = ContaBancaria('Nilce', 'R$90.000')
print(conta3)
conta3.ativar_conta()


"""4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário."""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self.ativo = False
    
    def __str__(self):
        return f'Olá {self._titular}, seja bem-vindo(a), o seu saldo atual é de {self._saldo}.'
    
    def ativar_conta(self):
        self.ativo = True
        return print(f"O estado de ativo da sua conta é {self.ativo}.")
    
    @property
    def nome(self):
        print(self._titular)

conta4 = ContaBancaria('João', 'R$80.000')
print(conta4)
conta4.nome

"""5 - Crie uma instância da classe e imprima o valor da propriedade titular."""
conta4 = ContaBancaria('João', 'R$80.000')
print(conta4)
conta4.nome
"""6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor."""
class ClienteBanco:
    def __init__(self, nome, idade, id, valor, ativo = False):
        self.nome = nome
        self.idade = idade
        self.id = id
        self.valor = valor
        self.ativo = False
    
cliente1 = ClienteBanco('cliente1', 23, 1, 'R$100.000', True)
cliente2 = ClienteBanco('cliente2', 25, 2, 'R$200.000')
cliente3 = ClienteBanco('cliente3', 21, 3, 'R$300.000', True)

"""7 - Crie um método de classe para a conta ClienteBanco."""
class ClienteBanco:
    def __init__(self, nome, idade, id, valor, ativo = False):
        self.nome = nome
        self.idade = idade
        self.id = id
        self.valor = valor
        self.ativo = False
    
    @classmethod
    def estudante(cls,idade):
        if idade <= 21:
            print(f'Tem cliente que é estudante.')
        else:
            print(f'Tem cliente que não é estudante.')
    
cliente1 = ClienteBanco('cliente1', 23, 1, 'R$100.000', True)
cliente2 = ClienteBanco('cliente2', 25, 2, 'R$200.000')
cliente3 = ClienteBanco('cliente3', 21, 3, 'R$300.000', True)
cliente3.estudante(idade=21)