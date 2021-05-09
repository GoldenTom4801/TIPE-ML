import utility
import random

class Generateur(object):
    def __init__(self, output_file):
        self.output_file = open(output_file, 'w')
        self.adj_name = "data/adjectif.txt"
        self.article_name = "data/article.txt"
        self.verbe_name = "date/verbe.txt"
        self.nom_name = "data/nom.txt"
        
        self.adjs = utility.read_file(self.adj_name)
        self.articles = utility.read_file(self.article_name)
        self.noms = [] = utility.read_file(self.nom_name)
        self.verbes = [] = utility.read_file(self.verbe_name)
    
        
    def gen_phrase_nominale(self):
        article = random.choice(self.articles)
        nom = random.ch&oice(self.noms)
        adj = random.choice(self.adjs)
        return article + " " + nom + " " + adj
    
    def gen_phrase_verbale(self):
        verbe = random.choice(self.verbes)
        complement = self.gen_phrase_nominale()
        return verbe + " " + complement
    
    def gen_phrase(self):
        nominal = self.gen_phrase_nominale()
        verbal = self.gen_phrase_verbale()
        return nominal + " " + verbal
    
    def output_phrase(self):
        self.output_file.write(self.gen_phrase(self))
    
    
        
    
    
