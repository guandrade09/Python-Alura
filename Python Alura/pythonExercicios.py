
import random

'''
1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().
'''

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

media1 = sum(gastos)/len(gastos)

print(f'A media dos gastos é de {media1}.')

print('')

'''
2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
'''

contadorPorcentagem = 0
somaTK = 0

for elemento in gastos:
    if elemento > 3000.00:
        contadorPorcentagem = contadorPorcentagem + 1
        somaTK = somaTK + elemento

mediaTK = somaTK / contadorPorcentagem

porcentagemTK = (contadorPorcentagem / len(gastos))*100

print(f'A media dos gastos acima de R$3000.00 é R${mediaTK}.')

print(f'O peso das compras acima de R$3000.00 é de {porcentagemTK}%.')

print('')

'''
3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
'''

listaNumeros = []

for elemento in range(0, 5):

    rand = random.randint(0, 10)
    listaNumeros.append(rand)

print(f'Números aleatórios na lista: {listaNumeros}')
print('')

'''
4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
'''

print(f'A versão contrária: {listaNumeros[::-1]}')
print('')

'''
5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
'''

numeroLim = int(input('Digite um número limite, retornará todos os números primos entre: '))

listaPrimos5 = []

for num in range(2, numeroLim+1):
    primo = True
    # print(f'num: {num}')
    for n in range(2, num):
        # print(f'n: {n}')
        if num % n == 0:
            primo = False
            break
    if primo == True:
        listaPrimos5.append(num)
    #print('break')

print(listaPrimos5)
print('')

'''
6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
'''

dados = {'dia': [], 'mes': [], 'ano': []} # type: ignore

for elemento in dados:
    dados[elemento] = int(input(f'Insira um {elemento}: '))

if dados['dia'] == 30 and dados['mes'] == 2 or dados['dia'] == 31 and dados['mes'] == 2:
    print(f'A data é invalida.')
elif dados['dia'] > 0 and dados['dia'] < 32 and dados['mes'] > 0 and dados['mes'] < 13 and dados['ano'] > 1900 and dados['ano'] < 2026:
    print(f'A data de hoje é: {dados['dia']}/{dados['mes']}/{dados['ano']}.')
    print(dados)
else:
    print(f'A data é invalida.')

'''
7) Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).
'''

nBacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

crescimento = []

amostraAtual = 0
amostraPassada = 0
percentual = 0

for elemento in nBacterias:
    amostraAtual = elemento
    if amostraPassada != 0:
        percentual = ((amostraAtual - amostraPassada) / amostraPassada) * 100
    crescimento.append(percentual)
    amostraPassada = elemento

for c in crescimento:
    print(f'{c:.2f}%')

'''
8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
'''

Id = []

doces = []
amargos = []

for i in range(1, 11):
    Id.append(int("10" + str(random.randint(100, 2000)).zfill(4)))

for sku in Id:
    if sku % 2 == 0:
        doces.append(sku)
    else:
        amargos.append(sku)

print(f'Os SKUs doces são: {doces}')
print(f'Os SKUs doces são: {amargos}')

'''
9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B
'''

gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']

respostas = []

nota = 0

for elemento in range(1, 11):
    questao = input(f'Resposta da questão {elemento} é: ').upper()
    respostas.append(questao)
    if gabarito[elemento-1] == respostas[elemento-1]:
        nota += 1

print(respostas)
print(gabarito)
print(f'Sua nota da prova foi de {nota}/10')

'''
10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
'''

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temperatura = []

for n in range(0, 12):
    temp = round(random.uniform(0.0, 60.0), 1)
    # temp = float(input(f'Indique a temperatura do mês de {mes[n]}: '))
    temperatura.append(temp)
    print(f'A temperatura do mês de {mes[n]} é: {temp}')

mediaTemp = round((sum(temperatura) / len(temperatura)), 1)

print(f'{temperatura}')
print(f'A média das temperaturas foi de {mediaTemp}°C.')

print(f'os meses com as temperaturas acima da média foram: ')
for n in range(0, 12):
    if temperatura[n] >= mediaTemp:
        print(f'{mes[n]}: {temperatura[n]}')

'''
11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
{'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
Escreva um código que calcule o total de vendas e o produto mais vendido.
'''

produtos = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

totalVendas = sum(produtos.values())
print(f'O total de vendas foi de {totalVendas}.')

maiorVenda = max(produtos.values())
maiorItem = max(produtos.keys())

print(f'A maior venda foi do {maiorItem}: {maiorVenda}.')

'''
12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos

Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
'''

votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

vencedor = max(votos.keys())
vencedorVotos = max(votos.values())
porcentagem = max(votos.values()) / sum(votos.values()) * 100

print(f'O vencedor foi o {vencedor}, com {vencedorVotos} votos, representando {porcentagem:.2f}% do total')

'''
13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.
'''

salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

abonos = []

for i in salarios:

    a = round(float((i * 0.1)), 2)

    if a >= 200:
        abonos.append(a)
    else:
        abonos.append(200.0)

dic = dict(zip(salarios, abonos))
print(dic)

gastos = sum(abonos)

print(f'Os gastos sobre os abonos foi de R${gastos:.2f}.')

print(f'Os salarios que receberam o abono mínimo foram: ')
for i in dic:
    if dic[i] == 200:
        print(f'R${i:.2f}: R${dic[i]:.2f}')

maior = max(dic.values())
maiorSal = max(dic.keys())
print(f'O maior valor de abono foi do salario R${maiorSal:.2f}: R${maior:.2f}')

'''
14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
{'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}
Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().
'''

estudo = {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

maior = 0

maiorArea = ''

for area, especies in estudo.items():
    somaEsp = sum(especies)
    mediaEsp = somaEsp / len(especies)
    print(f'A média de espécies da {area} é {mediaEsp:.0f}')

    if somaEsp > maiorEsp:
        maiorEsp = somaEsp
        maiorArea = area

print(f'A {maiorArea} é a mais diversa área, com {maiorEsp} especies.')

'''
15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65], 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64], 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56], 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
'''
info = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65], 
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64], 
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56], 
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
    }

totalIdade = 0
totalLen = 0

for setor, idade in info.items():
    soma = sum(idade)
    media = soma / len(idade)
    print(f'A média de idade do {setor} é de {media:.0f} anos.')

    totalIdade += soma
    totalLen += len(idade)

totalMedia = totalIdade / totalLen
print(f'A média total das idades da empresa é de {totalMedia:.0f} anos.')