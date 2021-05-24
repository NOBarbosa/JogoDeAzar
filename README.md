# Jogo De Azar?
## Considere o seguinte jogo:
Dois dados honestos são lançados simultaneamente. Caso as faces dos dados sejam iguais, o jogador vence. Caso as faces sejam diferentes, perde-se.
Para jogar é necessário pagar um taxa de R$ 5,00 (cinco reais). Se ganhar, recebe R$ 25,00 (vinte e cinco reais) de recompensa.

### Pergunta: Vale a pena jogar esse jogo? Vale a pena jogar uma quantidade n de partidas para obter lucro? Qual meu lucro médio ao repetir o jogo algumas vezes?

### Vamos Analisar

##### 1º: Precisamos notar que ao aceitar participar do jogo o lucro, caso vença, será de R$ 20, 00 (vinte reais) afinal foram gastos R$ 5,00 (cinco reais) para jogar.
Lucro = prêmio - taxa ----> Lucro = 25 - 5 = 20.<br/>
Sempre que perde, você tem o prejuízo de R$ 5,00 (cinco reais).

#### Vamos às Possibilidades:
Como os dados são honestos, as faces tem chances iguais de sair. Vamos observar o [Espaço Amostral](https://pt.wikipedia.org/wiki/Espa%C3%A7o_amostral) desse experimento e verificar quais as chances de vitória.

## Espaço Amostral:
![Espaço amostral](https://github.com/NOBarbosa/JogoDeAzar/blob/main/espacoamostral.jpg)

#### Notem que na diagonal do nosso espaço amostral temos as chances de vitória, isto é, temos as faces com valores iguais.
#### Esse espaço amostral tem 36 [Eventos Equiprováveis](https://mundoeducacao.uol.com.br/matematica/casos-equiprovaveis.htm#:~:text=Nos%20espa%C3%A7os%20amostrais%20equiprov%C3%A1veis%20temos,%2C%20isto%20%C3%A9%201%2F6.). Neste caso, nossa [Probabilidade](https://brasilescola.uol.com.br/matematica/probabilidade.htm#:~:text=Probabilidade%20%C3%A9%20um%20ramo%20da,chance%20de%20erro%20em%20pesquisas.) de vitória  e derrota são  expressos respectivamente por:<br/>
Vitória= 6/36 e Derrota= 30/36. Simplificando temos, respectivamente Vitória= 1/6 e Derrota= 5/6

### Vamos associar nossas probabilidades ao lucro Líquido:

Lucro Líquido | Probabilidade associada ao lucro
------------ | -------------
-5 | prob de ter 'lucro' -5 = 5/6
20| prob de ter lucro 20 = 1/6

### Está claro que com apenas 1 tentativa as chances de vitória são bem baixas porém, se jogarmos mais de uma vez será que o lucro não compensa o prejuízo?
#### Para responder essa questão analise o código [Jogo dos Dados](https://github.com/NOBarbosa/JogoDeAzar/blob/main/jogodeazar.py). Lembre-se que quanto maior a quantidade de vezes jogadas mais preciso serão seus resultados.




