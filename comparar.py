def comparar(mars, montador): # nome dos arquivos a serem comparados
  linha = 0
  correto = 0
  mips_mars = open(mars) # abre arquivo traduzido pelo mars
  mips_montador = open(montador) # abre arquivo traduzido pelo montador
  while (True):
    base = mips_mars.readline().rstrip() # lê linha por linha
    teste = mips_montador.readline().rstrip() # lê linha por linha
    if base == "" and teste == "": # para programa ao final dos arquivos
      break
    else:
      linha += 1
    if linha < 10: # mostra valores com zero
      zero = "0"
    else:
      zero = ""      
    if base == teste: 
      print(f"Linha {zero}{linha} está correta: {teste}") # mostra linha correta
      correto += 1
    else:
      print(f"Linha {zero}{linha} está ERRADA: {teste} != {base}") # mostra linha incorreta
  mips_mars.close()
  mips_montador.close()
  print(str(int(correto/linha*100))+"% de acerto") # mostra porcentagem de acerto
