import random

arquivo='berlin52.tsp'

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
        populacao[i] = [individuo, 0]
    return populacao

def calcular_distancia(individuo):
    distancia = 0 #distancia inicial 
    for i in range(len(individuo) - 1): 
        x1, y1 = individuo[i][1], individuo[i][2] # posição 1 e 2 porque não retirei o ponto/cidades da lista
        x2, y2 = individuo[i + 1][1], individuo[i + 1][2]
        distancia += abs(x2 - x1) + abs(y2 - y1)
    return distancia
    
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
    
    for i, individuo in enumerate(lista): #essa foi a unica forma q meu cerebro frito de encontrou pra usar a variavel individuo
        distancia = calcular_distancia(individuo[0])
        print(f"Possibilidade {i}: {individuo[0]} = Distância: {distancia}  <"+ "-"*20)

if __name__ == "__main__":
    principal()