import timeit
from cpf import  gerar

# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, cpf, nome, telefone, senha):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.senha = senha

# Função de teste de inserção na estrutura de dados
def teste_insercao(estrutura, num_registros):
    inicio = timeit.default_timer()
    for _ in range(num_registros):
        cpf, nome, telefone, senha = gerar()  #função do codigo cpf
        pessoa = Pessoa(cpf, nome, telefone, senha)
        estrutura.inserir(pessoa)
    fim = timeit.default_timer()
    return fim - inicio

# Função de teste de busca na estrutura de dados
def teste_busca(estrutura, num_buscas):
    tempos = []
    for _ in range(num_buscas):
        cpf, _, _, _ = gerar()  #função gerar() para gerar os dados
        inicio = timeit.default_timer()
        estrutura.buscar(cpf)
        fim = timeit.default_timer()
        tempo = fim - inicio
        tempos.append(tempo)
    tempo_medio = sum(tempos) / len(tempos)
    return tempo_medio

# Definindo o número de registros para inserção para cada estrutura de dados

num_registros_10k = 10000
num_registros_100k = 100000
num_registros_1m = 1000000




