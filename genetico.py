import random
from random import randint

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
def torneio(aptidao):
    pai1 = randint(0, len(aptidao) - 1)
    pai2 = randint(0, len(aptidao) - 1)

    if aptidao[pai1] < aptidao[pai2]: # Retorna a menor aptidão que é o menor percurso
        return pai1
    else:
        return pai2

def selecao_pais(populacao, aptidao):
    lista_pais = [None] * len(populacao)

    for i in range(len(populacao)):
        indice = torneio(aptidao)
        lista_pais[i] = populacao[indice]
    
    return lista_pais

# Fazer cruzamento
# Torneio
# Mutação

# Para fazer os testes
def principal():
    # Para fazer a reprodutibilidade
    random.seed(10)
    # Testando a função de seleção
    pop = [1, 2, 3, 4, 5, 6, 7]
    apt = [100, 50, 2, 6, 85, 24, 7]
    print(selecao_pais(pop, apt))
    
    

if __name__ == "__main__":
    principal()