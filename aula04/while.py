#%%
#faz até a condição ser satisfeita
i = 0
while i < 3:
    print(i)
    i = i +1
# %%
#A instrução ELSE é executada quando a condição while é falsa
i = 0
while i < 10:
    print(i)
    i = i + 1
else:
    print("\nNumero é maior ou igual a 10")

print("\n\nPrograma finalizado...")

# %%
##While, break e continue

i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i = i + 1

# %%
