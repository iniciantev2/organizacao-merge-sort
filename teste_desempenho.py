import time
import random

def calcular_metrica(preco_exercicio, prazo_vencimento, volume_negociado, spread):
    preco_normalizado = 100 - preco_exercicio
    prazo_normalizado = prazo_vencimento
    volume_normalizado = volume_negociado
    spread_normalizado = 100 - spread
    return (0.3 * preco_normalizado + 0.3 * prazo_normalizado + 
            0.2 * volume_normalizado + 0.2 * spread_normalizado)

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

def gerar_dados_teste(n):
    transacoes = []
    for _ in range(n):
        preco_exercicio = random.uniform(20, 80)
        prazo_vencimento = random.randint(1, 90)
        volume_negociado = random.randint(100, 5000)
        spread = random.uniform(1, 20)
        transacao = {
            "preco_exercicio": preco_exercicio,
            "prazo_vencimento": prazo_vencimento,
            "volume_negociado": volume_negociado,
            "spread": spread,
            "metrica": calcular_metrica(preco_exercicio, prazo_vencimento, volume_negociado, spread)
        }
        transacoes.append(transacao)
    return transacoes

def teste_desempenho():
    tamanhos = [1000, 10000, 100000]
    for tamanho in tamanhos:
        transacoes = gerar_dados_teste(tamanho)
        
        inicio = time.time()
        transacoes_ordenadas = merge_sort(transacoes)
        fim = time.time()
        
        print(f"\nTamanho: {tamanho}, Tempo de execução: {fim - inicio:.4f} segundos")
        print("Primeiras 5 transações ordenadas por atratividade:")
        for t in transacoes_ordenadas[:5]:
            print(t)

teste_desempenho()