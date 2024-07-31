# cifrarc4
Algoritmo de criptografia RC4 desenvolvido em python como atividade avaliativa da disciplina de Segurança de Sistemas do curso de Tecnologia em Análise e Desenvolvimento de Sistemas do Instituto Federal do Rio Grande do Sul Campus Canoas.

O script é capaz de criptografar a informação contida dentro de um arquivo txt, gerando outro arquivo txt. Também é possível fazer a decriptação de arquivos. 

## Melhoria
Acredito que uma possível melhoria implementada nesta versão seja o aumento dos vetores de key-scheduling, de 255 bytes para 1024 bytes. Dessa forma o algoritmo pode lidar com arquivos unicode utf-8. 

## Configuração
O algoritmo foi desenvolvido em e python v3.12 utilizando o windows 11 como sistema operacional, sendo somente testado neste sistema.
Recomenda-se estas configurações para que o algoritmo funcione como o esperado.

## Execução
O script deve ser executado no terminal com o seguinte comando:
python <script.py> <arquivo.txt> <chave> <operação>

Sendo:
<script.py>: o nome do arquivo do script python. Por padrão como está aqui o nome é cifra_rc4.py
<arquivo.txt: aqui deve ser passado o endereço do arquivo txt que será utilizado para fazer as operações.
Se o arquivo txt estiver na mesma pasta do script, pode ser colocado o nome do arquivo .txt que funcionará diretamente.
<chave>: insira uma chave para criptografar/decriptografar o arquivo. Para a decriptografia deve ser utilizada a mesma chave utilizada na criptografia.
<operação> 'c' ou 'd': aqui você escolhe qual operação quer fazer. Para criptografar um arquivo, digite c. para decriptografar, digite d.

Seja qual for a operação, o script criará um novo arquivo .txt criptografado/decriptografado do arquivo .txt utilizado na pasta em que o script se encontra. Os novos arquivos podem ser identificados com as terminações _cripot e _decripto conforme a operação utilizada.

## Exemplo de execução em windows

python cifra_rc4.py arquivo.txt chave c
