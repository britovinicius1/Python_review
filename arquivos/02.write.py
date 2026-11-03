#%%
nome_arquivo = "historia2.txt"

texto = "meu novo arquivo!! Esqueci de adicionar o nome... do arquivo"


# o default r -> Read "r"
# escrita, write ->  "w" (#overwrite)
#se escrever denovo ele vai sobrescrever. Ele apaga e escreve denovo, por conta do modo write


with open(nome_arquivo, mode="w") as open_file:
    open_file.write(texto)
# %%
text2 = "\nnovas informações!!"
#com o comando a ele adiciona novas informações (#append)
with open(nome_arquivo, mode="a", encoding="utf-8" ) as open_file:
    open_file.write(text2)
# %%

arquivo_sql = "text.sql"

with open(arquivo_sql, mode="r") as open_sql:
    query = open_sql.read()

# %%
print(query)
# %%
### lendo csv