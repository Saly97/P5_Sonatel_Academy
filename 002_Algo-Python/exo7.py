# phrase=input("donner la phrase que vous voullez connaitre son code corespondant: ")
phrase="BONJOUR MOUSSA tryfu;TU 456"
tab_alfabe={"A":2,"B":22,"C":222,"D":3,"E":33,"F":333,"G":4,"H":44,"I":444,"J":5,"K":55,"L":555,"M":6,"N":66,"O":666,"P":7,"Q":77,"R":777,"S":7777,"T":8,"U":88,"V":888,"W":9,"X":99,"Y":999,"Z":9999," ":"00","0":"a","1":"b","2":"c","3":"d","4":"e","5":"f","6":"g","7":"h","8":"i","9":"j"} 
# tab_chiffre={"0":"a","1":"b","2":"c","3":"d","4":"e","5":"f","6":"g","7":"h","8":"i","9":"j"}
tab_phrase=[]
tab_phrase=phrase
convertir=""
tab_alfabe["A"]
for char in phrase:
    if char not in tab_alfabe.keys():
        convertir+= char
    else:
         convertir+=str(tab_alfabe[char])
#if tab_alfabe[char-1]==tab_alfabe[char]:
    
print(convertir)
# if char in tab_chiffre:

#    if char == tab_alfabe[k] :
#             convertir+=tab_alfabe["k"]
# print(convertir)







