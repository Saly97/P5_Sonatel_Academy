    
def decouphrase(phrase):
    t=[]
    phrasecoupé=""
    for i in phrase:
        if i not in ["!",".","?"]:
            phrasecoupé+=i
            
        else: 
            phrasecoupé+=1
            t.append(phrasecoupé)
            phrasecoupé=""
    return t
tab=decouphrase("Sdrghjk salimeata hjhuyfg .jjiuioljjy fh ?hkjhkjjhg§!kl")
print(tab)