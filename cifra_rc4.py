#MAIN

import sys
def main():
    if sys.argv != 3:
        nome_arquivo = sys.argv[1]
        chave = sys.argv[2]
        funcao = sys.argv[3].lower()  

        mensagem = ''
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            mensagem += arquivo.read()

        if (funcao != 'c') and (funcao != 'd'):
            param_error()
        else:
            if funcao == 'c':
                cifrar(mensagem, nome_arquivo, chave)
            else:
               decifrar(mensagem, nome_arquivo, chave)

    else:
        param_error()


# Métodos Cripto/Decripto
# KSA
# cria vetores para gerar o código de criptografia que será utilizado
# para fazer a substituição da tabela unicode
def ksa(chave):
  stream = [] # vetor de índices de 1025 posições para melhor funcionamento com unicode utf-8
  k_stream = [] # vetor de conversão dos caracteres da chave para gerar o código de criptografia

  for i in range(0, 1025): # aloca os valores nos vetores não importando o tamanho da chave
      stream.append(i)
      k_stream.append(ord(chave[i % len(chave)])) # transforma caracter em inteiro

  j = 0
  for i in range(0, 1025): # embaralha os vetores
      j = (j + stream[i] + k_stream[i]) % 256
      temp = stream[i]
      stream[i] = stream[j]
      stream[j] = temp
  return (stream)

#PRGA
# função que faz a criptografia e decriptografia de fato, fazendo um cálculo xor
def prga(mensagem, stream):
  i = 0
  j = 0
  cripto = []
  for n in range(len(mensagem)):
    i = (i + 1) % 256
    j = (j + stream[i]) % 256
    temp = stream[i]
    stream[i] = stream[j]
    stream[j] = temp
    cripto.append(stream[(stream[i] + stream[j]) % 256] ^ ord(mensagem[n])) # aqui é feito o cálculo xor entre os pares de dados pra criptografia
  
  mensagem_criptografada = ''
  
  for i in cripto: # transforma cada número binário representado em cripto em um caracter, fazendo uma concatenação em string
    mensagem_criptografada += chr(i)

  return(mensagem_criptografada)   

#cifrar
def cifrar(mensagem, nome_arquivo, chave):
  stream = ksa(chave)
  mensagem_criptografada = prga(mensagem, stream)
  novo_arquivo = nome_arquivo[0:-4] + '_cripto.txt'
  with open(novo_arquivo, "w", encoding='utf-8') as arquivo:
            arquivo.write(mensagem_criptografada)
  print('Criptografado com sucesso.')

#decifrar
def decifrar(mensagem_criptografada, nome_arquivo, chave):
  stream = ksa(chave)
  mensagem_decriptografada = prga(mensagem_criptografada, stream)
  novo_arquivo = nome_arquivo[0:-11] + '_decripto.txt'
  with open(novo_arquivo, "w", encoding='utf-8') as arquivo:
            arquivo.write(mensagem_decriptografada)
  print('Decriptografado com sucesso.')

#exibição de erro
def param_error():
   print('Erro de parâmetros.')
   print('Devem ser passados 3 argumentos após o nome do script')
   print('Os argumentos devem seguir a seguinte ordem: nome do arquivo .txt; chave de criptografia; c para criptografar ou d para decriptografar')


main()

