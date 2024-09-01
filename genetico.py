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
# Seleção dos pais por torneio
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
# Cruzamento PMX
def cruzamento_pais(pai1, pai2, taxa_cruzamento):
    if random.random() <= taxa_cruzamento:
        filho1 = [None] * len(pai1)
        filho2 = [None] * len(pai1)

        ponto_corte = randint(1, len(pai1)-1) # O ponto de corte sempre vai ser menos da metade
        
        filho1[:ponto_corte] = pai1[:ponto_corte]
        filho2[:ponto_corte] = pai2[:ponto_corte]

        # Definindo o filho1
        for i in range(ponto_corte, len(pai1)):
            # if pai2[i] not in filho1:
            #     filho1[i] = pai2[i]
            valor = pai2[i]   
            while valor in filho1:
                valor = pai2[pai1.index(valor)]
            filho1[i] = valor
        
        # defininco filho2
        for i in range(ponto_corte, len(pai1)):
            valor = pai1[i]
            while valor in filho2:
                valor = pai1[pai2.index(valor)]
            filho2[i]= valor

        return filho1, filho2
    return pai1, pai2

# Cruzamento de todos os pais
def cruzamento(lista_pais, taxa_cruzamento):
    lista_filhos = [None] * len(lista_pais)
    for i in range(0, len(lista_pais), 2):
        filho1, filho2 = cruzamento_pais(lista_pais[i], lista_pais[i+1], taxa_cruzamento)
        lista_filhos[i] = filho1
        lista_filhos[i+1] = filho2
    return lista_filhos

# Mutação

# Para fazer os testes
def principal():
    # Para fazer a reprodutibilidade
    random.seed(7)
    
    # Testando até agora
    genes = [1, 2, 3, 4, 5]
    tamanho_pop = 10
    taxa_cruzamento = 0.9
    lista_pais = populacao_inicial(tamanho_pop, genes)
    print(lista_pais)
    lista_filhos = cruzamento(lista_pais, taxa_cruzamento)
    print(lista_filhos)
    

if __name__ == "__main__":
    principal()