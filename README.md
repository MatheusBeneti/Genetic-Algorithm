
### Versão em Português:

# Algoritmo Genético para o Problema da Mochila

Este repositório contém uma implementação de um Algoritmo Genético para resolver o clássico Problema da Mochila. O problema envolve a otimização da seleção de itens para colocar em uma mochila, considerando o peso e o valor de cada item, com o objetivo de maximizar o valor total sem exceder a capacidade da mochila.

## Objetos e Parâmetros

Os objetos disponíveis para seleção, como "Refrigerator A," "Celular," "TV 55," entre outros, possuem diferentes pesos e valores. O espaço disponível na mochila é limitado a 3.0 unidades, e o algoritmo é configurado para criar uma população inicial de 48 indivíduos, com uma taxa de mutação de 10%. O algoritmo evolui por 1000 gerações.

## Como Utilizar

Certifique-se de ter os módulos `Crossover`, `Object`, e `Population` no mesmo diretório ou no seu caminho de busca para executar o código com sucesso. O script Python cria objetos, configura parâmetros do algoritmo, gera a população inicial, executa cruzamento e mutação ao longo de várias gerações, e exibe os resultados.

## Resultados

Ao final da execução, o script imprime a última geração da população, destaca o melhor indivíduo encontrado e apresenta a possível melhor combinação de objetos para a mochila, otimizando o valor total.


### English Version:

# Genetic Algorithm for the Knapsack Problem

This repository contains an implementation of a Genetic Algorithm to solve the classical Knapsack Problem. The problem involves optimizing the selection of items to put in a knapsack, considering the weight and value of each item, with the goal of maximizing the total value without exceeding the knapsack's capacity.

## Objects and Parameters

The available objects for selection, such as "Refrigerator A," "Cellphone," "TV 55," among others, have different weights and values. The available space in the knapsack is limited to 3.0 units, and the algorithm is configured to create an initial population of 48 individuals, with a mutation rate of 10%. The algorithm evolves over 1000 generations.

## How to Use

Make sure to have the `Crossover`, `Object`, and `Population` modules in the same directory or in your search path to successfully execute the code. The Python script creates objects, configures algorithm parameters, generates the initial population, performs crossover and mutation over multiple generations, and displays the results.

## Results

At the end of the execution, the script prints the last generation of the population, highlights the best individual found, and presents the possible best combination of objects for the knapsack, optimizing the total value.



