import markov

with markov.GenMarkov("data/fables_fontaine.txt", "output/test_fables_fontaine.txt") as gen:
    #print(gen.genParagraphe("les"))
    gen.writeParagraphe("les")