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
corect_prenom<-function(prenom){
  for (j in c(1:nchar(prenom)) ) {
    if (substring(prenom,j,j) %in% c(letters,LETTERS) && nchar(prenom)>=3){
      return(TRUE)
    }
    else{
      return(FALSE)
    }
  }
}
corect_numero<-function(numero){
  for (i in 1:nchar(numero) ){
    if (((substring(numero,i,i) %in% LETTERS) | ("0"<=numero[i] && numero<="9")) && nchar(numero)==7){
      return(numero)
    }
    else{
      return(FALSE)}
  }
}

q<-projet$Nom
for (i in 1:length(q)){
  if (nomm(q[i])==TRUE){
    pn<-projet$Prénom
    # for (j in 1:length(pn)){
    # if (corect_prenom(pn[j])==TRUE){
    num<- projet$Numero
    # print(num)
    
  }
}
#   }
# }
