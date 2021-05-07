# TIPE-ML

Ce TIPE a pour but d'étudier la génération automatique de texte par la création de texte aléatoire cohérent. A partir d'un corpus initial de texte, on entraine un alogrithme qui par la suite pourra des textes intelligibles. Pour cela, plusieurs pistes sont étudiés (ayant des complexités d'implémentations et des performances différentes). Les solutions retenues sont les suivantes :
- La génération suivant un schéma de Markov 
- La génération suivant une structure de langage issue de la classification des langages de Chomsky
- La génération par réseau de neuronne 


- Schéma de Markov : Solution naïve
On construit le texte de façon itérative mot à mot. A chaque mot (ou vecteur de mot), on associe une certaine probabilité d'avoir un prochain mot. L'entrainement de l'algorithme se fait à partir d'un corpus de texte. 
On extrait le vocabulaire. Pour chaque mot présent dans le texte, on regarde l'ensemble des mots suivants que l'on dénombre avec multiplicité. On associe ensuite une probabilité suivant la multiplicité.
On peut ainsi générer un texte de longueur arbitraire.

Possibilités:
- Forcer
