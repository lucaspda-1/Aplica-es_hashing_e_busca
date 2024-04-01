from testes import teste_insercao,num_registros_10k,num_registros_100k,num_registros_1m,teste_busca

class ListaNaoOrdenadaSequencial:
    def __init__(self):
        self.registros = []

    def inserir(self, pessoa):
        self.registros.append(pessoa)

    def buscar(self, cpf):
        for pessoa in self.registros:
            if pessoa.cpf == cpf:
                return pessoa
        return None
    


print("TESTE DE INSERÇÃO#######")
print()
print("Inserção na Lista Não Ordenada com Busca Sequencial 10000 registros:")
print()
lista_sequencial_10k = ListaNaoOrdenadaSequencial()
tempo_lista_sequencial_10k = teste_insercao(lista_sequencial_10k, num_registros_10k)
print(f"Tempo de inserção na Lista Não Ordenada com Busca Sequencial 10000 registros: {tempo_lista_sequencial_10k:.6f} segundos")
print()
print("Inserção na Lista Não Ordenada com Busca Sequencial 100000 registros:")
print()
lista_sequencial_100k = ListaNaoOrdenadaSequencial()
tempo_lista_sequencial_100k = teste_insercao(lista_sequencial_100k, num_registros_100k)
print(f"Tempo de inserção na Lista Não Ordenada com Busca Sequencial 100000 registros: {tempo_lista_sequencial_100k:.6f} segundos")
print()
print("Inserção na Lista Não Ordenada com Busca Sequencial 1000000 registros:")
print()
lista_sequencial_1m = ListaNaoOrdenadaSequencial()
tempo_lista_sequencial_1m = teste_insercao(lista_sequencial_1m, num_registros_1m)
print(f"Tempo de inserção na Lista Não Ordenada com Busca Sequencial 1000000 registros: {tempo_lista_sequencial_1m:.6f} segundos")
print()
print()
print("TESTE DE BUSCA########")
print()
# Teste de busca na Lista Não Ordenada com Busca Sequencial
print("Busca na Lista Não Ordenada com Busca Sequencial 10000 buscas):")
print()
tempo_busca_sequencial_10k = teste_busca(lista_sequencial_10k, num_registros_10k)
print(f"Tempo médio de busca na Lista Não Ordenada com Busca Sequencial 10000 buscas): {tempo_busca_sequencial_10k:.6f} segundos")
print()
print("Busca na Lista Não Ordenada com Busca Sequencial 100000 buscas):")
print()
tempo_busca_sequencial_100k = teste_busca(lista_sequencial_100k, num_registros_100k)
print(f"Tempo médio de busca na Lista Não Ordenada com Busca Sequencial 100000 buscas): {tempo_busca_sequencial_100k:.6f} segundos")
print()
print("Busca na Lista Não Ordenada com Busca Sequencial 1000000 buscas):")
print()
tempo_busca_sequencial_1m = teste_busca(lista_sequencial_1m, num_registros_1m)
print(f"Tempo médio de busca na Lista Não Ordenada com Busca Sequencial 1000000 buscas): {tempo_busca_sequencial_1m:.6f} segundos")