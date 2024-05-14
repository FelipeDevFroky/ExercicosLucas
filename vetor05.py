def ler_vetor_20_numeros():
  """
  Função para ler 20 números inteiros do usuário e armazená-los em um vetor.

  Retorna:
    Um vetor contendo os 20 números inteiros lidos.
  """
  vetor = []
  for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)
  return vetor

def separar_pares_impares(vetor):
  """
  Função para separar os números pares e ímpares do vetor em dois vetores distintos.

  Argumentos:
    vetor: O vetor contendo os 20 números inteiros.

  Retorna:
    Uma tupla contendo dois vetores:
      - vetor_par: Vetor com os números pares.
      - vetor_impar: Vetor com os números ímpares.
  """
  vetor_par = []
  vetor_impar = []
  for numero in vetor:
    if numero % 2 == 0:
      vetor_par.append(numero)
    else:
      vetor_impar.append(numero)
  return vetor_par, vetor_impar

def mostrar_vetores(vetor, nome_vetor):
  """
  Função para mostrar um vetor na tela.

  Argumentos:
    vetor: O vetor a ser mostrado.
    nome_vetor: O nome do vetor a ser impresso.
  """
  print(f"{nome_vetor}:", end=" ")
  for elemento in vetor:
    print(elemento, end=" ")
  print()

# Leitura do vetor de 20 números
vetor = ler_vetor_20_numeros()

# Separação dos números pares e ímpares
vetor_par, vetor_impar = separar_pares_impares(vetor)

# Impressão dos vetores
mostrar_vetores(vetor, "Vetor original")
mostrar_vetores(vetor_par, "Vetor PAR")
mostrar_vetores(vetor_impar, "Vetor ÍMPAR")
