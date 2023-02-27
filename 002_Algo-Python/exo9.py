from P5_Python_FSB001.mes_fonctions import*
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
        while chiffre_correct(note_devoir)!= True: 
            note_devoir=input("vous devez donner un chiffre compris entre 1 et 20 : ")
        note_projet=input("donner votre note de projet svp : ")
        while chiffre_correct(note_projet)!= True:
            note_projet=input("vous devez donner un chiffre compris entre 1 et 20 : ")
        note_examen=input("donner votre note d'examen svp : ")
        while chiffre_correct(note_examen)!= True:
            note_examen=input("vous devez donner un chiffre compris entre 1 et 20 : ")
        moyenne=format(((float(note_examen) + float(note_devoir) + float(note_projet))/3),'.2f')
        moyenne = str (moyenne)
        dict_donne=[prenom,nom,telephone,classe,note_devoir,note_projet,note_examen,moyenne]
        list_etudiant.append(dict_donne)