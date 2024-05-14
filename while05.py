def verificar_senha():
  """
  Função para verificar se a senha digitada está correta.

  Retorna:
    True se a senha estiver correta, False caso contrário.
  """
  senha_correta = "1234"  # Senha correta (substitua por sua senha real)
  senha_digitada = input("Digite a senha: ")

  return senha_digitada == senha_correta


while not verificar_senha():
  print("Senha Incorreta. Tente novamente.")

print("Senha Correta!")

