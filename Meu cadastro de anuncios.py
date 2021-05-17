import time
import os
import datetime

print('''Bem vindo ao sistema de cadastro de anúncios!
Selecione uma das opções para continuar:
    [1] Inserir novo anúncio;
    [2] Consulta a anúncios já cadastrados;
    [3] Encerrar programa.''')

opção = input(f'>>>Qual a sua opção? {int}')

if opção == 1:
    anuncio = input('''>>INSERIR NOVO ANÚNCIO<<
    Nome do Anúncio: ''')
    cliente = input('Nome do Cliente: ')
    data_inicio = input(datetime('Data de Início em dd/mm/aaaa: '))
    data_termino = input(datetime('Data de termino em dd/mm/aaaa: '))
    valor_investido = input('Insira o valor investido por dia: ')
quantidade_dias = int(data_termino - data_inicio)
#Calculadora quantidade de vizualizações, cliques e compartilhamento
valor_investido = int(input('Valor Investido por dia: '))

vizualizacao_por_real = 30 * valor_investido # A cada 1 real investido são 30 vizualizações

# Calculando o maximo de vizualizações (anúncio original+compartilhamento)

cliques_por_vizualizacoes = vizualizacao_por_real * 0.12 # A cada 100v vizualizações, 12 cliques. 12% das vizualizações geram cliques.

compartilhamento_por_clique = cliques_por_vizualizacoes * 0.15 # A cada 20 cliques, 3 compartilhamentos. 15% dos cliques são compartilhados.

vizualizacoes_por_compartilhamento = compartilhamento_por_clique * 40 # Cada compartilhamento gera 40 novas vizualizações.

vizualizacao_final = vizualizacoes_por_compartilhamento * 4 # Ao multiplicarmos por 4 cada vizualização por compartilhamento, teremos o valor aproximado de vizualizações no geral, considerando o anuncio original + compartilhamentos.

quantidade_cliques = cliques_por_vizualizações * vizualizações_por_real

quantidade_compartilhamento = compartilhamento_por_clique * 4

total_investimento = quantidade_dias * valor_investido
print (f'''A quantidade aproximada de vizualizações é {vizualizacao_final}.
A quantidade máxima de cliques é {quantidade_cliques}.
O maximo de compartilhamento gerado é {quantidade_compartilhamento}''')
anuncio = {'Anúncio': anuncio, 'Cliente': cliente, 'Início do anúncio': data_inicio,
                 'Término do anúncio': data_termino, 'Investimento por dia': valor_investido,
                 'Quantidade de Visualizações': vizualizacao_final, 'Valor total Investido': total_investimento, 'Quantidade de Compartilhamentos': quantidade_compartilhamento}

 #Salvando relatório.
banco = open('db.txt', 'r')
banco.write(str(anuncio) + '\n')
banco.close()
print('Dados registrados')
    elif opção == 2:  # Consulta anuncio já cadastrados
print('''1. Procurar pelo nome do cliente
      2. Procurar por dat''')

opcao = int(input("Opção: "))

if opcao == 1:
    cliente_desejado = input("Nome do cliente: ")
    doc = open('db.txt', 'r')
    for linha in arquivo:
        linha = linha.rstrip()
        if pesquisa_cliente in linha:
            cont = cont + 1
            print('Sua pesquisa encontrou o seguinte resultado:')
            print(linha)
    doc.close()
    break
else:
elif opção == 3:
print('Fim do programa! Obrigado por usar o sistema de cadastro de anúncios!')