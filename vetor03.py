def ler_notas():
  """
  Função para ler 4 notas do usuário.

  Retorna:
    Uma lista contendo as 4 notas lidas.
  """
  notas = []
  for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)
  return notas

def mostrar_notas_e_media(notas):
  """
  Função para mostrar as notas e a média na tela.

  Argumentos:
    notas: A lista contendo as 4 notas.
  """
  print("Notas:")
  for nota in notas:
    print(f"- {nota}")

  media = sum(notas) / len(notas)
  print(f"Média: {media:.2f}")

notas = ler_notas()
mostrar_notas_e_media(notas)
