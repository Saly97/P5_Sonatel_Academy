from mes_fonctions import*
# nombre_etudiant=2
# booleen = True
# while True:
list_etudiant=[]
list_etudiants=[]
reponse=''
en_tete = ["prenom", "nom","telephone","classe","note_devoir","note_projet","note_examen","moyenne"]
list_etudiant.append(en_tete)
while reponse != 'non':
    demande=input("voulez vous nous donner tes informations svp ? repondez par oui ou non : ")
    while demande!="oui" and demande!="non":
        demande=input("vous avez commis une erreur ? repondez par oui ou non svp : ")  

    if demande=="non":
        print("vous n'etes pas un etudiant donc donner la place a un autre")
        reponse=demande  
    
    else:    
        moyenne=""
        prenom=input("donner votre prenom svp : ")
        nom=input("donner votre nom svp : ")
        telephone=input("donner votre numero de telephone  svp : ")
        if valide_num(telephone)==True:
            tab_etudiants=[]
            tab_etudiants.append(telephone)
        else:
            while  valide_num(telephone)!=True:
                telephone=input("le numero de telephone n est pas corect donner un autre : ")   
        classe=input("donner votre classe svp :  ")
        note_devoir=input("donner votre note de devoir svp : ")
        note_projet=input("donner votre note de projet svp : ")
        note_examen=input("donner votre note d'examen svp : ")
        moyenne=(float(note_examen) + float(note_devoir) + float(note_projet))/3 
        moyenne = str (moyenne)
        dict_donne=[prenom,nom,telephone,classe,note_devoir,note_projet,note_examen,moyenne]
        list_etudiant.append(dict_donne)

for ligne in list_etudiant :
    for i in range(len(ligne)) :
        print (ligne[i],end=(15-len(ligne[i]))*" ")
    print ('\n')

# list_etudiant =  [['saly', 'ba', '771212121' , 'rte', '11', '13', '14', '12.666666666666666'], ['serigne', 'diop', '771211121', 'hgfds', '11', '1', '2', '4.666666666666667']]

    


            


