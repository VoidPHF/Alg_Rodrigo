# Algoritmos para a resolução do problema do Caixeiro Viajante (TSP) 
## Tecnologias
- [Python](https://www.python.org/ "Python")
- [Matplotlib](https://matplotlib.org/ "Matplotlib")

## Projeto

Implementar dois algoritmos baseados em metaheurísticas de otimização para resolver o problema do Caixeiro Viajante (TSP) utilizando o mapa Berlin52 da biblioteca TSPlib. 

Este projeto foi desenvolvido para a 2ª Avaliação da disciplina "Projeto Interdisciplinar para Sistemas de Informação II"

## Problema do Caixeiro Viajante (TSP)

O problema do Caixeiro Viajante (TSP) consiste em determinar o menor ciclo hamiltoniano de um conjunto dado de pontos em um grafo. No que diz respeito a  complexidade computacional pertence a classe dos  problemas NP-Difíceis, que não se conhecem hoje algoritmos capazes de determinar resultado ótimo garantidamente em tempo polinomial.

Diferente dos métodos exatos, As metaheurísticas são capazes de  encontrar uma solução satisfatória dentro de um tempo de computação aceitável. Para esse trabalho será usado os algoritmos de colonia de formigas (ACO) e genético (GA).


## Algoritmo genético (GA)

O Algoritmo Genético (GA) pertence à classe dos algoritmos evolucionários, sendo uma técnica de otimização estocástica inspirada na teoria da evolução de Darwin. Nesse contexto, cada indivíduo de uma população representa uma solução potencial para o problema. O GA opera através de processos de seleção, cruzamento e mutação, onde as soluções mais aptas, ou seja, aquelas que melhor resolvem o problema em questão, têm uma maior probabilidade de transmitir suas características para a geração seguinte. Ao longo de várias iterações, o GA converge para uma solução otimizada, sendo amplamente utilizado para resolver o problema do caixeiro viajante (TSP) devido à sua capacidade de explorar vastos espaços de soluções e encontrar caminhos próximos ao ótimo global.


## Algoritmo da otimização de colônia de formigas (ACO)

O Algoritmo de Otimização por Colônia de Formigas (ACO) é inspirado no comportamento coletivo das formigas, que, através de uma organização social altamente estruturada, conseguem realizar tarefas complexas como encontrar o caminho mais curto entre o formigueiro e uma fonte de alimento. No contexto da resolução do TSP, o ACO simula a cooperação das formigas para explorar múltiplas rotas possíveis entre as cidades. As formigas virtuais depositam feromônios ao longo dos caminhos percorridos, reforçando rotas mais curtas e atraindo outras formigas para essas soluções promissoras. Com o tempo, o algoritmo converge para o caminho ótimo ou quase ótimo, fazendo do ACO uma ferramenta poderosa na resolução de problemas combinatórios como o TSP.


##Equipe
- Heloisa Gonçalves
- Paulo Henrique
- Ryan Batista