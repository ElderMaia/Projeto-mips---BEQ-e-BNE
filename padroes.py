# padrão i exemplo: addi $s $t imediato (numero em complemento de 2 em 16 bits)
# padrão r exemplo: add $d $s $t
# padrão s exemplo: sll $d $t a (numero em 5 bits)
# padrão d exemplo: div $s $t 
# padrão b exemplo: beq $s $t b (instrução[indice] - roluto[indice] - 1 em 16 bits) 
# padrão j exemplo: div $s $t j (0x00400000 + indice * 4 >> 2 em 26 bits)
# padrões podem ser adicionados ou modificados (modificar também montar.py)

def padroes(nome): # nome é string do nome da instrução
  instrucoes = { # dicionário de dicionários. Ideia xerocada do @maure-tads
    "add": {
      "instrucao": "000000"+"std"+"00000"+"100000", # instrução $d $s $t
      "padrao": "r"
    },
    "addi": {
      "instrucao": "001000"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "addiu": {
      "instrucao": "001001"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "addu": {
      "instrucao": "000000"+"std"+"00000"+"100001", # instrução $d $s $t
      "padrao": "r"
    },
    "and": {
      "instrucao": "000000"+"std"+"00000"+"100100", # instrução $d $s $t
      "padrao": "r"
    },
    "andi": {
      "instrucao": "001100"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "div": {
      "instrucao": "000000"+"st"+"00000"+"00000"+"011010", # instrução $s $t 
      "padrao": "d"
    },
    "divu": {
      "instrucao": "000000"+"st"+"00000"+"00000"+"011011", # instrução $s $t 
      "padrao": "d"
    },
    "mul": {
      "instrucao": "011100"+"std"+"00000"+"000010", # instrução $d $s $t
      "padrao": "r"
    },
    "mult": {
      "instrucao": "000000"+"st"+"00000"+"00000"+"011000", # instrução $s $t 
      "padrao": "d"
    },
    "multu": {
      "instrucao": "000000"+"st"+"00000"+"00000"+"011001", # instrução $s $t 
      "padrao": "d"
    },
    "nop": {
      "instrucao": "000000"+"00000"+"00000"+"00000"+"00000"+"000000", # caso à parte
      "padrao": "r"
    },
    "nor": {
      "instrucao": "000000"+"std"+"00000"+"100111", # instrução $d $s $t
      "padrao": "r"
    },
    "or": {
      "instrucao": "000000"+"std"+"00000"+"100101", # instrução $d $s $t
      "padrao": "r"
    },
    "ori": {
      "instrucao": "001101"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "sll": {
      "instrucao": "000000"+"00000"+"tda"+"000000", # instrução $d $t a (5 bits)
      "padrao": "s"
    },
    "slt": {
      "instrucao": "000000"+"std"+"00000"+"101010", # instrução $d $s $t
      "padrao": "r"
    },
    "slti": {
      "instrucao": "001010"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "sltiu": {
      "instrucao": "001011"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "sltu": {
      "instrucao": "000000"+"std"+"00000"+"101011", # instrução $d $s $t
      "padrao": "r"
    },
    "sra": {
      "instrucao": "000000"+"00000"+"tda"+"000011", # instrução $d $t a (5 bits)
      "padrao": "s"
    },
    "srl": {
      "instrucao": "000000"+"00000"+"tda"+"000010", # instrução $d $t a (5 bits)
      "padrao": "s"
    },
    "sub": {
      "instrucao": "000000"+"std"+"00000"+"100010", # instrução $d $s $t
      "padrao": "r"
    },
    "subu": {
      "instrucao": "000000"+"std"+"00000"+"100011", # instrução $d $s $t
      "padrao": "r"
    },
    "syscall": {
      "instrucao": "000000"+"00000"+"00000"+"00000"+"00000"+"001100", #caso a parte
      "padrao": "r"
    },
    "xor": {
      "instrucao": "000000"+"std"+"00000"+"100110", # instrução $d $s $t
      "padrao": "r"
    },
    "xori": {
      "instrucao": "001110"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "beq": {
      "instrucao": "000100"+"stb", # instrução $s $t b (16 bits)
      "padrao": "b"
    },
    "bne": {
      "instrucao": "000101"+"stb", # instrução $s $t b (16 bits)
      "padrao": "b"
    },
    "j": {
      "instrucao": "000010"+"j", # instrução instr_index (26 bits) >> 2 bits à direita
      "padrao": "j"
    },
  }
  if nome in instrucoes: # Se houver o a instrução cadastrada 
    return instrucoes[nome] # o programa retorna o dicionário com a instrução
  else:
    return f"instrução {nome} inválida" # caso contrário retorna um erro

def registadores(registrador): # registrador é string
  registradores = { # dicionário de dicionários xerocado de @maure-tads
    "zero": 0,
    "at": 1,
    "v0": 2,
    "v1": 3,
    "a0": 4,
    "a1": 5,
    "a2": 6,
    "a3": 7,
    "t0": 8,
    "t1": 9,
    "t2": 10,
    "t3": 11,
    "t4": 12,
    "t5": 13,
    "t6": 14,
    "t7": 15,
    "s0": 16,
    "s1": 17,
    "s2": 18,
    "s3": 19,
    "s4": 20,
    "s5": 21,
    "s6": 22,
    "s7": 23,
    "t8": 24,
    "t9": 25,
    "k0": 26,
    "k1": 27,
    "gp": 28,
    "sp": 29,
    "fp": 30,
    "ra": 31
  }
  if registrador in registradores: # se houver o o nome do registrador
    return registradores[registrador] # retorna o valor inteiro do registrador
  else:
    return registrador # caso contrário retorno o parametro original 