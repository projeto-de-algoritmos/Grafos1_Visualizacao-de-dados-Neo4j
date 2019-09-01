import json

with open('actors.json', 'r') as f:
    actors = json.load(f)

# print(actors["nodes"][0]["id"])

create_actors = ""

for actor in actors["nodes"]:
    create_actors += "CREATE (" + actor["id"] + \
        ": Person {name: '" + actor["id"] + "'})\n"

f = open("actors.txt", "w+")

f.write(create_actors)

f.close()

# criar relações

relations = ""

for relation in actors["links"]:
    relations += "CREATE (" + relation["source"] + \
        ")-[:interagiu_com {quantidade_de_interacoes:['" + \
        str(relation["value"]) + "']}]->(" + relation["target"] + ")\n"

f = open("relations.txt", "w+")
f.write(relations)
f.close()
