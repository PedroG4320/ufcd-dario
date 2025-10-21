def jogar_ppt(jogador1: str, jogador2: str) -> str:
    p1 = jogador1.lower()
    p2 = jogador2.lower()

    if p1 == p2:
        return "Empate!"

    match (p1, p2):
        case ("pedra", "tesoura") | ("papel", "pedra") | ("tesoura", "papel"):
            return "Jogador 1 venceu!"
        case ("tesoura", "pedra") | ("pedra", "papel") | ("papel", "tesoura"):
            return "Jogador 2 venceu!"
        case _:
            return "Jogada inválida."


if __name__ == "__main__":
    j1 = input("Jogador 1, escolha pedra, papel ou tesoura: ")
    j2 = input("Jogador 2, escolha pedra, papel ou tesoura: ")
    resultado = jogar_ppt(j1, j2)
    print(resultado)

