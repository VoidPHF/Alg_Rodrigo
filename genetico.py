#importações
from matplotlib import pyplot as plt
import math
import random
import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Leitura do arquivo
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
            coordenadas[indice] = (float(parte[1]), float(parte[2])) # Guardar o ponto e as coordenadas em uma tupla dentro da lista
    return coordenadas

# População incial (soluções aleatorias)
def pop_inicial(total_solucoes):
    caminhos_aleatorios = []
    for _ in range (100):
        rota_aleatoria = list(range(1,  total_solucoes))
        random.shuffle(rota_aleatoria)
        rota_aleatoria = [0] + rota_aleatoria
        caminhos_aleatorios.append(rota_aleatoria)
    
    return caminhos_aleatorios

#Avaliação (fitness)
def distancia_total(pontos, rota):
    return sum(math.dist(pontos[rota[i-1]], pontos[rota[i]]) for i in range (1, len(rota)))

# Seleção
def escolher_pais(pontos, populacao_antiga):
    sobreviventes = []
    random.shuffle(populacao_antiga)
    metade = len(populacao_antiga) // 2
    for i in range (metade):
        if distancia_total(pontos, populacao_antiga[i]) <  distancia_total(pontos, populacao_antiga[i + metade]):
            sobreviventes.append(populacao_antiga[i])
        else:
            sobreviventes.append(populacao_antiga[i+metade])

    return sobreviventes


# Cruzamento
def criar_filhos(pai1, pai2):
    filho = []
    começo = random.randint(0, len(pai1) - 1)
    fim = random.randint(começo, len(pai1))
    gene_pai1 = pai1[começo:fim]
    gene_pai2 = list([gene for gene in pai2 if gene not in gene_pai1])
    for i in range (0,(len(pai1))):
        if começo <= i < fim:
            filho.append(gene_pai1.pop(0))
        else:
            filho.append(gene_pai2.pop(0))

    return filho

# Recombinação
def crossover(sobreviventes):
    filhos = []
    metade = len(sobreviventes) // 2
    for i in range (metade):
        pai1, pai2 = sobreviventes[i], sobreviventes [i+metade]
        for _ in range(2):
            filhos.append(criar_filhos(pai1, pai2))
            filhos.append(criar_filhos(pai2, pai1))
    return filhos

# Mutação
def mutação(nova_geração):
    geração_mutada = []
    for rota in nova_geração:
        if random.random() < 0.009:
            ponto1, ponto2 = random.randint(1, len(rota)- 1), random.randint(1, len(rota)- 1)
            rota[ponto1], rota[ponto2] = rota [ponto2], rota[ponto1]
        geração_mutada.append(rota)

    return geração_mutada

# Cria uma nova população
def gerar_nova_população(pontos, populacao_antiga):
    sobreviventes = escolher_pais(pontos, populacao_antiga)
    filhos = crossover(sobreviventes)
    nova_geração = mutação(filhos)
    return nova_geração

def encontrar_melhor_rota(pontos, populacao):
    melhor_rota = min(populacao, key=lambda rota: distancia_total(pontos, rota))
    return melhor_rota

def main():
    arquivo = "berlin52.tsp"
    pontos = ler_arquivo(arquivo)
    total_solucoes = len(pontos)
    populacao_inicial = pop_inicial(total_solucoes)
    
    melhor_rota_primeira_geracao = None
    melhor_rota_ultima_geracao = None
    
    for geracao in range(1000):
        print(f"Geração {geracao+1}")
        populacao_nova = gerar_nova_população(pontos, populacao_inicial)
        melhor_rota = encontrar_melhor_rota(pontos, populacao_nova)
        print(f"Melhor rota: {melhor_rota}")
        print(f"Distância total: {distancia_total(pontos, melhor_rota)}")
        print("————————————————————————")
        
        if geracao == 0:
            melhor_rota_primeira_geracao = melhor_rota
        elif geracao == 999:
            melhor_rota_ultima_geracao = melhor_rota
        
        populacao_inicial = populacao_nova
    
    # lista de coordenadas para a primeira geração
    x_coords_primeira_geracao = [pontos[melhor_rota_primeira_geracao[i]][0] for i in range(len(melhor_rota_primeira_geracao))] + [pontos[0][0]]
    y_coords_primeira_geracao = [pontos[melhor_rota_primeira_geracao[i]][1] for i in range(len(melhor_rota_primeira_geracao))] + [pontos[0][1]]
    
    # listas de coordenadaspara a última geração
    x_coords_ultima_geracao = [pontos[melhor_rota_ultima_geracao[i]][0] for i in range(len(melhor_rota_ultima_geracao))] + [pontos[0][0]]
    y_coords_ultima_geracao = [pontos[melhor_rota_ultima_geracao[i]][1] for i in range(len(melhor_rota_ultima_geracao))] + [pontos[0][1]]
    
    # gráfico para a primeira geração
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords_primeira_geracao, y_coords_primeira_geracao, 'r-')
    plt.scatter(x_coords_primeira_geracao, y_coords_primeira_geracao, color='blue')
    plt.title('Primeira Geração')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
    
    # gráfico para a última geração
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords_ultima_geracao, y_coords_ultima_geracao, 'r-')
    plt.scatter(x_coords_ultima_geracao, y_coords_ultima_geracao, color='blue')
    plt.title('Última Geração')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
