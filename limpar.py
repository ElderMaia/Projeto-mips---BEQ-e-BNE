def limpar(linha): 
  if linha.count(".") > 0:
    linha = linha.replace(".text", " ")
  if linha.count("#") > 0:
    comentario = linha.index("#")
    linha = linha[:comentario] + " "
  if linha.count(":") > 0:
    rotulo = linha.index(":")
    linha = linha[rotulo + 1:] + " "
  linha = linha.replace(",", " ")
  linha = linha.replace("$", " ")
  linha = linha.split()
  return linha