import utility
import random
from _operator import concat

class Generateur(object):
    def __init__(self, output_file):
        self.output_file = open(output_file, 'w')
        self.adj_name = "data_perso/adjectif.txt"
        self.article_name = "data_perso/article.txt"
        self.verbe_name = "data_perso/verbe.txt"
        self.nom_name = "data_perso/nom.txt"
        self.adv_name = "data_perso/adverbe.txt"
        self.prep_name = "data_perso/preposition.txt"
        
        self.preps = utility.read_file(self.prep_name)
        self.advs = utility.read_file(self.adv_name)
        self.adjs = utility.read_file(self.adj_name)
        self.articles = utility.read_file(self.article_name)
        self.noms = utility.read_file(self.nom_name)
        self.verbes = utility.read_file(self.verbe_name)
        
        
    def __enter__(self):
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.output_file.close()
    
        
    def gen_syn_nominale(self):
        article = random.choice(self.articles)
        nom = random.choice(self.noms)
        prep = self.gen_syn_prep()
        adj = self.gen_syn_adj()
        
        return utility.concat(article, nom, prep, adj)

    def gen_syn_verbale(self):
        verbe = random.choice(self.verbes)
        complement = self.gen_phrase_nominale()
        return utility.concat(verbe, complement)
    
    def gen_syn_adv(self):
        adv = random.choice(self.advs)
        synAdv = ""
        
        if random.random() < 0.2:
            synAdv = self.gen_syn_adv()
        
        return utility.concat(synAdv, adv)

        
    def gen_syn_prep(self):
        prep = random.choice(self.preps)
        syn_nominal = self.gen_syn_nominale()
        
        return utility.concat(prep, syn_nominal)
    
    def gen_syn_adj(self):
        adj = random.choice(self.adjs)
        
        return adj
        
    def gen_phrase(self):
        nominal = self.gen_syn_nominale()
        verbal = self.gen_syn_verbale()
        return utility.concat(nominal, verbal)
    
    def gen_paragraphe(self, n):
        phrases = [gen_phrase() for i in range(n)]
        return "\n".join(phrases)
    
    def output_phrase(self):
        self.output_file.write(self.gen_phrase())
        
    def output_paragraph(self,n):
        self.output_file.write(self.gen_paragraphe(n))
    
    
        
    
    
