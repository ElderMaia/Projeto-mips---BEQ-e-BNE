from padroes import registadores
def bin_to_hex(instrucao):
  return format(int(instrucao, 2), "08x")

def dec_to_bin(numero):
  binario = ""
  for i in range(16):
    binario += str(numero >> 15-i & 1) 
  return binario

def name_to_dec(linha):
  if len(linha) > 1:
    for i in range(1, len(linha) - 1):
      linha[i] = registadores(linha[i])