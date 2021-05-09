import chomsky

with chomsky.Generateur("test_output/test.html") as gen:
    print(gen.gen_phrase())
    gen.output_phrase()
    
    #print(gen.gen_phrase())
    