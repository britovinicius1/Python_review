#%%

preco_imoveis = [2.17,1.54,1.45,2.37,1.7,1.9]
tamanho_imoveis = [207,104,203,130,220,147]

#10% para teste

fator = 0.2

i = int((1 - fator) * len(preco_imoveis))
precos_treino = preco_imoveis[:i]
preco_teste = preco_imoveis[i:]

print(preco_teste)

# %%
precos_imoveis = [2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37,
                  1.62, 2.05, 1.88, 2.41, 1.73, 1.99, 2.15, 1.56, 2.28, 1.84,
                  1.47, 2.33, 1.91, 2.08, 1.65, 2.19, 1.78, 2.44, 1.52, 2.02,
                  1.86, 2.27, 1.69, 2.11, 1.95, 2.38, 1.74, 2.06, 1.83, 2.22,
                  1.58, 2.35, 1.92, 2.13, 1.67, 2.29, 1.81, 2.47, 1.55, 2.04,
                  1.89, 2.31, 1.71, 2.16, 1.97, 2.42, 1.76, 2.09, 1.85, 2.24,
                  1.60, 2.36, 1.93, 2.14, 1.68, 2.26, 1.82, 2.48, 1.53, 2.03,
                  1.87, 2.32, 1.72, 2.17, 1.96, 2.43, 1.77, 2.07, 1.84, 2.21,
                  1.59, 2.34, 1.90, 2.12, 1.66, 2.28, 1.80, 2.46, 1.54, 2.01,
                  1.88, 2.30, 1.70, 2.15, 1.98, 2.40, 1.75, 2.10, 1.83, 2.23]

tamanho_imoveis = [207, 148, 130, 203, 257, 228, 160, 194, 232, 147,
                   175, 218, 195, 241, 163, 209, 235, 152, 248, 186,
                   142, 223, 197, 214, 168, 239, 178, 255, 155, 202,
                   189, 227, 171, 219, 198, 243, 165, 208, 183, 236,
                   158, 245, 192, 213, 167, 229, 181, 252, 153, 205,
                   190, 231, 172, 216, 200, 247, 176, 211, 185, 224,
                   161, 237, 193, 215, 169, 233, 182, 258, 154, 204,
                   188, 226, 173, 220, 196, 244, 177, 210, 184, 222,
                   159, 238, 191, 212, 166, 230, 180, 251, 156, 203,
                   187, 225, 170, 217, 199, 246, 174, 212, 183, 228]

def separa_listas(precos,tamanhos,fator=0.1):
    if len(precos) == len(tamanhos):
        i = int((1-fator)*len(precos))
        precos_imoveis_treino = precos[:i]
        precos_imoveis_teste = precos[i:]
        tamanho_imoveis_treino = tamanhos[:i]
        tamanho_imoveis_teste = tamanhos[i:]
        return (precos_imoveis_treino,precos_imoveis_teste,tamanho_imoveis_treino,tamanho_imoveis_teste)
    else:
        print("A listas de preços nao são do mesmo tamanho...")
        return None

# %%
w,x,y,z = separa_listas(precos_imoveis,tamanho_imoveis)
print(x)
# %%

