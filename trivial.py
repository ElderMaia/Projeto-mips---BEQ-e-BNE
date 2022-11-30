# funções importadas dos arquivos modularizados

from indexar import indexar
from limpar import limpar
from padroes import padroes
from montar import montar
from converter import bin_to_hex
from converter import name_to_dec
from comparar import comparar

# programa construído com ajuda dos alunos de TADS 2022.1
mars = "mars" # arquivo hexadecimal gerado no MARS a partir de dor_e_sofrimento
montador = "nada" # arquivo hexadecimal gerado por este montador
entrada = "dor_e_sofrimento" # caminho do arquivo a ser lido
instr = "instrucoes" # caminho do arquivo com instruções lidas
programa = open(entrada, 'r') # abre arquivo a ser lido 
linhas = programa.read().split("\n") # lista separada por quebra de linha (xerocado de @maure-tads)
for i in range(len(linhas)):
  linhas[i] = limpar(linhas[i]) # limpa-se a linha
linhas = indexar(linhas) # lista com linhas do programa indexadas e rotuladas 
saida = open(montador, "w") # aquivo a ser escrito pelo programa
instrucoes = open(instr, "w") # arquivo a ser escrito com isntruções
for linha in linhas: # rotina para cada linha do arquivo lido
  instrucoes.write(str(linha)+"\n") # escreve instrução em cada linha
  name_to_dec(linha[1]) # traduz nome de registradores para inteiros
  instrucao = padroes(linha[1][0]) # pega padrão mips da instrução
  if "inválida" in instrucao: # encerra o programa caso instrução seja inválida
    print(instrucao)
    exit(0)
  #for linha in linhas:
  #  print(linha)
  instrucao = montar(instrucao, linha, linhas) # monta binario de 32 bits conforme instrução
  instrucao = bin_to_hex(instrucao) # converte binário de 32 bits para hex 8 bits
  saida.write(instrucao+"\n") # escreve instrução em hexadecimal em cada linha
programa.close() # fecha arquivo de entrada
saida.close() # fecha arquivo de saída
instrucoes.close
comparar(mars, montador) # compara os arquivos gerados pelo mars e pelo montador
