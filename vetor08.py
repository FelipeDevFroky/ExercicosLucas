def ler_idades_alturas():
  """
  Função para ler as idades e alturas de 5 pessoas e armazená-las em vetores.

  Retorna:
    Uma tupla contendo:
      - idades: Um vetor contendo as idades das 5 pessoas.
      - alturas: Um vetor contendo as alturas das 5 pessoas.
  """
  idades = []
  alturas = []
  for i in range(1, 6):
    print(f"\nPessoa {i}:")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    idades.append(idade)
    alturas.append(altura)
  return idades, alturas

def mostrar_idades_alturas_inversa(idades, alturas):
  """
  Função para mostrar as idades e alturas na ordem inversa à ordem lida.

  Argumentos:
    idades: O vetor contendo as idades das 5 pessoas.
    alturas: O vetor contendo as alturas das 5 pessoas.
  """
  print("\nResultados na ordem inversa:")
  for i in range(len(idades) - 1, -1, -1):
    print(f"Pessoa {i + 1}: idade = {idades[i]}, altura = {alturas[i]:.2f}")

# Leitura das idades e alturas
idades, alturas = ler_idades_alturas()

# Impressão das idades e alturas na ordem inversa
mostrar_idades_alturas_inversa(idades, alturas)
