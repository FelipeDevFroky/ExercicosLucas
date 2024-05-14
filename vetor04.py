def ler_vetor_caracteres():
  """
  Função para ler um vetor de 10 caracteres do usuário.

  Retorna:
    Uma lista contendo os 10 caracteres lidos.
  """
  caracteres = []
  for i in range(10):
    caractere = input(f"Digite o {i + 1}º caractere: ")
    caracteres.append(caractere)
  return caracteres

def contar_e_mostrar_consoantes(caracteres):
  """
  Função para contar e mostrar as consoantes em um vetor de caracteres.

  Argumentos:
    caracteres: A lista contendo os 10 caracteres.
  """
  cont_consoantes = 0
  consoantes = []
  vogais = "aeiouAEIOU"

  for caractere in caracteres:
    if caractere not in vogais:
      cont_consoantes += 1
      consoantes.append(caractere)

  print(f"Número de consoantes: {cont_consoantes}")
  print("Consoantes:", end=" ")
  for consoante in consoantes:
    print(consoante, end=" ")
  print()

caracteres = ler_vetor_caracteres()
contar_e_mostrar_consoantes(caracteres)
