def get_index(linhas, valor): # recebe lista de linhas e valor a ser procurado
  for i in range(len(linhas)):
    if linhas[i][0] == valor:
      valor = linhas[i][-1]
  return valor # retorna indice linha que contém do valor

