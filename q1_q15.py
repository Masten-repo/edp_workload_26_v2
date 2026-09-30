import math 
import csv 
import statistics
from collections import Counter 

FICHIERS = [
    "trace_0.csv",
    "trace_1.csv",
    "trace_2.csv",
    "trace_3.csv",
    "trace_4.csv",
]


def lire_trace(fichier):
    requetes = []

    with open(fichier, 'r') as f:
        reader = csv.DictReader(f)

        for ligne in reader:
            requetes.append({
                "index" : int(ligne["index"]),
                "timestamp" : int(ligne["timestamp"]),
                "mode" : ligne['mode'],
                "address" : int(ligne["address"]),
                "size" : int(ligne["size"]),
                "pid" : int(ligne["pid"]),

            })

    return requetes


traces= {}

for fichier in FICHIERS:
    traces[fichier] = lire_trace(fichier)


print ("\n 1- Plus grand nbr de requetes :")



for fichier, requetes in traces.items():
    print(fichier, ":", len(requetes))


print("\n 2- Plus grande date d'envoi :")

for fichier, requetes in traces.items():
    print(fichier, ":", max(r["timestamp"] for r in requetes))



print("\n 3- Plus grand nombre decriture :")

for fichier, requetes in traces.items():
    nombre = sum(r["mode"] == "w" for r in requetes)
    print(fichier, ":", nombre)


print("\n 4- plus grand nombre d'octts ecrits")

for fichier, requetes in traces.items():
    total = sum(r["size"] for r in requetes if r["mode"] == "w")
    print(fichier, ":", total)


print("\n 5- la plus grande mediane du nombre d'ectets lus")

for fichier, requetes in traces.items():
    tailles = [r["size"] for r in requetes if r["mode"] == "r"]

    if len(tailles) > 0:
        mediane = statistics.median(tailles)
        print(fichier, ":", mediane)
    else:
        print(fichier, ": aucune lecture")

print("\n 6- leplus grand sys de stockage cible par la trace")

for fichier, requetes in traces.items():
    fin = max(r["address"] + r["size"] for r in requetes)
    print(fichier, ":", fin)


print("\n 7 - le plus grand nbr de processus distincs")

for fichier, requetes in traces.items():
    proc = set(r["pid"] for r in requetes)
    print(fichier, ":" , len(proc))


print("\n 8 - processus avec le plus grand nbr de requetes")

for fichier, requetes in traces.items():
    compteur = Counter(r["pid"] for r in requetes )
    pid, nombre = compteur.most_common(1)[0]
    print(fichier, ":", pid, ":",nombre)


print("\n 9 - requetes en //")

for fichier, requetes in traces.items():

    compteur = Counter(r["timestamp"] for r in requetes)

    parallele = any(nombre > 1 for nombre in compteur.values())

    if parallele:
        print(fichier, ": OUI")
    else:
        print(fichier, ": NON")


print("\n 10 - taille constante")

for fichier, requetes in traces.items():
    tailles = set(r["size"] for r in requetes)
    if len(tailles) == 1:
        print(fichier, ": OUI")
    else:
        print(fichier, ": NON")


print("\n 12 - plus long steam de lecture")

for fichier, requetes in traces.items():
    courant = 0
    maximum = 0 

    for i in requetes:
        if i["mode"] == "r":
            courant += 1
            if courant > maximum:
                maximum = courant
        else:
            courant = 0

    print(fichier, ":", maximum)

print("\n15 - Plus longue execution")

for fichier, requetes in traces.items():

    debut = requetes[0]["timestamp"]
    fin = requetes[-1]["timestamp"]

    duree = fin - debut

    print(fichier, ":", duree, "secondes")
