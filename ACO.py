from matplotlib import pyplot as plt
import random

"""Algoritmo de otimização colônia de formigas"""
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

# Inicializando as formigas
class Formiga:
    def __init__(self, qtde_pontos):
        self.cidades_visitadas = [None] * qtde_pontos
        self.visitou = [False] * qtde_pontos
        self.distancia_percorrida = 0
            
# Retorna distância entre dois pontos
def calcular_distancia(cidade_a, cidade_b):
    distancia = ((cidade_a[1] - cidade_b[1]) ** 2 + (cidade_a[2] - cidade_b[2]) ** 2) ** 0.5
    return distancia

# Criando matriz com as distâncias entre 2 pontos => retorna uma matriz com as distancias entre dois pontos
def gerar_matriz_distancias(cidades):
    arestas = [[None] * len(cidades) for _ in range(len(cidades))]
    for i in range(len(cidades)):
        for j in range(len(cidades)):
            arestas[i][j] = calcular_distancia(cidades[i], cidades[j])
    return arestas

# Inicializando matriz de feromonio
def gerar_matriz_feromonios(cidades, valor_inicial):
    feromonio = [[valor_inicial] * len(cidades) for _ in range(len(cidades))] 
    return feromonio

# Evaporaçao de feromônios
def evaporar_feromonios(matriz_feromonios, taxa_evaporacao):
    for i in range(len(matriz_feromonios)):
        for j in range(len(matriz_feromonios)):
            matriz_feromonios[i][j] *= (1-taxa_evaporacao)

# Deposicao de feromônios
def depositar_feromonios(k, formiga, matriz_feromonios, taxa_deposicao):
    for i in range(len(formiga[k].cidades_visitadas) - 1):
        cidade_a = formiga[k].cidades_visitadas[i]
        cidade_b = formiga[k].cidades_visitadas[i+1]
        matriz_feromonios[cidade_a][cidade_b] += taxa_deposicao / formiga[k].distancia_percorrida
        matriz_feromonios[cidade_b][cidade_a] = matriz_feromonios[cidade_a][cidade_b]
    
    # Fechando ciclo hamiltoniano
    cidade_a = formiga[k].cidades_visitadas[-1]
    cidade_b = formiga[k].cidades_visitadas[0]
    matriz_feromonios[cidade_a][cidade_b] += taxa_deposicao / formiga[k].distancia_percorrida
    matriz_feromonios[cidade_b][cidade_a] = matriz_feromonios[cidade_a][cidade_b]

# Atualizar feromonios
def atualizar_feromonios(formiga, matriz_feromonios, taxa_evaporacao, taxa_deposicao):
    evaporar_feromonios(matriz_feromonios, taxa_evaporacao)

    for k in range(len(formiga)):
        depositar_feromonios(k, formiga, matriz_feromonios, taxa_deposicao)

# Calculando as Probabilidades => Retorna lista com a probabilidade de visitar as proximas cidades
def calcular_probabilidades(cidade_atual, matriz_feromonios, matriz_distancias, formiga, qtde_pontos, a, b):
    probabilidades = []
    for cidade in range(qtde_pontos):
        if not formiga.visitou[cidade]:
            valor_feromonio = matriz_feromonios[cidade_atual][cidade] ** a
            valor_distancia = (1/matriz_distancias[cidade_atual][cidade]) ** b
            probabilidades.append(valor_feromonio * valor_distancia)
        else:
            probabilidades.append(0)

    total = sum(probabilidades)
    if total > 0:
        probabilidades = [probabilidade / total for probabilidade in probabilidades]
    
    return probabilidades

# Definir qual cidade visita a partir do passo atual 
def definir_prox_cidade(probabilidades, formiga, passo_atual):
    while True:
        prox_cidade = random.choices(range(len(probabilidades)), probabilidades)[0]
        if not formiga.visitou[prox_cidade]:
            formiga.cidades_visitadas[passo_atual] = prox_cidade
            formiga.visitou[prox_cidade] = True
            break

# Calcular o custo da solução construida pela formiga
def distancia_percorrida(formiga, matriz_distancias):
    distancia = 0
    for i in range(len(formiga.cidades_visitadas) - 1):
        cidade_a = formiga.cidades_visitadas[i]
        cidade_b = formiga.cidades_visitadas[i+1]

        if cidade_a is None or cidade_b is None:
            continue

        distancia += matriz_distancias[cidade_a][cidade_b]
    return distancia

# Fazer as rotas
def construir_solucoes(qtde_formigas, qtde_pontos, matriz_feromonios, matriz_distancias, a, b):
    formigas = [Formiga(qtde_pontos) for _ in range(qtde_formigas)]
    
    # Cidade inicial
    for formiga in formigas:
        cidade_inicial = random.randint(0, qtde_pontos -1)
        formiga.cidades_visitadas[0] = cidade_inicial
        formiga.visitou[cidade_inicial] = True

    # # Lista de cidades para iniciar
    # cidades_iniciais = list(range(qtde_pontos))

    # # Colocando uma formiga em cada ponto do mapa
    # for i, formiga in enumerate(formigas):
    #     cidade_inicial = cidades_iniciais[i]
    #     formiga.cidades_visitadas[0] = cidade_inicial
    #     formiga.visitou[cidade_inicial] = True

    # Construindo as soluções para cada formiga
    for passo_atual in range(1, qtde_pontos):
        for formiga in formigas:
            cidade_atual = formiga.cidades_visitadas[passo_atual - 1]
            probabilidades = calcular_probabilidades(cidade_atual, matriz_feromonios, matriz_distancias, formiga, qtde_pontos, a, b)
            definir_prox_cidade(probabilidades, formiga, passo_atual) 
            formiga.distancia_percorrida = distancia_percorrida(formiga, matriz_distancias)
    
    return formigas

# Retornar apenas a melhor solução 
def verificar_melhor_percurso(formigas):
    menor_distancia = float('inf')
    melhor_percurso = []
    for formiga in formigas:
        if formiga.distancia_percorrida < menor_distancia:
            menor_distancia = formiga.distancia_percorrida
            melhor_percurso = formiga.cidades_visitadas
    
    return melhor_percurso, menor_distancia

# Para fazer os testes
def principal():
    # Para fazer a reprodutibilidade
    random.seed(10)

    pontos = ler_arquivo("berlin52.tsp")

    feromonio_inicial = 0.1

    feromonios = gerar_matriz_feromonios(pontos, feromonio_inicial)
    distancias = gerar_matriz_distancias(pontos)
    qtde_formigas = len(pontos)
    alfa = 1
    beta = 2
    iteracoes = 150
    taxa_evaporacao = 0.1
    taxa_deposicao = 100
    
    for i in range(iteracoes):
        formigas = construir_solucoes(qtde_formigas, len(pontos), feromonios, distancias, alfa, beta)
        atualizar_feromonios(formigas, feromonios, taxa_evaporacao, taxa_deposicao)
    
        solucao_final, distancia = verificar_melhor_percurso(formigas)

    print(solucao_final, distancia)

    # Crie as listas de coordenadas x e y
    x_coords = [pontos[solucao_final[i]][1] for i in range(len(solucao_final))]
    y_coords = [pontos[solucao_final[i]][2] for i in range(len(solucao_final))]

    #Fechar o grafo
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])

    # Crie o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, 'r-')
    plt.scatter(x_coords, y_coords, color='blue')
    plt.title('Melhor Rota')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    principal()