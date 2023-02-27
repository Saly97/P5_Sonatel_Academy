notes = ['Math[10|15:15] ', 'Francais[17|9|8:13] ', 'Anglais[10.5|9:15] ', 'PC[10|13:11]  ', 'SVT[12|11|16|8:12]  ', 'HG[10:10]']
for note in notes:
    matiere ={}
    nouvelle_note = note.replace("[","-").replace("|","-").replace(":","-").replace("]","-").split("-")
    # ['SVT', '12', '19', '01', '04', '']
    matiere[nouvelle_note[0]]={
        "devoir": nouvelle_note[1:-2],
        "examen": nouvelle_note[-2]
    }

    somme_des_devoirs = 0.0
    moyenne_des_devoirs=0.0
    for d in matiere[nouvelle_note[0]]["devoir"]:
        somme_des_devoirs+=float(d)
    moyenne_des_devoirs = somme_des_devoirs/len(matiere[nouvelle_note[0]]["devoir"])
    print(moyenne_des_devoirs)