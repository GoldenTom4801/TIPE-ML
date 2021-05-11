
# Fonctions utiles dans tout le projet 

def read_file(chemin):
    with open(chemin, 'r') as f:
        return f.read().split(" ")