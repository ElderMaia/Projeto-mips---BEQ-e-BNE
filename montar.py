from converter import dec_to_bin
def montar(instrucao, linha):
  padrao = instrucao["padrao"]
  instrucao = instrucao["instrucao"]
  if len(linha) == 1:
    return instrucao
  if padrao == "i":
    s = int(linha[2]) # $s
    t = int(linha[1]) # $t
    i = int(linha[3]) # imediato
    instrucao = instrucao.replace("s", format(s, "05b"))
    instrucao = instrucao.replace("t", format(t, "05b"))
    instrucao = instrucao.replace("i", dec_to_bin(i))
  elif padrao == "r":
    s = int(linha[2]) # $s
    t = int(linha[3]) # $t
    d = int(linha[1]) # $d
    instrucao = instrucao.replace("s", format(s, "05b"))
    instrucao = instrucao.replace("t", format(t, "05b"))
    instrucao = instrucao.replace("d", format(d, "05b"))
  elif padrao == "d":
    s = int(linha[1]) # $s
    t = int(linha[2]) # $t
    instrucao = instrucao.replace("s", format(s, "05b"))
    instrucao = instrucao.replace("t", format(t, "05b"))
  elif padrao == "s":  
    d = int(linha[1]) # $d
    t = int(linha[2]) # $t
    a = int(linha[3]) # a
    instrucao = instrucao.replace("d", format(d, "05b"))
    instrucao = instrucao.replace("t", format(t, "05b"))
    instrucao = instrucao.replace("a", format(a, "05b"))
  return instrucao