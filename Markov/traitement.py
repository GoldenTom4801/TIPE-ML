import markov

def evaluation(path):
    print("Evaluation de phrase : Commencer (Enter)")
    gen = markov.GenMarkov("data/fables_fontaine.txt", "void")
    
    f = open(path, "w")
    
    phraseAcc = []
    phraseRef = []
    
    phrase = gen.genPhrase("les")
    print(phrase)
    a = input("Garder (O/N), Quitter : Q")
    while a!="Q":
        if a == "O":
            phraseAcc.append(phrase)
        elif a == "N":
            phraseRef.append(phrase)
        else:
            print("Erreur, phrase abandonnée")
        phrase = gen.genPhrase("les")
        print(phrase)
        a = input("Garder (O/N), Quitter : Q")
    
    parag_acc = "Phrases considérées comme satisfaisantes :\n" "\n\n".join(phraseAcc)
    parag_ref =  "Phrases non satisfaisantes :\n" "\n\n".join(phraseRef)
    texte =parag_acc + "\n\n\n\n" + parag_ref
    nbTot = len(phraseAcc) + len(phraseRef)
    tex_commenté = texte + "\n\n" + "Nombre de phrases total = {0} \n{1}% accepté {2}% refusé".format(nbTot, len(phraseAcc)/nbTot/100, len(phraseRef)/nbTot/100)
    f.write(tex_commenté)
    
    
    
path = "output/evaluation/phrases.txt"   
evaluation(path)