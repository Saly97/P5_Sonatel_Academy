correct_classes<-function(classe){
  if (nchar(classe)<1){
    return(invalide)}
  else{
      if ((substring(classe,1,1) %in% (3:6 )) && (substring(classe,nchar(classe),nchar(classe)) %in% c("A","B"))){
        return(paste0(substring(classe,1,1),"em",substring(classe,nchar(classe),nchar(classe))))
      }
    }
  }
classed<-"3ieme B"
correct_classes(classed)