# Lista 1 sobre grafos da matéria Projeto de Algoritmos
Foi utilizado um Json com as interações entre os personagens do filme Les Miserable, transformado-o para a linguagem cypher foram adicionados os nós (Personagens) e as relações entre eles no banco orientado a grafo Neo4j.

## Preparando o banco de dados

- Faça o download do [Neo4j](https://neo4j.com/) e o execute
- Crie um novo projeto
- Adicione os [Atores](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/actors.txt)
- Adicione as [Interações](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/relations.txt)

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
       WHERE NOT (p)-[:interagiu_com]->()<-[:interagiu_com]-(cocoActors) AND p <> cocoActors
       RETURN cocoActors AS Recommended, count(*) AS Strength ORDER BY Strength DESC


![Imagem 5](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/Imagens/notinteract.png)

## Caminhos

- Cypher utilizado para encontrar o menor caminho entre dois personagens:

        MATCH (a:Person { name: 'Valjean' }),(b:Person { name: 'Listolier' }), p = shortestPath((a)-[*..15]-(b))
        RETURN p
  
![Image3](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/Imagens/shorterpath1.png)

- Cypher utilizado para encontra todos os menores caminhos entre dois personagens:

        MATCH (a:Person { name: 'Valjean' }),(b:Person { name: 'Tholomyes' }), p = allShortestPaths((a)-[*]-(b))
        RETURN p
 ![Image4](https://github.com/projeto-de-algoritmos/Lista1_MikhaelleBueno_GuilhermeDeusdara/blob/master/Imagens/allpath2.png)
