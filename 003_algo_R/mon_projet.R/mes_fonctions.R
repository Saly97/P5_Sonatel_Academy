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
corect_prenom<-function(prenom)
  {
  for (j in 1:nchar(prenom) ) {
    if (substring(prenom,j,j) %in% c(letters,LETTERS) && nchar(prenom)>=3){
      return(TRUE)
    }
    else{
      return(FALSE)
    }
  }
}

prenom<-"8D805GT"
corect_numero(prenom)



