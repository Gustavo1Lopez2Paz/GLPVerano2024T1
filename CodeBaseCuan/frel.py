def obtener_fr(fa):

  fr = []
  for elemento in fa:
    frel = elemento / sum(fa) * 100
    fr.append(frel)
      
  return fr
