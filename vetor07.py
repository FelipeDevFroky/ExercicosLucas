def ler_vetor_5_numeros():
  """
  Função para ler um vetor de 5 números inteiros do usuário.

  Retorna:
    Um vetor contendo os 5 números inteiros lidos.
  """
  vetor = []
  for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)
  return vetor

def calcular_soma_multiplicacao(vetor):
  """
  Função para calcular a soma e a multiplicação dos números do vetor.

  Argumentos:
    vetor: O vetor contendo os 5 números inteiros.

  Retorna:
    Uma tupla contendo:
      - soma: A soma dos números do vetor.
      - multiplicacao: A multiplicação dos números do vetor.
  """
  soma = 0
  multiplicacao = 1
  for numero in vetor:
    soma += numero
    multiplicacao *= numero
  return soma, multiplicacao

def mostrar_vetor_soma_multiplicacao(vetor, soma, multiplicacao):
  """
  Função para mostrar o vetor, a soma e a multiplicação dos números na tela.

  Argumentos:
    vetor: O vetor contendo os 5 números inteiros.
    soma: A soma dos números do vetor.
    multiplicacao: A multiplicação dos números do vetor.
  """
  print("Vetor:", end=" ")
  for numero in vetor:
    print(numero, end=" ")
  print()

  print(f"Soma: {soma}")
  print(f"Multiplicação: {multiplicacao}")

# Leitura do vetor de 5 números
vetor = ler_vetor_5_numeros()

# Cálculo da soma e multiplicação
soma, multiplicacao = calcular_soma_multiplicacao(vetor)

# Impressão do vetor, soma e multiplicação
mostrar_vetor_soma_multiplicacao(vetor, soma, multiplicacao)
