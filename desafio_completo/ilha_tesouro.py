#Você é um explorador que naufragou em uma ilha misteriosa. 
# Seu objetivo é sobreviver por 10 dias, explorar o território, 
# coletar recursos e encontrar um tesouro escondido antes que sua energia acabe.
#O jogo funciona inteiramente no terminal, com escolhas do jogador,
#  eventos aleatórios, gerenciamento de recursos e um sistema de progressão.

import random

jogador = {
    "HEALTH": 100,
    "ENERGY": 100,
    "FOOD": 5,
    "WATER": 5,
    "WOOD": 0,
    "GOLD": 0,
    "DAY": 1
}

def explorar_ilha():
    print("\nVocê decidiu explorar a ilha...")

    eventos = {
    "Você encontrou um baú!": {"GOLD": +10},
    "Você foi atacado por um animal!": {"HEALTH": -20},
    "Você achou uma poção!": {"HEALTH": +15},
}
    texto = random.choice(list(eventos))
    print("")
    print(f"EVENTO: {texto}")

    for var, valor in eventos[texto].items():
        jogador[var] = jogador[var] + valor
        print(f"{var} : {valor:+}")

    input("\nPressione enter para continuar...")


def menu():
    print("="*50)
    print("Ilha do tesouro".center(50))
    print("="*50)

    print(f"DIA: {jogador['DAY']}/10")
    print(f"\n❤️  Vida: {jogador['HEALTH']}/100")
    print(f"⚡ Energia: {jogador['ENERGY']}/100 ")

    print(f"\nINVENTÁRIO")
    print(f"\n🍖 Comida: {jogador['FOOD']}")
    print(f"💧 Água: {jogador['WATER']}")
    print(f"🪵  Madeira: {jogador['WOOD']}")
    print(f"🪙  Ouro: {jogador['GOLD']}")


    print("="*50)
    print("O QUE DESEJA FAZER?")

    print("\n[1] Explorar Ilha")
    print("[2] Caçar")
    print("[3] Coletar água")
    print("[4] Cortar madeira")
    print("[5] Descansar")
    print("[6] Construir abrigo")
    print("[7] Procurar tesouro")
    print("[0] Encerrar jogo")


def main():
    while True:
        if jogador["HEALTH"] > 0 :
            menu()
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                explorar_ilha()
                jogador["DAY"] += 1
            
            elif opcao == '0':
                print("Jogo finalizado!...")
                break
        else:
            print("Você morreu =(")
            break    

if __name__ == '__main__':
    main()
# %%
