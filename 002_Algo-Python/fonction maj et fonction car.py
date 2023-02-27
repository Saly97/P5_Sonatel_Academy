#text=input("donner votre text")
text="""Demander des informations concernant& l’étudiant tant que l’utilisateur,,,,,, désire continuer.
Vous devez demander le téléphone, nom,      prénom,     classe, note$$ de devoir, note de projet et
note d’examen pour ensuite calculer la moyenne et afficher le résultat sous forme du tableau
ci- dessous lorsque l’utilisateur terminera sa saisie."""
def phrasere_cupépéré(text):
    phrase=""
    tab_phrase=[]
    for t in text:
        phrase+=t
        if t in [".","!","?"]:
            tab_phrase.append(text)
            phrase=""
    return tab_phrase   
def enlevé_espac_unitil(phrase):
    p=""
    fc=False
    for i in range(len(phrase)-1):
        if not (phrase[i] in  [" ",])

             


