from testes import teste_insercao,teste_busca,num_registros_10k,num_registros_100k,num_registros_1m

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def funcao_hashing(self, cpf):
        return int(cpf) % self.tamanho

    def inserir(self, pessoa):
        indice = self.funcao_hashing(pessoa.cpf)
        if self.tabela[indice] is None:
            self.tabela[indice] = pessoa
        else:
            pass

    def buscar(self, cpf):
        indice = self.funcao_hashing(cpf)
        if self.tabela[indice] is not None and self.tabela[indice].cpf == cpf:
            return self.tabela[indice]
        else:
            return None


# Definindo o tamanho para a tabela hash
tamanho_hash_10k = 10007  # Não sei porque , mas com o hash não queria pegar com o numero na casa fechada
tamanho_hash_100k = 100003  # Só quis pegar com o numero primo mais proximo
tamanho_hash_1m = 1000003  # Acho que tem haver com o calculo do hash


print("TESTE DE INSERÇÃO#######")
print()
print("Inserção na Tabela Hash 10000 registros:")
print()
hashing_10k = TabelaHash(tamanho_hash_10k)
tempo_hashing_10k = teste_insercao(hashing_10k, num_registros_10k)
print(f"Tempo de inserção na Tabela Hash 10000 registros: {tempo_hashing_10k:.6f} segundos")
print()
print("Inserção na Tabela Hash 100000 registros:")
print()
hashing_100k = TabelaHash(tamanho_hash_100k)
tempo_hashing_100k = teste_insercao(hashing_100k, num_registros_100k)
print(f"Tempo de inserção na Tabela Hash 100000 registros: {tempo_hashing_100k:.6f} segundos")
print()
print("Inserção na Tabela Hash 1000000 registros:")
print()
hashing_1m = TabelaHash(tamanho_hash_1m)
tempo_hashing_1m = teste_insercao(hashing_1m, num_registros_1m)
print(f"Tempo de inserção na Tabela Hash 1000000 registros: {tempo_hashing_1m:.6f} segundos")

print()
print("TESTE DE BUSCA########")
print()

print("Busca na Tabela Hash 10000 buscas:")
print()
tempo_busca_hashing_10k = teste_busca(hashing_10k, num_registros_10k)
print(f"Tempo médio de busca na Tabela Hash 10000 buscas: {tempo_busca_hashing_10k:.6f} segundos")
print()
print("Busca na Tabela Hash 10000 buscas:")
print()
tempo_busca_hashing_100k = teste_busca(hashing_100k, num_registros_100k)
print(f"Tempo médio de busca na Tabela Hash 10000 buscas: {tempo_busca_hashing_100k:.6f} segundos")
print()
print("Busca na Tabela Hash 100000 buscas:")
print()
tempo_busca_hashing_1m = teste_busca(hashing_1m, num_registros_1m)
print(f"Tempo médio de busca na Tabela Hash 100000 buscas: {tempo_busca_hashing_1m:.6f} segundos")
