#%%
import pandas as pd
import sqlalchemy
from urllib.parse import quote_plus

#%%

senha = quote_plus("postgres")  # codifica caso tenha caracteres especiais (não é o caso aqui, mas é boa prática)

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/mydb")

clientes = pd.read_sql_table(table_name="dimcustomer", con=engine)

# %%