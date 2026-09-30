import csv 
import math 
import random

NB_REQUETES = 100

T_min = 1
T_max = 10 

M = 5
N = 3

MOYENNE = 4096
VARIANCE = 1024

FICHIER = "trace.csv"



ecart_type = math.sqrt(VARIANCE)

date = 0
adresse = 0

with open(FICHIER, mode='w', newline='') as f:
    writer = csv.writer(f)

    for i in range(NB_REQUETES):
        #date
        date +=random.randint(T_min, T_max)

        #type 
        if i % (M + N) < M:
            type_requete = "r"
        else:
            type_requete = "w"

        taille = int(round(random.gauss(MOYENNE, ecart_type)))

        while taille<=0:
            taille = int(round(random.gauss(MOYENNE, ecart_type)))

        writer.writerow([
            i,
            date,
            type_requete,
            adresse,
            taille,
        ]
        )
        adresse += taille

print("trace generee dans ", FICHIER)
        
