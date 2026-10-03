def dizer_oi(nome):
    print(f"Oi, {nome}!")

print("__name__ aqui vale:", __name__)

if __name__ == '__main__':
    print("Rodei direto, então vou testar:")
    dizer_oi("Teste")