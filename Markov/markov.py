
import random
import utility


class GenMarkov:
    
    dic = {}
    texte = [] #Liste des mots du texte
    
    def __init__(self,path):
        self.texte = utility._read_file(path)
        self.constructionDic(self)
        
        
    #Comptage des mots
    def constructionDic(self):
        for ind in range(len(texte) - 1):
            if texte[ind] in dic:
                dic[texte[ind]].append(texte[ind + 1]) 
            else:
                dic[mot] = [texte[ind + 1]]
        
    #Donne le prochain mot
    #Prend directement en compte les multiplicités
    #Note Attention à la complexité spatiale
    def prochainMot(self, mot):
        return random.choice(dic[mot])
    
    def genTexte(self,longueur, motInitial = self.texte[0]):
        liste = [motInitial]
        for i in range(longueur -1):
            liste.append(self.prochainMot(liste[-1]))
        return liste
        
        