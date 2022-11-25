# padrão i ex: addi $s $t imediato (16 bits)
# padrão r add $d $s $t
# padrão s sll $d $t a (5 bits)
# padrão d div $s $t 
def padroes(nome):
  instrucoes = {
  "add": {
    "instrucao": "000000"+"std"+"00000"+"100000", #add $d $s $t
    "padrao": "r"
  },
  "addi": {
    "instrucao": "001000"+"sti", #addi $t $s imediato (16 bits)
    "padrao": "i"
  },
  "addiu": {
    "instrucao": "001001"+"sti", #addi $t $s imediato (16 bits)
    "padrao": "i"
  },
  # ...
}
  if nome in instrucoes:
    return instrucoes[nome]
  else:
    return f"instrução {nome} inválida"

def registadores(registrador):
  registradores = {
    "zero": 0,
    "at": 1,
    "v0": 2,
    "t0": 8
    # ...
  }
  if registrador in registradores:
    return registradores[registrador]
  else:
    return registrador