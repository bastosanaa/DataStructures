# Classes

- Elemento: classe que representa os Nodes que formarão a lista encadeada, contendo o seu valor e "apontando" para o seu sucessor

- EmptyListError: exceção levantada quando uma operação é realizada em uma lista encadeada vazia;

- MinhaListaDuplamenteEncadeada: classe que representa a implementação pedida para o trabalhinho 1

# Funções:

## Operações de cursor (\_\_privadas)

1. avancarKPosicoes:

   - recebe como parametro o número de posições a serem avançadas;
   - avança o cursor conforme o número de posições passadas, ou até que o Elemento atual do cursor não possua sucessor;

2. retrocederKPosicoes:

   - recebe como parâmetro o número de posições a serem regredidas;
   - regride o cursor conforme o número de posições passadas, ou até que o Elemento atual do cursor não possua antecessor;

3. irParaPrimeiro:

   - cursor aponta para o elemento apontado por inicio
   - caso um estiver vazio, ambos estao vazios, e portanto, nada acontece

4. irParaUltimo:

   - cursor aponta para o elemento apontado pelo fim
   - caso um estiver vazio, ambos estao vazios, e portanto, nada acontece

## Funções de manipulação na lista

1. acessarAtual - caso o cursor apontar para um elemento, retorna o valor do elemento apontado;

2. inserirAntesDoAtual:

3. inserirAposAtual -

4. inserirComoUltimo:
