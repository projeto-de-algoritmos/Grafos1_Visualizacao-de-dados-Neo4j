import json

with open('actors.json', 'r') as f:
    actors = json.load(f)

create_actors = ""

for actor in actors["nodes"]:
    create_actors += "CREATE (" + actor["id"] + \
        ": Person {name: '" + actor["id"] + "'})\n"

f = open("actors.txt", "w+")

f.write(create_actors)

f.close()

# criar relações

relations = "MATCH"

for relation in actors["links"]:
    relations += "\n\t(" + relation["source"] + \
        ")-[:interagiu_com {quantidade_de_interacoes:['" + \
        str(relation["value"]) + "']}]-(" + relation["target"] + "),"

# retirando última vírgula
relations = relations[0:-1]

f = open("relations.txt", "w+")
f.write(relations)
f.close()
