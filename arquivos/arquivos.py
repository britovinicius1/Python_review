#%%
nome_arquivo = "historia.txt"

##Abre o arquivo
open_file = open(nome_arquivo)

#%%
print(open_file)

# %%
#le os dados do arquivo
conteudo = open_file.read()
# %%
print(conteudo)
# %%
#fecha o arquivo
open_file.close()
# %%
### tem outra forma de fazer isso, tem uma forma mais comum e usual,
## enquanto esse arquvi estiver aberto, o arquivo fica com o nome open_file
#depois do escopo ele ja fecha o arquivo, sem precisar fechar

### lendo arquico ###

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)


# %%
