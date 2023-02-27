# listenum="770652519 "
def eface_espace(listenum):
    tab=""
    for i in listenum:
        if i!=" ":
            tab+=i
    return tab



def eface_virgule(mot):
    normal=""
    for lettre  in mot:
        if lettre!="," :
            normal+=lettre
    return normal


        

def gerer_format(date):
    for i in date:
        if i=="/" or "0"<=i<="9"  :
            continue
        else:
            date=date.replace(i,"/")
    return date


def divise_date(datediv):
    datediv=datediv.split("/")
    return datediv





def valide_num(numero):
    if  (numero[:2] in ["77","78","76","70","75"]) and len(numero)==9:
        return True
    else:
        return False    
    

def chiffre_correct(note):
    if '0'<=note<='20' :
        return True
    else:
        return False
    

def nbre_matiere_correct(nbrematiere):
    if nbrematiere>=1 :
        return True
    else:
        return False
def matiere_existe(matiere):
    if matiere in ["francais","svt","math","HG","Anglais","PC"]:
        return True
    else:
        return False
    
def note_correct(notes):
    recupernot=""
    for i in notes:
        if i!="|" and chiffre_correct(i)==True:
            recupernot+=i
            return recupernot
        else:
            return False
    
    

    
    

def menu():
    print("Afficher tout")
    print("Trier et afficher (par l' ordre croissant de la moyenne) ")
    print("Rechercher selon un critere(telephone,nom, prenom,ou classe) ")
    print("Modification de notes pour un étudiant choisit par l’utilisateur en donnant le numéro de téléphone.")
    print("Sortir (permet de terminer l’application)")

def menu():

    print("  1)  D’afficher les informations (Valide ou invalide ; au choix : ")
    print("  2)  D’afficher une information (par son numéro) : ")
    print("  3)  D’afficher les cinq premiers : ")
    print("  4)  D’ajouter une information en vérifiant la validité des informations données. : ")
    print("  5)  De modifier une information invalide ensuite le transférer dans la structure où setrouve les informations valides : ")

    choix=input("donnner votre choix : ")


def numero_valide(numero):
    #numero_colec=""
    for i in range(len(numero)):
        if ("A"<=numero[i]<="Z" or "0"<=numero[i]<="9") and len(numero)==7 :
            #numero_colec=numero
            return numero
        else :
            return False
        
        
def  prenom_valide(prenom):
    for i in range(len(prenom)):
        if ("A"<=prenom[0]<="Z" or "a"<=prenom[0]<="z") and len(prenom)>=3:
            return True
        else:
            return False
        

def nom_valide(nom):
    for i in range(len(nom)):
        if ("A"<=nom[0]<="Z" or "a"<=nom[0]<="z") and len(nom)>=2:
            return True
        else:
            return False
        

def anne_bisextile_valide(annee):
    if( annee%4==0 or (annee%4==0 and annee%100!=0 )and annee>=1) or ((annee%4==0 and (annee%100!=0 and annee%400==0 ))  and annee>=1):
        return True
    else:
        return False
    

def mois_valide(mois):
    if mois in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09","10","11","12"]:
        return True
    else:
        return False

    
def jour_valide(jour):
    if jour in ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]:
        return True
    else:
        return False
    
def date_de_naissance_valide(annee,mois,jour):
    if (jour_valide(jour)==True and mois_valide(mois)==True) :
        return True
    else:
        return False

def classe_valide(classe):
    if classe in ["6emA", "5emA","4emA","3emA","6emB","5emB","4emB","3emB"]:
        return True
    else:
        return False


def classe_format_valide(classeformat):
    if len(classeformat)<1:
        return "invalide"
    if classeformat[0] in ["6","5","4","3"] and classeformat[-1] in ["A","B"] :
        return classeformat[0]+"em"+classeformat[-1]
    else:
        return "invalide"

def divise_note(notediv):
    notediv=notediv.split("#")
    return notediv
  # print(ligne)
def convert_row(row):
   return """<etudiant="%s">
   <code>%s</code>
   <numero>%s</numero>
   <nom>%s</nom>
   <prenom>%s</prenom>
   <dn>%s</dn>
   <classe>%s</classe>
</etudiant>""" % (
   row[0], row[1], row[2], row[3], row[4], row[5], row[6])

#print ('\n'.join(csv_f.apply(convert_row, axis=1)))


fichier='/home/salimata/Bureau/algorithme/exoalgophython/projet.csv'
import csv              
f = open(fichier)
csv_f = csv.reader(f)  
entete=next(csv_f ) 
print(entete)
for ligne in csv_f:
   convert_row(ligne) 
    
 
# valide=divise_note(h)
# print(valide)
