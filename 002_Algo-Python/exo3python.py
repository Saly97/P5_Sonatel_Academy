def maj_point(phrase):
    #if (chaine[0]>="A" and chaine[0]<="Z"):
     if ("A"<= phrase[0]<="Z") and (phrase[-1] in ["!",".","?"]):  
         return True
     else:
         return False
     
def caractaire(phrase):
    for c in range(len(phrase)):
        if (("A"<= phrase[c]<="Z") or (phrase[-1] in ["!",".","?"]) or ("a"<= phrase[c]<="z") or ('0'<phrase[c]<'9') ):
            return False
        else:
            return True 
        
def longuerphrase(phrase):  
    if len(phrase)<=25:
        return True
    else:
        return False
    
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




#phrase=input("donner un groupe de phrases \n")
phrase ="""Demander des informations concernant !l’étudiant tant que l’utilisateur désire continuer.
Vous devez demander le téléphone, nom, prénom, classe, note de devoir, note de projet et
note d’examen pour ensuite? Calculer la moyenne et. afficher le résultat sous forme du tableau
ci- dessous .Lorsque l’utilisateur terminera sa saisie."""

t=[]
chaine=""
for c in phrase:
    chaine+=c
if (c=="!" or c=="." or c=="?"):
    t.append(chaine)
# if maj_point(t)==True and caractaire(t)==False and longuerphrase(t):
#     print(t)
