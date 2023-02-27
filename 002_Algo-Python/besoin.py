for k in range(len(tab_couleur)):
    #for p in range(len(tab_position)):
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[5]):
            for i in range(long_matrice):
                for j in range(long_matrice):
                    matrice[i][long_matrice-i-1]=1
                    # matrice[i][i]=1
                    # matrice[i][j]=1                    
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[2]):
            for i in range(long_matrice):
                matrice[i][i]=1
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[0]):
            for i in range(long_matrice):
                matrice[0][1]=1
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[1]):
            for i in range(long_matrice):
                matrice[1][0] 
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[4]):
            for i in range(long_matrice):
                matrice[1][2]=1
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[3]):
            for i in range(long_matrice):
                matrice[2][1]=1
print(matrice)


                                      
     #  while(choix!="haut" and choix!="bas"):
#     choix=input("donner votre choix entre haut et bas ; ")
#     if(couleur== "rouge")and(choix=="haut"):
#         if i>j:
#             # matrice[i][j]==["\033[31m 1 \033[67m \033[32m"]
#             for  liste in matrice:
#                 for j in liste:
#                      matrice[i][j]=j
# print(matrice[i][j])
# # print(matrice)
# #             t=["\033[31m 1 \033[67m \033[32m"]
# # print(t)
# # print(t[0 ,1,2])
    
        
#             #  matrice==["\033[34m 1 \033[67m \033[34m"]
#              for  liste in matrice:
# #     for j in liste:
# #         print(j)
# # print(matrice)
# #
# couleur =""
# choix =""
# #couleur!="rouge"  F
# # or 
# # couleur!="bleu" V
        
  
             
                
# def affichage(tab):
#     #entete = tab[0]
#     print("_________________________________________________________________________________________________________________")
#     print("|{0:<15}|{1:<20}|{2:<15}|{3:<15}|{4:<15}|{5:<15}|{6:<15}|".format("code","numero","nom","prenom","date de naissance","classe","note"))
#     print("_________________________________________________________________________________________________________________")
#     diction = {}
        
#     entete = tab[0][0]
#     for i in range(1,len(tab)):
#         #print(tab[i])
#         diction['code']=tab[i][0]
#         diction['numero']=tab[i][1]
#         diction['nom']=tab[i][2]
#         diction['prenom']=tab[i][3]
#         diction['date de naissance']=tab[i][4]
#         diction['classe']=tab[i][5]
#         diction['note']=tab[i][6]
#         print(diction)
#         for k , keyv in diction.items1():
#                  print("{0:<15}|{1:<20}|{2:<15}|{3:<15}|{4:<15}|{5:<15}|{6:<15}".format(
#                  keyv['code'],
#                  keyv['numero'],
#                  keyv['nom'],
#                  keyv['prenom'],
#                  keyv['date de naissance'],
#                  keyv['classe'],
#                  keyv['note']))
#                  print("_________________________________________________________________________________________________________________")

#         # # #diction[entete]=tab[i]
#         #print(diction)
#         #for cle, valeur in diction.items():
          
#         #        pass
# def menu():

#     print("  1)  D’afficher les informations (Valide ou invalide ; au choix : ")
#     print("  2)  D’afficher une information (par son numéro) : ")
#     print("  3)  D’afficher les cinq premiers : ")
#     print("  4)  D’ajouter une information en vérifiant la validité des informations données. : ")
#     print("  5)  De modifier une information invalide ensuite le transférer dans la structure où setrouve les informations valides : ")

#     choix=input("donnner votre choix : ")
#     if choix=="1":
#         info=projet_donne()
       
#         deuxieme_choix=input("donner a pour tableau invalide b pour tableau valide : ")
#         if deuxieme_choix=="a":
#             affichage(info[0]) 
#         else:
#             affichage(info[1])
#             menu()
#     if choix==2:
#                 pass
# menu()    
        


    


# # # #for ligne in tab_etudiant_valide:
# # # #    print(ligne)
    












    

