import random

"""Algoritmo genético"""
# Ler arquivo Berlin52 e armazenar pontos em uma lista
def ler_arquivo(arquivo):
    coordenadas = [None for i in range(52)]
    with open(arquivo, "r") as f:
        linhas = f.readlines()
        inicio = linhas.index("NODE_COORD_SECTION\n") + 1
        for caractere in linhas[inicio:]:
            if caractere.strip() == "EOF":
                break
            parte = caractere.split()
            indice = int(parte[0])- 1 # para inserir em cada posição da lista coordenadas
            coordenadas[indice] = (int(parte[0]), float(parte[1]), float(parte[2])) # Guardar o ponto e as coordenadas em uma tupla dentro da lista
    return coordenadas


#Criar população inicial
def populacao_inicial(tamanho_pop, genes):
    populacao = [None] * tamanho_pop
    for i in range(tamanho_pop):
        individuo = random.sample(genes, len(genes))
        populacao[i] = individuo
    return populacao

# Calcular aptidão
# Seleção dos pais
# Fazer cruzamento
# Torneio
# Mutação

# Para fazer os testes
def principal():
    # Para fazer a reprodutibilidade
    random.seed(10)
    # Testando
    genes = ler_arquivo("berlin52.tsp")
    lista = populacao_inicial(5, genes)
    print(lista)
    

if __name__ == "__main__":
    principal()