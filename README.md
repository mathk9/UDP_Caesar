# UDP_Caesar
Este repositório contem os scripts Client e Server utilizados para realizar um teste de interceptação de mensagens criptografadas com a Cifra de César.

## O que é a Cifra de Cesar?
A Cifra de Cesar é um dos mais conhecidos métodos para criptografia de mensagens que utiliza a substituição monoalfabética criada pelo Imperador Romano Júlio César. Nesta cifra, é utilizada uma técnica simples de criptografia em que a mesma chave utilizada para criptografar é usada para decriptografar o texto. No cenário original foi usado o número 3 como chave, dessa forma, as letras eram deslocadas em 3 posições no alfabeto para criptografar uma mensagem. Por exemplo, a expressão "Bom dia" passa a ser "Erp gld", dificultando a sua compreensão por aqueles que não conheciam a chave de decriptografia e a forma de aplicá-la.

Para que a mensagem fosse decriptografada era necessário retornar as 3 posições deslocadas no alfabeto para identificar qual mensagem havia sido enviada.

Para o teste realizado pelo grupo foi utilizada a chave igual a 4.
### Funcionamento dos scripts
Optamos por utilizar de exemplo uma classe disponbilizada pelo professor Fabio Henrique Cabrini, já contendo métodos para criptografar e decriptografar mensagens enviadas entre Cliente e Servidor. Adaptamos o script para que fossem tratados os caracteres especiais e palavras com acento.

Importamos a classe nos scripts Simple_udpClient.py e Simple_udpServer.py e realizamos as chamadas para que os scripts pudessem criptografar a mensagem enviada pelo Client e decriptografá-la para exibição ao Server, assim ao ser interceptada pelo programa WireShark ela seria de forma criptografada, dificultando a leitura de seu conteudo.

## Video de demonstração do teste
[Youtube | Desafio de Criptografia - Cifra de Cesar](https://youtu.be/cHXh4Xy669E)
## Grupo
Caio Vinicius Magro - 081200042

Giovana Moreira da Silva - 081200043

Matheus Novais de Souza - 081190048

Ysabela Akiyama Molero Rodrigues - 081200044