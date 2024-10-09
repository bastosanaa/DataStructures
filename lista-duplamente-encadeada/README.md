# Documentação - MinhaListaDuplamenteEncadeada

# Classes

- Elemento: classe que representa os Nodes que formarão a lista encadeada, contendo o seu valor, o seu antecessor e sucessor;

- MinhaListaDuplamenteEncadeada: classe que representa a implementação pedida para o trabalhinho 1;

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

A implementação da MinhaListaDuplamenteEncadeada possui algumas peculiaridades dadas pelas decisões do desenvolvedor, seguem estas:

## Peculiaridades da Implementação

1. acessarAtual - caso o cursor apontar para um elemento, retorna o valor do elemento apontado;

Comportamento do cursor ao realizar as operações de lista:

- Inserções = após todas as inserções o cursor se apontará para o elemento inserido

2. inserirAntesDoAtual:

   - caso 1: cursor aponta para um elemento que possui antecessor (do meio da lista);
   - caso 2: cursor aponta para o primeiro elemento da lista
     no caso 2 a função não altera o elemento sucessor do elemento antecessor apontado pelo cursor e define o novo elemento como o inicio da lista

3. inserirAposAtual:

   - caso 1: cursor aponta para um elemento que possui sucessor (do meio da lista);
   - caso 2: cursor aponta para o primeiro elemento da lista
     no caso 2 a função não altera o elemento anteessor do elemento sucessor apontado pelo cursor e define o novo elemento como o fim da lista

4. inserirPorPrimeiro;

5. inserirPorUltimo;

6. inserirNaPosicao:

   - a localização da posição a ser inserida é feita por uma contagem dos elementos, partindo do incio da lista;
   - caso a lista esteja vazia, o elemento é inserido como primeiro;
   - caso a lista+1 ainda possua um número de elementos menor do que a da posição escolhida, o elemento é adicionado ao final da lista;

7. excluirAtual: após a exclusão o cursor apontará para o elemento que precedia o elemento excluído

8. excluirPrimeiro: após a exclusão o cursor apontará para o primeiro elemento

9. excluirUltimo: após a exclusão o cursor apontará para o último elemento

10. excluirElemento: exclui o elemento da lista que possui valor igual ao passado (considerando que não há valores repetidos na lista)

11. exluirDaPosicao:
    - a localização da posição a ter o elemento excluido é feita por uma contagem dos elementos, partindo do incio da lista;
    - caso a lista esteja vazia, nada acontece;
    - caso a posição ainda não esteja ocupada na lista, nada acontece
    - o cursor aponta para o elemento que precede o elemento excluido, ou para o ultimo elemento caso nao haja exclusao
