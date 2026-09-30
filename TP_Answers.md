# TP Workload — Réponses

## Exercice 2 — Exploration de traces I/O

**Objectif :** concevoir un script permettant d'extraire les caractéristiques des traces I/O.

Le script utilisé est **`q1_q15.py`**. Il lit les cinq fichiers `trace_0.csv` à `trace_4.csv` avec `csv.DictReader`.

Chaque requête contient les champs :

```text
index, timestamp, mode, address, size, pid
```

où :
- `timestamp` est la date d'envoi ;
- `mode` vaut `r` pour une lecture et `w` pour une écriture ;
- `address` est l'adresse du premier octet accédé ;
- `size` est la taille de la requête en octets ;
- `pid` est le processus à l'origine de la requête.

Chaque trace contient **200 000 requêtes**.

---

## 1. Le plus grand nombre de requêtes

### Résultat

| Trace | Nombre de requêtes |
|---|---:|
| `trace_0.csv` | 200 000 |
| `trace_1.csv` | 200 000 |
| `trace_2.csv` | 200 000 |
| `trace_3.csv` | 200 000 |
| `trace_4.csv` | 200 000 |

**Réponse :** les cinq traces sont ex æquo avec **200 000 requêtes**.

### Logique

Pour chaque fichier, on compte simplement le nombre de lignes de requêtes. Comme toutes les traces ont le même nombre de requêtes, elles sont toutes concernées.

---

## 2. La plus grande date d'envoi

### Résultat

| Trace | Plus grand timestamp |
|---|---:|
| `trace_0.csv` | 400 000 |
| `trace_1.csv` | 902 217 |
| `trace_2.csv` | **16 640 000** |
| `trace_3.csv` | 14 998 980 |
| `trace_4.csv` | 1 600 000 |

**Réponse :** `trace_2.csv`.

### Logique

Pour chaque trace, on cherche le plus grand `timestamp`. La trace qui possède la valeur maximale correspond à la plus grande date d'envoi.

---

## 3. Le plus grand nombre d'écritures

### Résultat

| Trace | Nombre d'écritures |
|---|---:|
| `trace_0.csv` | 59 955 |
| `trace_1.csv` | 20 000 |
| `trace_2.csv` | 0 |
| `trace_3.csv` | **200 000** |
| `trace_4.csv` | 198 007 |

**Réponse :** `trace_3.csv`.

### Logique

On parcourt toutes les requêtes et on compte celles dont le champ `mode` vaut `w`.

---

## 4. Le plus grand nombre d'octets écrits

### Résultat

| Trace | Octets écrits |
|---|---:|
| `trace_0.csv` | 1 918 560 |
| `trace_1.csv` | 451 239 936 |
| `trace_2.csv` | 0 |
| `trace_3.csv` | 3 276 800 000 |
| `trace_4.csv` | **3 679 416 320** |

**Réponse :** `trace_4.csv`.

### Logique

Pour chaque requête d'écriture (`mode == "w"`), on ajoute sa taille au total :

```text
total_octets_ecrits = somme des size pour les requêtes w
```

---

## 5. La plus grande médiane du nombre d'octets lus

### Résultat

| Trace | Médiane des tailles lues |
|---|---:|
| `trace_0.csv` | 32 |
| `trace_1.csv` | **24 576** |
| `trace_2.csv` | 4 096 |
| `trace_3.csv` | aucune lecture |
| `trace_4.csv` | 20 480 |

**Réponse :** `trace_1.csv`.

### Logique

On garde uniquement les requêtes de lecture (`mode == "r"`), puis on calcule la médiane de leurs tailles.

Pour `trace_3.csv`, il n'y a aucune lecture, donc aucune médiane ne peut être calculée.

---

## 6. Le plus grand système de stockage ciblé par la trace

### Résultat

| Trace | Fin de l'espace ciblé |
|---|---:|
| `trace_0.csv` | 6 400 000 |
| `trace_1.csv` | 1 073 764 069 |
| `trace_2.csv` | 778 313 728 |
| `trace_3.csv` | 134 234 034 |
| `trace_4.csv` | **3 717 173 248** |

**Réponse :** `trace_4.csv`.

### Logique

Une requête commence à `address` et accède à `size` octets.

La fin de la zone ciblée est donc approximativement :

```text
address + size
```

On cherche ensuite la valeur maximale parmi toutes les requêtes de la trace.

---

## 7. Le plus grand nombre de processus distincts

### Résultat

| Trace | Nombre de processus |
|---|---:|
| `trace_0.csv` | 2 |
| `trace_1.csv` | 8 |
| `trace_2.csv` | 2 |
| `trace_3.csv` | **10** |
| `trace_4.csv` | 5 |

**Réponse :** `trace_3.csv`.

### Logique

On récupère tous les `pid` de la trace et on les place dans un ensemble (`set`). Un ensemble ne garde qu'une seule occurrence de chaque PID.

Le nombre d'éléments de cet ensemble donne le nombre de processus distincts.

---

## 8. Le processus avec le plus grand nombre de requêtes

### Résultat

| Trace | PID | Nombre de requêtes |
|---|---:|---:|
| `trace_0.csv` | 6 | 159 860 |
| `trace_1.csv` | 2196 | 40 157 |
| `trace_2.csv` | 9999 | 198 007 |
| `trace_3.csv` | 11 | 59 760 |
| `trace_4.csv` | 3981 | 40 138 |

### Logique

Pour chaque trace, on compte le nombre d'apparitions de chaque `pid`. Le PID qui apparaît le plus souvent est celui qui a envoyé le plus grand nombre de requêtes.

---

## 9. Plusieurs requêtes envoyées en parallèle

### Résultat

| Trace | Requêtes en parallèle |
|---|---|
| `trace_0.csv` | Non |
| `trace_1.csv` | **Oui** |
| `trace_2.csv` | Non |
| `trace_3.csv` | Non |
| `trace_4.csv` | Non |

**Réponse :** `trace_1.csv`.

### Logique

On compte combien de requêtes possèdent le même `timestamp`.

Si deux requêtes ou plus ont exactement le même timestamp, elles sont considérées ici comme envoyées en parallèle.

---

## 10. Une taille de requête constante

### Résultat

| Trace | Taille constante |
|---|---|
| `trace_0.csv` | **Oui** |
| `trace_1.csv` | Non |
| `trace_2.csv` | Non |
| `trace_3.csv` | **Oui** |
| `trace_4.csv` | Non |

**Réponse :** `trace_0.csv` et `trace_3.csv`.

### Logique

On récupère toutes les valeurs de `size` dans un ensemble.

Si l'ensemble ne contient qu'une seule valeur, alors toutes les requêtes ont la même taille.

---

## 11. Une taille de requête suivant une loi normale

**Question non traitée dans le script actuel.**

### Logique

Pour tester cette propriété, il faut observer la répartition des valeurs de `size`. Une approche simple consiste à faire un histogramme des tailles et à vérifier si la distribution présente approximativement une forme en cloche, centrée autour d'une moyenne.

Cette question n'a pas été déterminée dans la version actuelle de l'analyse.

---

## 12. Le plus long stream de lecture

### Résultat

| Trace | Plus longue suite de lectures |
|---|---:|
| `trace_0.csv` | 33 |
| `trace_1.csv` | 900 |
| `trace_2.csv` | **200 000** |
| `trace_3.csv` | 0 |
| `trace_4.csv` | 2 |

**Réponse :** `trace_2.csv`.

### Logique

On parcourt les requêtes dans l'ordre.

- si la requête est une lecture, on augmente le compteur courant ;
- si c'est une écriture, on remet le compteur à zéro ;
- on mémorise la plus grande valeur obtenue.

Ainsi, on obtient la plus longue suite de lectures consécutives.

---

## 13. Des requêtes identiques (hormis la date d'envoi)

**Question non traitée dans le script actuel.**

### Logique

Deux requêtes sont considérées comme identiques si les champs suivants sont identiques :

```text
mode + address + size + pid
```

Le `timestamp` est volontairement ignoré.

Il suffit donc de rechercher plusieurs occurrences d'une même combinaison de ces quatre champs.

Cette question n'a pas été déterminée dans la version actuelle de l'analyse.

---

## 14. Une erreur de formatage

**Question non traitée dans le script actuel.**

### Logique

Pour vérifier le formatage, il faut contrôler chaque ligne du CSV :

- présence des 6 colonnes ;
- `index`, `timestamp`, `address`, `size` et `pid` doivent être numériques ;
- `mode` doit être `r` ou `w`.

Une ligne qui ne respecte pas ces règles indique une erreur de formatage.

Cette question n'a pas été déterminée dans la version actuelle de l'analyse.

---

## 15. La plus longue exécution

### Résultat

| Trace | Durée |
|---|---:|
| `trace_0.csv` | 399 998 s |
| `trace_1.csv` | 902 208 s |
| `trace_2.csv` | **16 639 984 s** |
| `trace_3.csv` | 14 998 920 s |
| `trace_4.csv` | 1 599 992 s |

**Réponse :** `trace_2.csv`.

### Logique

On considère la durée de la trace comme :

```text
dernier timestamp - premier timestamp
```

On compare ensuite cette durée entre les cinq fichiers.

---

## Conclusion

D'après l'analyse réalisée dans `q1_q15.py` :

- **Trace 0** : taille constante de requête.
- **Trace 1** : requêtes envoyées en parallèle et plus grande médiane des lectures.
- **Trace 2** : plus grande date d'envoi, plus long stream de lecture et plus longue durée.
- **Trace 3** : plus grand nombre d'écritures, taille constante et plus grand nombre de processus distincts.
- **Trace 4** : plus grand nombre d'octets écrits et plus grand espace de stockage ciblé.

Les questions **11, 13 et 14** restent à analyser.
