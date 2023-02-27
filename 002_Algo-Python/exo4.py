#nbre_valide=input("donner a liste des numeros")
listenum="770652519,   25193445777,76654445, 77 229 09 02, 3345556 78 567 45 56 "
def eface_espace(listenum):
    tab=""
    for i in listenum:
        if i!=" ":
            tab+=i
    return tab
#newlist= eface_espace(listenum)
#print(newlist)

def valide_num(newlist):
    valide=[]
    invalide=[]
    numero=""
    for j in newlist:
        if j!=",":
            numero+=j
            #print(j, " ",numero) 
        elif  (numero[:2] in ["77","78","76","70","75"]) and len(numero)==9:
            valide.append(numero)
            #print("Valide  ",valide) 
            numero=""
            #return valide
        else:
             invalide.append(numero)
            # print("invalide  ",invalide) 
             numero=""
        #return invalide
    return [valide, invalide]

             
#listenum="77065  2519"
#print(validé_num(eface_espace(listenum)))
num_sans_espace =eface_espace(listenum)
valide_num_n=valide_num(num_sans_espace)
print(valide_num_n)
