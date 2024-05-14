def ler_vetor():
  """
  Função para ler um vetor de 10 números reais.

  Retorna:
    Um vetor contendo os 10 números reais lidos.
  """
  vetor = []
  for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    vetor.append(numero)
  return vetor

def mostrar_vetor_inverso(vetor):
  """
  Função para mostrar os elementos de um vetor na ordem inversa.

  Argumentos:
    vetor: O vetor a ser mostrado na ordem inversa.
  """
  print("Vetor na ordem inversa:", end=" ")
  for i in range(len(vetor) - 1, -1, -1):
    print(vetor[i], end=" ")
  print()

vetor = ler_vetor()
mostrar_vetor_inverso(vetor)
