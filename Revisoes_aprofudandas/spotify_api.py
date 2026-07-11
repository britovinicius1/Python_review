#%%
import pandas as pd
import requests
import os

#%%

client_id = '13bd5e480661431d9411116a95d3bdbe'
client_secret = '81d4b88bb5ea4b8b8c4e8f38b4baf58b'


#%%
import base64

string = client_id + ':' + client_secret
string_bytes = string.encode('ascii')

base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode('ascii')
#%%
url = 'https://accounts.spotify.com/api/token'

headers = {'Authorization': f'Basic {base64_string}',
           'Content-Type': 'application/x-www-form-urlencoded'}

payload = {'grant_type': 'client_credentials'}

response = requests.request('POST', url = url, headers = headers, data = payload)



# %%
access_token = response.json()['access_token']
# %%
access_token
# %%
url = 'https://api.spotify.com/v1/tracks/6rqhFgbbKwnb9MLmUQDhG6'

headers = {'Authorization': f'Bearer {access_token}'}

response = requests.request('GET', url = url, headers = headers)

response.status_code
# %%
response.json()
# %%
total = 0

for i in range(1,4):
    total += (i * i - i)

print(total)

# %%
soma = 8 + 4 + 16 + 12
print(soma)
# %%
