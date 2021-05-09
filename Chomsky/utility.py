#Fonctions qui servent pour le reste du projet

def read_file(chemin):
    with read(chemin, 'r') as f:
        return f.readlines()