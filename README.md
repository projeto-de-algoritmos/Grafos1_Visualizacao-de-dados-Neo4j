# Lista 1 sobre grafos da matéria Projeto de Algoritmos
Foi utilizado um Json com as interações entre os personagens do filme Les Miserable, transformado-o para a linguagem cypher foram adicionados os nós (Personagens) e as relações entre eles no banco orientado a grafo Neo4j.

## Visualização total das interações

 - Cypher utilizado para encontrar todas as ocorrências: 

        MATCH (n:Person) RETURN n
        
![Imagem1](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/Imagens/All_relations.png)  

## Visualização total de interações com o personagem principal Jean Valjean

- Cypher utilizado para encontrar todas as ocorrências: 

        MATCH (n:Person { name: 'Valjean' })--(p:Person)
        RETURN n,p
        
![Imagem2](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/Imagens/Valjean_relations.png)
