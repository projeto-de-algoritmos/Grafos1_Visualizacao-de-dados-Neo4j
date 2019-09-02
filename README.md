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

## Personagens que Jean Valjean não interagem


- Cypher utilizado para encontrar todas as ocorrências: 




       MATCH (p:Person {name:"Valjean"})-[:interagiu_com]->(m)<-[:interagiu_com]-(coActors),
        (coActors)-[:interagiu_com]->(m2)<-[:interagiu_com]-(cocoActors)
       WHERE NOT (p)-[:ACTED_IN]->()<-[:ACTED_IN]-(cocoActors) AND p <> cocoActors
       RETURN cocoActors AS Recommended, count(*) AS Strength ORDER BY Strength DESC


![Imagem 5](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/Imagens/notinteract.png)

## Caminhos

- Cypher utilizado para encontrar o menor caminho entre dois personagens:

        MATCH (a:Person { name: 'Valjean' }),(b:Person { name: 'Listolier' }), p = shortestPath((a)-[*..15]-(b))
        RETURN p
  
![Image3](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/Imagens/shorterpath1.png)

- Cypher utilizado para encontra todos os caminhos entre dois personagens:

        MATCH (a:Person { name: 'Valjean' }),(b:Person { name: 'Tholomyes' }), p = allShortestPaths((a)-[*]-(b))
        RETURN p
 ![Image4](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/Imagens/allpath2.png)
