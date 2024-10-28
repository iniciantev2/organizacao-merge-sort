def calcular_metrica(preco_exercicio, prazo_vencimento, volume_negociado, spread):
    # personalizar conforme necessário
    preco_normalizado = 100 - preco_exercicio
    prazo_normalizado = prazo_vencimento
    volume_normalizado = volume_negociado
    spread_normalizado = 100 - spread

    return (0.3 * preco_normalizado + 0.3 * prazo_normalizado + 
            0.2 * volume_normalizado + 0.2 * spread_normalizado)

# Merge Sort
def merge_sort(transacoes):
    if len(transacoes) <= 1:
        return transacoes
    
    meio = len(transacoes) // 2
    esquerda = merge_sort(transacoes[:meio])
    direita = merge_sort(transacoes[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i]['metrica'] >= direita[j]['metrica']:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

# Exemplo de uso
transacoes = [
    {"preco_exercicio": 50, "prazo_vencimento": 30, "volume_negociado": 1000, "spread": 5},
    {"preco_exercicio": 60, "prazo_vencimento": 10, "volume_negociado": 500, "spread": 10},
    {"preco_exercicio": 55, "prazo_vencimento": 20, "volume_negociado": 800, "spread": 8}
]

for transacao in transacoes:
    transacao['metrica'] = calcular_metrica(transacao['preco_exercicio'], transacao['prazo_vencimento'], transacao['volume_negociado'], transacao['spread'])

transacoes_ordenadas = merge_sort(transacoes)

print("Transações ordenadas por atratividade:")
for t in transacoes_ordenadas:
    print(t)