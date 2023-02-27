t=[["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"],["january","february","march","april","may","jun","jully","august","september","octomber","november","december"]]


choix=input("choisissez entre :\n1.francais\n2.anglais\n3.quitté")
for k in range(3):
    for i in range(k,12,3):
        c =t[int(choix)-1][i]
        print(c+" "*(20-len(c)),end="")
    print("\n ")




