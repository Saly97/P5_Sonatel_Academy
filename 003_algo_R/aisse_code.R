library(readr)
projet <- read.csv("/home/salimata/Bureau/algorithme/003_algo_R/projet.csv")
#print(projet)
# etudiant <-function(projet){
#   for (i in 1:nrow(projet)){
#   }
# }

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
  for (j in c(1:nchar(prenom)) ){
    if (substring(prenom,j,j) %in% c(letters,LETTERS) && nchar(prenom)>=3){
      return(prenom)
    }
    else{
      return(FALSE)}
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
correct_classes<-function(classe){
  
  if(classe!=''){
  
  if ((substring(classe,1,1) %in% c("3","4","5","6")) && (substring(classe,nchar(classe),nchar(classe)) %in% c("A","B"))){
    return(paste0(substring(classe,1,1),"em",substring(classe,nchar(classe),nchar(classe))))}
  else{
    return(FALSE)
  }
  }else{
    return(FALSE)
  }
}

q<-projet$Nom
for (i in 1:length(q)){
  if (nomm(q[i])==TRUE){
    pn<-projet$Prénom
  }
}

    for (j in 1:length(pn)){
      if (corect_prenom(pn[j])==TRUE){
        num<- projet$Numero
      }
    }
        for (k in 1:length(num)) {
           if (corect_numero(num[k])!=FALSE){
             classes <-projet$Classe
           }
        }
          
          for (c in 1:length(projet$Classe)){
            classecorrect_classes(projet$classes))
          }
