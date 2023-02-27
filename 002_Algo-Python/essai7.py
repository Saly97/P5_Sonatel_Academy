# phrase=input("donner la phrase que vous voullez connaitre son code corespondant: ")
phrase="BONJOUR MOUSSA tryfu;TU 456"
tab_alfabe={"A":2,"B":22,"C":222,"D":3,"E":33,"F":333,"G":4,"H":44,"I":444,"J":5,"K":55,"L":555,"M":6,"N":66,"O":666,"P":7,"Q":77,"R":777,"S":7777,"T":8,"U":88,"V":888,"W":9,"X":99,"Y":999,"Z":9999," ":"00","0":"a","1":"b","2":"c","3":"d","4":"e","5":"f","6":"g","7":"h","8":"i","9":"j"} 
# tab_chiffre={"0":"a","1":"b","2":"c","3":"d","4":"e","5":"f","6":"g","7":"h","8":"i","9":"j"}
tab_phrase=[]
tab=[]
tab_phrase=phrase
convertir=[]
tab_alfabe["A"]
for char in phrase:
    if char not in tab_alfabe.keys():
        convertir.append(char)
    else:
         convertir.append(str(tab_alfabe[char]))
tab.append(convertir[0])
for i in range(1,len(convertir)):
    a=convertir[i-1]
    b=convertir[i]
    if a[len(a)-1]==b[0]:
        tab.append("0")
        
    tab.append(convertir[i])
print(tab)
print(len(convertir))
#if convertir[char-1]==convertir[char]:
    # if char in tab_chiffre:

#    if char == tab_alfabe[k] :
#             convertir+=tab_alfabe["k"]
# print(convertir)







