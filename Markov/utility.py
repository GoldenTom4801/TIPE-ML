
import re

# Fonctions utiles dans tout le projet 

def minuscule(mot):
    return mot.lower()

def brutVersListe(texte):
    liste = texte.split("\n")
    liste = list(map(lambda phrase : phrase.split(), liste))
    listeMot = []
    for listePhrase in liste:
        listeMot += listePhrase
    return listeMot
        
def read_file(chemin):
    with open(chemin, 'r') as f:
        listeMots =  brutVersListe(f.read())
        return list(map(minuscule, listeMots))
    