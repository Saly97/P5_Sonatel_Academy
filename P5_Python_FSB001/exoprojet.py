import csv
from P5_Python_FSB001.mes_fonctions import*
tab_etudiant_valide=[]
tab_etudiant_invalide=[]
tab_etudiant_note=[]
tab_etudiant_valide_note=[]
matiere={}
fichier='/home/salimata/Bureau/algorithme/exoalgophython/projet.csv'
def projet_donne(fichier):

    file=open(fichier)
    fichiercsv=csv.reader(file)

# for ligne in fichiercsv:
#     print(ligne)
    for x in fichiercsv:

        nom=x[2]

        nom_etudiant_valide=nom_valide(nom)

    if nom_etudiant_valide==True:

        prenom=x[3]
        prenom_etudiant_valide=prenom_valide(prenom)
        
        if prenom_etudiant_valide==True:
            
            numero=x[1]
            
            numero_etudiant_valide=numero_valide(numero)
            
            if numero_etudiant_valide!=False:
                numero_corect=numero_etudiant_valide
                
                date=x[4]
                format=gerer_format(date)
                divise=divise_date(format)
            
                try:
                    date_naissance_etudiant_valide= date_de_naissance_valide(divise[2],str(divise[1]),str(divise[0]))
                
                except:
                    print("invalide")
                
                if date_naissance_etudiant_valide==True:
                    
                    classe=x[5]
                    classe_etudiants_sans_espace=eface_espace(classe)
                    classe_etudiant_format=classe_format_valide(classe_etudiants_sans_espace)
                    classe_etudiant_valide=classe_valide(classe_etudiant_format) 
                    
                                    
                    if classe_etudiant_valide!=False:
                        classe_correct=  classe_etudiant_format

                        note=x[6]
                        chiffre=divise_note(note)
                        tab_matiere=[]
                        for i in chiffre:
                            try:
                                nouvelle_note = i.replace("[","-").replace(",",".").replace("|","-").replace(":","-").replace("]","-").split("-")
                                
                                matiere[nouvelle_note[0]]={ 
                                    "devoir": nouvelle_note[1:-2],
                                    "examen": nouvelle_note[-2]
                                        }
                                tab_matiere.append(matiere)
                                print(tab_matiere)
                                
                                somme_des_devoirs = 0.0
                                moyenne_des_devoirs=0.0
                                for d in matiere[nouvelle_note[0]]["devoir"]:
                                    somme_des_devoirs+=float(d)
                                
                                    moyenne_des_devoirs = somme_des_devoirs/len(matiere[nouvelle_note[0]]["devoir"])
                                
                            except Exception as e:
                                        ""
                        
                            tab_etudiant_valide.append([x[0], numero_corect,x[2],x[3],x[4],classe_correct])
                    
                        

                    else:
                        tab_etudiant_invalide.append(x)
                else:
                    tab_etudiant_invalide.append(x)
            else:
                tab_etudiant_invalide.append(x)
        else:
            tab_etudiant_invalide.append(x)   
        
    return tab_etudiant_invalide,tab_etudiant_valide



print(projet_donne(fichier))

def affiche_valide_sans_notes(fichier) :
    tabinv,tabv=projet_donne(fichier)

    print("___________________________________________________________________________________________________________________________________")
    print('|  '+"code"+(20-len("code"))*" "+ "|  "+"numero"+(20-len("numero"))*" "+'|  '+"nom"+(20-len("nom"))*" "+'|  '+"prenom"+(20-len("prenom"))*" "+'|  '+"date de naissance"+(20-len("date de naissance"))*" "+'|  '+"classe")
    print("___________________________________________________________________________________________________________________________________")
    for liste in tabv:
        for element in liste:
            print('|  '+element+(20-len(element))*" ",end="")
        print("\n")

def affiche_invalide(fichier) :
    tabinv,tabv=projet_donne(fichier)
    for liste in tabinv:
        for element in liste:
            print('|  '+element+(10-len(element))*" ",end="")
        print("\n")

#essai="['Anglais': {'devoir': ['10.5', '9'], 'examen': '15'}, 'PC': {'devoir': ['10', '13'], 'examen': '11'}]"
# def affiche_valide_notes(fichier) :
#     tabinv,tabv,notev=projet_donne(fichier)
#     for liste in notev:
       
#         for element in liste:
#             print('|  '+element+(10-len(element))*" ",end="")
            
#         print("\n")

# def affichage():
#     print("================================================================================================================================")
#     print("||                               MENU                                                                                          ||")
#     print("================================================================================================================================")
#     print("|| 1)  D’afficher les informations (Valide ou invalide ; au choix :                                                            ||")
#     print("|| 2)  D’afficher une information (par son numéro) :                                                                           ||")
#     print("|| 3)  D’afficher les cinq premiers :                                                                                          ||")
#     print("|| 4)  D’ajouter une information en vérifiant la validité des informations données. :                                          ||")
#     print("|| 5)  De modifier une information invalide ensuite le transférer dans la structure où setrouve les informations valides :     ||")
#     print("=================================================================================================================================")

# def menu(fichier):
#     affichage()
#     while True:
#         choix=input("donnner votre choix : ")
#         if choix=="1":
#             info=projet_donne(fichier)
        
#             deuxieme_choix=input("donner a pour tableau invalide b pour tableau valide : ")
#             if deuxieme_choix=="a":
#                 affiche_invalide(fichier)
#                 affichage()
#             else:
#                 affiche_valide_sans_notes(fichier)
#                 menu(fichier)
#         if choix==2:
#                     pass    
        




