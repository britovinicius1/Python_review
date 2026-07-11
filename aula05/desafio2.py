#%%
#crie uma função para calcular os clientes inadimpletes
#retorne os cnpjs inadimplentes
# Cliente inadimplente ->  +1000 reais por +20 dias.

clientes_devedores = [
    ('462.286.561-65', 14405, 24),
    ('251.569.170-81', 16027,  1),
    ('297.681.579-21',  8177, 28),
    ('790.223.154-40',  9580, 12),
    ('134.872.390-17', 21300,  5),
    ('583.914.267-33', 17650,  9),
    ('920.347.618-55',  4320, 31),
    ('671.058.293-44', 12890,  7),
    ('348.729.015-88', 33100,  2),
    ('815.463.702-96',  6750, 19),
    ('229.381.047-62', 28400,  4),
    ('497.630.158-71', 11200, 15),
    ('763.025.849-30',  9930, 22),
    ('152.874.603-59', 44800,  1),
    ('608.319.274-85', 13570,  8),
    ('371.256.980-14',  7890, 17),
    ('984.102.365-27', 19400,  6),
    ('546.873.021-43', 25600,  3),
    ('213.698.754-91',  5340, 26),
    ('879.041.236-68', 31750,  2),
    ('425.317.869-50', 18200, 11),
    ('691.584.230-76',  3980, 34),
    ('137.920.486-15', 22900,  5),
    ('804.263.571-89', 16340, 13),
    ('562.748.103-37',  8760, 20),
]

def clientes_inadip(lista_cpfs):
    lista_inadip = []
    for cliente in clientes_devedores:
        cpf, valor, dias = cliente
        if valor > 1000 and dias > 20:
            lista_inadip.append(cpf)
    return lista_inadip

print(clientes_inadip(clientes_devedores))
print(len(clientes_inadip(clientes_devedores)))
print(len(clientes_devedores))

# %%
