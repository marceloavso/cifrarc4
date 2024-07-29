#MAIN

import sys
def main():
    if sys.argv != 3:
        nome_arquivo = sys.argv[1]
        chave = sys.argv[2]
        funcao = sys.argv[3] 

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
# para fazer a substituição da tabela ascii
def ksa(chave):
  stream = [] # vetor base de 255 bits
  k_stream = [] # vetor 

  for i in range(0, 256):
      stream.append(i)
      k_stream.append(ord(chave[i % len(chave)]))

  j = 0
  for i in range(0, 256):
      j = (j + stream[i] + k_stream[i]) % 256
      temp = stream[i]
      stream[i] = stream[j]
      stream[j] = temp
  return (stream)

#PRGA
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
    cripto.append(stream[(stream[i] + stream[j]) % 256] ^ ord(mensagem[n]))
  
  mensagem_criptografada = ''
  
  for i in cripto:
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

