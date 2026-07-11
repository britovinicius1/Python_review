#%%

nome_arquivo = "historia.txt"

###%%enquanto o arquvo tiver aberto dps ele fecha
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)
#%%





open_file = open(nome_arquivo)

#%%
conteudo = open_file.read()
print(conteudo)

#%%
open_file.close()

#%%

#### Eescrever ###
nome_arquivo_2 = "historia_02.txt"
text = "meu novo arquivo resolviiiiii mudar o textoo"
with open (nome_arquivo_2, mode="w") as open_file:
    open_file.write(text)
