#%%
#107)
import modules as md


percent_up = 10
percent_down = 13

p = float(input("Digite o preço R$: "))
print(f"A metade de {md.moeda(p)} é {md.moeda(md.metade(p))}")
print(f"O dobro de {md.moeda(p)} é {md.moeda(md.dobrar(p))}")
print(f"Aumentando {percent_up}%, temos {md.moeda(md.aumentar_percent(p, 10))}")
print(f"Reduzindo {percent_down}%, temos {md.moeda(md.diminuir_percent(p, 13))}")

# %%
p = float(input("Digite o preço R$: "))
print(f"A metade de {md.moeda(p)} é {md.moeda(md.metade(p))}")
print(f"O dobro de {md.moeda(p)} é {md.moeda(md.dobrar(p))}")
print(f"Aumentando {percent_up}%, temos {md.moeda(md.aumentar_percent(p, 10))}")
print(f"Reduzindo {percent_down}%, temos {md.moeda(md.diminuir_percent(p, 13))}")