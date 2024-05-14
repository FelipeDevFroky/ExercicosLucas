def ler_vetor_10_elementos():
  """
  Função para ler um vetor de 10 elementos do usuário.

  Retorna:
    Um vetor contendo os 10 elementos lidos.
  """
  vetor = []
  for i in range(10):
    elemento = input(f"Digite o {i + 1}º elemento: ")
    vetor.append(elemento)
  return vetor

def gerar_vetor_intercalado(vetor1, vetor2):
  """
  Função para gerar um vetor intercalado com elementos dos dois vetores originais.

  Argumentos:
    vetor1: O primeiro vetor com 10 elementos.
    vetor2: O segundo vetor com 10 elementos.

  Retorna:
    Um vetor de 20 elementos intercalados.
  """
  vetor_intercalado = []
  for i in range(10):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])
  return vetor_intercalado

def mostrar_vetores(nome_vetor, vetor):
  """
  Função para mostrar um vetor na tela.

  Argumentos:
    nome_vetor: O nome do vetor a ser impresso.
    vetor: O vetor a ser mostrado.
  """
  print(f"{nome_vetor}:", end=" ")
  for elemento in vetor:
    print(elemento, end=" ")
  print()

# Leitura dos vetores
vetor1 = ler_vetor_10_elementos()
vetor2 = ler_vetor_10_elementos()

# Geração do vetor intercalado
vetor_intercalado = gerar_vetor_intercalado(vetor1, vetor2)

# Impressão dos vetores
mostrar_vetores("Vetor 1", vetor1)
mostrar_vetores("Vetor 2", vetor2)
mostrar_vetores("Vetor Intercalado", vetor_intercalado)
