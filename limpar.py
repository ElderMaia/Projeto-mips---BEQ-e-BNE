def limpar(linha): # recebe string
  if linha.count(".") > 0:
    linha = linha.replace(".text", " ") # remove .text (pode-se adicionar .data)
  if linha.count("#") > 0:
    comentario = linha.index("#") 
    linha = linha[:comentario] + " " # remove comentários
  linha = linha.replace(",", " ") # remove vígulas
  linha = linha.replace("$", " ") # remove sifrões
  linha = linha.replace("  ", " ") # remove tabulação horizontal
  linha = linha.split() # cria uma lista com as instruções limpas
  return linha # retorna lista

def limpa_dois_pontos(rotulo):
  return rotulo.replace(":", "") # remove rótulos (transformar em função)