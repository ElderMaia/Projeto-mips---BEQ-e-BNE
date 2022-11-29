# funções importadas dos arquivos modularizados

from indexar import indexar
from limpar import limpar
from padroes import padroes
from montar import montar
from converter import bin_to_hex
from converter import name_to_dec

# programa construído com ajuda dos alunos de TADS 2022.1

arquivo = "dor_e_sofrimento" # caminho do arquivo a ser lido
programa = open(arquivo, 'r') # abre arquivo a ser lido 
linhas = programa.read().split("\n") # lista separada por quebra de linha (xerocado de @maure-tads)
for i in range(len(linhas)):
  linhas[i] = limpar(linhas[i]) # limpa-se a linha
linhas = indexar(linhas) # lista com linhas do programa indexadas e rotuladas 
saida = open("nada", "w") # aquivo a ser escrito pelo programa
for linha in linhas: # rotina para cada linha do arquivo lido
  name_to_dec(linha[1]) # traduz nome de registradores para inteiros
  instrucao = padroes(linha[1][0]) # pega padrão mips da instrução
  if "inválida" in instrucao: # encerra o programa caso instrução seja inválida
    print(instrucao)
    exit(0)
  instrucao = montar(instrucao, linha[1], linha[-1]) # monta binario de 32 bits conforme instrução
  print(linha[1])
  instrucao = bin_to_hex(instrucao) # converte binário de 32 bits para hex 8 bits
  saida.write(instrucao+"\n") # escreve instrução em hexadecimal em cada linha
saida.close() #fecha arquivo de saída
    