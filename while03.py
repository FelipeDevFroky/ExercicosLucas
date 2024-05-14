#Conta quantas pessoas são maiores de idade
cont_maior = 0
i = 0

while i < 5:
  idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
  if idade >= 18:
    cont_maior += 1
  i += 1

print(f"{cont_maior} pessoas são maiores de 18 anos.")



