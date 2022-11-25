from padroes import registadores # importa a função registradores de padroes.py

def bin_to_hex(instrucao): # string que representa numero de 32 bits em binário 
  return format(int(instrucao, 2), "08x") # string de represneta nume hex de 8 bits  

def dec_to_bin(numero, bits): # inteiro 
  binario = ""
  for i in range(bits):
    binario += str(numero >> (bits - 1) - i & 1) 
  return binario # retorna string que representa binário de 16 bits em complento de 2

def name_to_dec(linha): # lista com instrução mips limpa
  if len(linha) > 1:
    for i in range(1, len(linha) - 1):
      linha[i] = registadores(linha[i]) # transforma nome do registrador em inteiro