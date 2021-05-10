import chomsky

with chomsky.Generateur("test_output/test.txt") as gen:
    gen.output_paragraphe(50)
    
    #print(gen.gen_phrase())
    