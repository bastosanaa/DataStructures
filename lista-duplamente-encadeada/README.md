# Classes

- Elemento: classe que representa os Nodes que formarão a lista encadeada, contendo o seu valor e "apontando" para o seu sucessor

- EmptyListError: exceção levantada quando uma operação é realizada em uma lista encadeada vazia;

- MinhaListaEncadeada: classe que representa a implementação pedida para o trabalhinho 1, optei por criar uma lista encadeada NÃO circular, contendo algumas peculiaridades exclusivas que serão documentadas abaixo:

# Peculiaridades da implementação

- A implementação da MinhaListaEncadeada é dividida em duas partes

  1. operações de cursor: algumas funções complementares que auxiliarão nas funções principais, estas não possuem tratamento de erros já que serão utilizadas dentro das funções princípais, responsáveis por possíveis verificações;

  2. operações de lista: funções de acessos,incerções e remoções feitas na lista.

1. acessarAtual - retorna o valor do Node em que o cursor "se localiza";

2. inserirAntesDoAtual:

   - ao inserir o elemento antes do elemento atual, o cursor continua por apontar para o elemento em que se encontrava antes da alteração(elemento atual);
   - Ao tentar inserir um elemento sem que o cursor aponte para ninguém (lista vazia), é levantado um erro

3. inserirAposAtual - ao inserir o elemento antes do elemento atual, o cursor continua por apontar para o elemento em que se encontrava antes da alteração(elemento atual);

4. inserirComoUltimo:
   - caso nao haja nenhum elemento na lista, a função insere como primeiro;
   - a função faz com que o cursor aponte para o elemento adicionado (último elemento);
