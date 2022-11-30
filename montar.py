from converter import dec_to_bin # importa função de converter decimal para binário
from indexar import pega_indice # importa função que retorna indice de rótulo

def montar(instrucao, linha, linhas): # dicionário com padrão e lista com instrução mips
  padrao = instrucao["padrao"]
  instrucao = instrucao["instrucao"]
  mips = linha
  linha = linha[1]
  
  if len(linha) == 1:
    return instrucao # retona sycall e nop (melhorar no futuro)
    
  if padrao == "i": # montagem do padrão I
    s = int(linha[2]) # $s
    t = int(linha[1]) # $t
    i = int(linha[3]) # imediato 
    instrucao = instrucao.replace("s", format(s, "05b")) # substitui 's' por 5 bits
    instrucao = instrucao.replace("t", format(t, "05b")) # substitui 't' por 5 bits
    instrucao = instrucao.replace("i", dec_to_bin(i, 16)) # substitui 'i' por 16 bits

  elif padrao == "b":
    s = int(linha[1]) # $s
    t = int(linha[2]) # $t
    index_rotulo = pega_indice(linhas, linha[3]) # indice do rotulo 
    b = index_rotulo - mips[-1] - 1 # calculo da distancia entre instruções
    instrucao = instrucao.replace("s", format(s, "05b")) # substitui 's' por 5 bits
    instrucao = instrucao.replace("t", format(t, "05b")) # substitui 't' por 5 bits
    instrucao = instrucao.replace("b", dec_to_bin(b, 16)) # substitui 'i' por 16 bits
  
  elif padrao == "r": # montagem do padrão R
    s = int(linha[2]) # $s
    t = int(linha[3]) # $t
    d = int(linha[1]) # $d
    instrucao = instrucao.replace("s", format(s, "05b")) # substitui 's' por 5 bits
    instrucao = instrucao.replace("t", format(t, "05b")) # substitui 't' por 5 bits
    instrucao = instrucao.replace("d", format(d, "05b")) # substitui 'd' por 5 bits
    
  elif padrao == "d": # montagem do padrão D
    s = int(linha[1]) # $s
    t = int(linha[2]) # $t
    instrucao = instrucao.replace("s", format(s, "05b")) # substitui 's' por 5 bits
    instrucao = instrucao.replace("t", format(t, "05b")) # substitui 't' por 5 bits
    
  elif padrao == "s": # montagem do padrão S
    d = int(linha[1]) # $d
    t = int(linha[2]) # $t
    a = int(linha[3]) # a
    instrucao = instrucao.replace("d", format(d, "05b")) # substitui 'd' por 5 bits
    instrucao = instrucao.replace("t", format(t, "05b")) # substitui 't' por 5 bits
    instrucao = instrucao.replace("a", format(a, "05b")) # substitui 's' por 5 bits

  elif padrao == "j": # montagem do padrão j 
    j = 0x00400000 + pega_indice(linhas, linha[1]) * 4 >> 2 # instr_index deslocada 2 bits à direita
    instrucao = instrucao.replace("j", dec_to_bin(j, 26)) # substitui 'j' por 26 bits
    
  return instrucao # string representa binário de 32 bits