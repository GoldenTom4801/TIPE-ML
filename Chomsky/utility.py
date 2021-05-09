#Fonctions qui servent pour le reste du projet

def read_file(chemin):
    with open(chemin, 'r') as f:
        return f.read().split("\n")