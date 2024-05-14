def ler_notas_alunos():
  """
  Função para ler as notas de 10 alunos.

  Retorna:
    Uma lista de listas, onde cada lista interna contém as 4 notas de um aluno.
  """
  notas_alunos = []
  for i in range(1, 11):
    print(f"\nAluno {i}:")
    notas_aluno = []
    for j in range(4):
      nota = float(input(f"Digite a nota {j + 1}: "))
      notas_aluno.append(nota)
    notas_alunos.append(notas_aluno)
  return notas_alunos

def calcular_medias(notas_alunos):
  """
  Função para calcular as médias das notas de cada aluno.

  Argumentos:
    notas_alunos: A lista de listas contendo as notas de cada aluno.

  Retorna:
    Uma lista contendo as médias de cada aluno.
  """
  medias = []
  for notas_aluno in notas_alunos:
    media = sum(notas_aluno) / len(notas_aluno)
    medias.append(media)
  return medias

def contar_alunos_media_maior_igual_7(medias):
  """
  Função para contar o número de alunos com média maior ou igual a 7.0.

  Argumentos:
    medias: A lista contendo as médias de cada aluno.

  Retorna:
    O número de alunos com média maior ou igual a 7.0.
  """
  cont_media_maior_igual_7 = 0
  for media in medias:
    if media >= 7.0:
      cont_media_maior_igual_7 += 1
  return cont_media_maior_igual_7

# Leitura das notas dos alunos
notas_alunos = ler_notas_alunos()

# Cálculo das médias
medias = calcular_medias(notas_alunos)

# Contagem de alunos com média maior ou igual a 7
cont_media_maior_igual_7 = contar_alunos_media_maior_igual_7(medias)

# Impressão dos resultados
print("\nResultados:")
for i, media in enumerate(medias):
  print(f"Aluno {i + 1}: média = {media:.2f}")

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {cont_media_maior_igual_7}")
