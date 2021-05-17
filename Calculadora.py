#CALCULADORA DE ALCANCE DE ANÚNCIOS

print('======Calculadora de Alcance de Anúncios======')

# Calcular inicialmente o maximo de vizualizações no anúncio original, com relação ao valor investido
valor_investido = int(input('Valor Investido: '))

vizualizacao_por_real = 30 * valor_investido # A cada 1 real investido são 30 vizualizações

# Calculando o maximo de vizualizações (anúncio original+compartilhamento)

cliques_por_vizualizacoes = vizualizacao_por_real * 0.12 # A cada 100v vizualizações, 12 cliques. 12% das vizualizações geram cliques.

compartilhamento_por_clique = cliques_por_vizualizacoes * 0.15 # A cada 20 cliques, 3 compartilhamentos. 15% dos cliques são compartilhados.

vizualizacoes_por_compartilhamento = compartilhamento_por_clique * 40 # Cada compartilhamento gera 40 novas vizualizações.

vizualizacao_final = vizualizacoes_por_compartilhamento * 4 # Ao multiplicarmos por 4 cada vizualização por compartilhamento, teremos o valor aproximado de vizualizações no geral, considerando o anuncio original + compartilhamentos.


print(f'O alcance a cada R${valor_investido} investido é de aproximadamente {vizualizacao_final} vizualizações.')
