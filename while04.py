while True:
    try:
        numero = int(input("Digite um número entre 1 e 10: "))

        if 1 <= numero <= 10:
            break  # Sai do loop while se o número for válido
        else:
            print("Número inválido!")

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Tabuada do número
print(f"Tabuada do {numero}:")
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")

