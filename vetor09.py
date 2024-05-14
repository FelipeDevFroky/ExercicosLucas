def ler_vetor_10_numeros():
  """
  Função para ler um vetor de 10 números inteiros do usuário.

  Retorna:
    Um vetor contendo os 10 números inteiros lidos.
  """
  vetor = []
  for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)
  return vetor

def calcular_soma_quadrados(vetor):
  """
  Função para calcular a soma dos quadrados dos elementos do vetor.

  Argumentos:
    vetor: O vetor contendo os 10 números inteiros.

  Retorna:
    A soma dos quadrados dos elementos do vetor.
  """
  soma_quadrados = 0
  for numero in vetor:
    soma_quadrados += numero ** 2
  return soma_quadrados

def mostrar_soma_quadrados(vetor, soma_quadrados):
  """
  Função para mostrar o vetor e a soma dos quadrados dos elementos na tela.

  Argumentos:
    vetor: O vetor contendo os 10 números inteiros.
    soma_quadrados: A soma dos quadrados dos elementos do vetor.
  """
  print("Vetor:", end=" ")
  for numero in vetor:
    print(numero, end=" ")
  print()

  print(f"Soma dos quadrados: {soma_quadrados}")

# Leitura do vetor de 10 números
vetor = ler_vetor_10_numeros()

# Cálculo da soma dos quadrados
soma_quadrados = calcular_soma_quadrados(vetor)

# Impressão do vetor e da soma dos quadrados
mostrar_soma_quadrados(vetor, soma_quadrados)
