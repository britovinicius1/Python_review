#%%
#Desafio
#Calcular o % de stockout
# o % de stockout é calculado por (vendas perdidas por estoque)/ (vendas concluidas + vendas perdidas por estoque)

vendas = {
    'VE0001': (15000,  'Concluído',  ''),
    'VE0002': (13300,  'Cancelado',  'Cancelado pelo Cliente'),
    'VE0003': (12000,  'Concluído',  ''),
    'VE0004': (15562,  'Concluído',  ''),
    'VE0005': (18752,  'Cancelado',  'Estoque em Falta'),
    'VE0006': (16358,  'Cancelado',  'Estoque em Falta'),
    'VE0007': (9400,   'Cancelado',  'Cancelado pelo Cliente'),
    'VE0008': (22100,  'Concluído',  ''),
    'VE0009': (11050,  'Cancelado',  'Estoque em Falta'),
    'VE0010': (17800,  'Concluído',  ''),
    'VE0011': (8500,   'Cancelado',  'Estoque em Falta'),
    'VE0012': (31000,  'Concluído',  ''),
    'VE0013': (4750,   'Cancelado',  'Cancelado pelo Cliente'),
    'VE0014': (27300,  'Concluído',  ''),
    'VE0015': (19900,  'Cancelado',  'Estoque em Falta'),
    'VE0016': (6200,   'Concluído',  ''),
    'VE0017': (14400,  'Cancelado',  'Cancelado pelo Cliente'),
    'VE0018': (33500,  'Concluído',  ''),
    'VE0019': (21750,  'Cancelado',  'Estoque em Falta'),
    'VE0020': (9870,   'Concluído',  ''),
    'VE0021': (45000,  'Concluído',  ''),
    'VE0022': (7100,   'Cancelado',  'Estoque em Falta'),
    'VE0023': (12900,  'Cancelado',  'Cancelado pelo Cliente'),
    'VE0024': (28600,  'Concluído',  ''),
    'VE0025': (16000,  'Cancelado',  'Estoque em Falta'),
}

def calculo_stockout(dicionario_vendas):
    numerador = 0
    denominador = 0
    for venda in vendas:
        valor, status, motivo = dicionario_vendas[venda]
        if status == 'Concluído':
            denominador += valor
        elif status == 'Cancelado' and motivo == 'Estoque em Falta':
            denominador += valor
            numerador += valor
    return numerador / denominador

percent_stockout = calculo_stockout(vendas)

print(f"O Percentual de stockout é: {percent_stockout:.2%}")

# %%
