# funções importadas dos arquivos modularizados

from padroes import padroes
from limpar import limpar
from montar import montar
from converter import bin_to_hex
from converter import name_to_dec

# programa construído com ajuda dos alunos de TADS 2022.1

programa = "dor_e_sofrimento" # caminho do arquivo a ser lido
# abre arquivo e cria uma lista separando itens pela quebra de linha
programa = open(programa, 'r').read().split("\n") # xerocado de @pedro-maure
saida = open("nada", "w") # aquivo a ser escrito pelo programa
for linha in programa: # rotina para cada linha do arquivo lido
  linha = limpar(linha) # limpa-se a linha
  if linha != []: # pula-se linhas vazinhas
    name_to_dec(linha) # traduz nome de registradores para inteiros
    instrucao = padroes(linha[0]) # pega padrão mips da instrução
    if "inválida" in instrucao: # encerra o programa caso instrução seja inválida
      print(instrucao)
      exit(0)
    instrucao = montar(instrucao, linha) # monta binario de 32 bits conforme instrução
    instrucao = bin_to_hex(instrucao) # converte binário de 32 bits para hex 8 bits
    saida.write(instrucao+"\n") # escreve instrução em hexadecimal em cada linha
saida.close() #fecha arquivo de saída
    