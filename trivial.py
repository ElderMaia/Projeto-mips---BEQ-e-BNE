from padroes import padroes
from limpar import limpar
from montar import montar
from converter import bin_to_hex
from converter import name_to_dec

programa = "dor_e_sofrimento"
programa = open(programa, 'r').read().split("\n")
saida = open("nada", "w")
for linha in programa:
  linha = limpar(linha)
  if linha != []:
    name_to_dec(linha)
    instrucao = padroes(linha[0])
    if "inválida" in instrucao:
      print(instrucao)
      exit(0)
    instrucao = montar(instrucao, linha)
    instrucao = bin_to_hex(instrucao)
    saida.write(instrucao+"\n")
saida.close()
    