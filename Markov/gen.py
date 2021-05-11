import markov

gen = GenMarkov("data/fables_fontaine.txt")
print(gen.genTexte(15, "les"))