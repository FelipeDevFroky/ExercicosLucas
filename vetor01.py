def ler_vetor():
  """
  Função para ler um vetor de 5 números inteiros.

  Retorna:
    Um vetor contendo os 5 números inteiros lidos.
  """
  vetor = []
  for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor.append(numero)
  return vetor

def mostrar_vetor(vetor):
  """
  Função para mostrar os elementos de um vetor.

  Argumentos:
    vetor: O vetor a ser mostrado.
  """
  print("Vetor:", end=" ")
  for numero in vetor:
    print(numero, end=" ")
  print()

vetor = ler_vetor()
mostrar_vetor(vetor)
