from testes import teste_insercao,teste_busca,num_registros_10k,num_registros_100k,num_registros_1m

class ListaOrdenadaBinaria:
    def __init__(self):
        self.registros = []

    def inserir(self, pessoa):
        # Implementar a inserção mantendo a lista ordenada pelo CPF
        inicio = 0
        fim = len(self.registros) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.registros[meio].cpf == pessoa.cpf:
                # Se ja tiver esse cpf ignora
                return
            elif self.registros[meio].cpf < pessoa.cpf:
                inicio = meio + 1
            else:
                fim = meio - 1
        # Insere na posição correta
        self.registros.insert(inicio, pessoa)

    def buscar(self, cpf):
        inicio = 0
        fim = len(self.registros) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.registros[meio].cpf == cpf:
                return self.registros[meio]
            elif self.registros[meio].cpf < cpf:
                inicio = meio + 1
            else:
                fim = meio - 1
        return None
    
print("TESTE DE INSERÇÃO#######")
print()
print("Inserção na Lista Ordenada com Busca Binária 10000 registros:")
print()
lista_binaria_10k = ListaOrdenadaBinaria()
tempo_lista_binaria_10k = teste_insercao(lista_binaria_10k, num_registros_10k)
print(f"Tempo de inserção na Lista Ordenada com Busca Binária 10000 registros: {tempo_lista_binaria_10k:.6f} segundos")
print()
print("Inserção na Lista Ordenada com Busca Binária 100000 registros:")
print()
lista_binaria_100k = ListaOrdenadaBinaria()
tempo_lista_binaria_100k = teste_insercao(lista_binaria_100k, num_registros_100k)
print(f"Tempo de inserção na Lista Ordenada com Busca Binária 100000 registros: {tempo_lista_binaria_100k:.6f} segundos")
print()
print("Inserção na Lista Ordenada com Busca Binária 1000000 registros:")
lista_binaria_1m = ListaOrdenadaBinaria()
print()
tempo_lista_binaria_1m = teste_insercao(lista_binaria_1m, num_registros_1m)
print(f"Tempo de inserção na Lista Ordenada com Busca Binária 1000000 registros: {tempo_lista_binaria_1m:.6f} segundos")


print()
print("TESTE DE BUSCA########")
print()

print("Busca na Lista Ordenada com Busca Binária 10000 buscas:")
print()
tempo_busca_binaria_10k = teste_busca(lista_binaria_10k, num_registros_10k)
print(f"Tempo médio de busca na Lista Ordenada com Busca Binária 10000 buscas: {tempo_busca_binaria_10k:.6f} segundos")
print()
print("Busca na Lista Ordenada com Busca Binária 100000 buscas:")
print()
tempo_busca_binaria_100k = teste_busca(lista_binaria_100k, num_registros_100k)
print(f"Tempo médio de busca na Lista Ordenada com Busca Binária 100000 buscas: {tempo_busca_binaria_100k:.6f} segundos")
print()
print("Busca na Lista Ordenada com Busca Binária 1000000 buscas:")
print()
tempo_busca_binaria_1m = teste_busca(lista_binaria_1m, num_registros_1m)
print(f"Tempo médio de busca na Lista Ordenada com Busca Binária 1000000 buscas: {tempo_busca_binaria_1m:.6f} segundos")
