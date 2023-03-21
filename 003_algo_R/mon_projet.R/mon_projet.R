
library(readr)
projet <- read.csv("/home/salimata/Bureau/algorithme/003_algo_R/projet.csv")
print(projet)
q<-projet$Nom
nomm <-function(nom)
{
  for (i in c(1:nchar(nom) )){
    if (substring(nom,i,i) %in% c(letters,LETTERS) && nchar(nom)>=2){
      return(TRUE)
    }
    else{
      return(FALSE)
    }
  }
}
for (i in 1:length(q)){
  if (nomm(q[i])==TRUE){
    pn<-projet$Prénom
    corect_prenom<-function(prenom){  
      for (j in c(1:nchar(prenom)) ){
        if (substring(prenom,j,j) %in% c(letters,LETTERS) && nchar(prenom)>=3){
          return(prenom)
        }
        else{
          return(FALSE)}
      }
    }
    for (j in 1:length(pn)){
      corect_prenom(pn[j])
      num<- projet$Numero
      corect_numero<-function(numero){
        for (i in 1:nchar(numero) ){
          if (((substring(numero,i,i) %in% LETTERS) | ("0"<=numero[i] && numero<="9")) && nchar(numero)==7){
            return(numero)
          }
          else{
            return(FALSE)}
        }
      }
      # for (k in 1:length(num)) {
      #   if (corect_numero(num[k])!=FALSE)
         dates<-projet$Date.de.naissance
         print(dates)
          
            }
  }
}

