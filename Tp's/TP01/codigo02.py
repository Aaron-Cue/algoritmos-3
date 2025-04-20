# input -> dos lineas, s1 y s2, s1 es la secuencia dictada original y s2 es la secuencia escuchada
# output -> num real, indica la probabilidad de que este en la posicion correcta
# + -> avanzar, - -> retroceder, ? -> no escucho => mueve con 50% de probabilidad hacia adelante o hacia atras

def calcular_posicion_correcta(sec):
  posicion_correcta = 0
  for movimiento in sec:
    if movimiento == '+':
      posicion_correcta += 1
    else:
      posicion_correcta -= 1
  return posicion_correcta


# calcula la cantidad de soluciones posibles
def backtrack(s2, i_actual, pos_actual, objetivo):
  # si ya no hay mas instrucciones. chequear si la solucion es valida
  if i_actual == len(s2):
    if pos_actual == objetivo:
      return 1
    else: 
      return 0

  if s2[i_actual] == '+':
    return backtrack(s2, i_actual + 1, pos_actual + 1, objetivo)
  elif s2[i_actual] == '-':
    return backtrack(s2, i_actual + 1, pos_actual - 1, objetivo)
  else: # s2[i_actual] == '?'
    return (
      backtrack(s2, i_actual + 1, pos_actual + 1, objetivo) +
      backtrack(s2, i_actual + 1, pos_actual - 1, objetivo)
    )


def calcular_probabilidad(s1, s2):
  objetivo = calcular_posicion_correcta(s1)
  
  if s2.count('?') > 0:
    posibilidades_totales = 2 ** s2.count('?') # 2^(cantidad de '?')
  else:
    return 1.0 if calcular_posicion_correcta(s2) == calcular_posicion_correcta(s1) else 0.0 # porque posibilidades_totales es 1

  casos_correctos = backtrack(s2, 0, 0, objetivo)
  return casos_correctos / posibilidades_totales

# lectura
s1 = input()
s2 = input()

# salida
resultado = calcular_probabilidad(s1, s2)
print(round(resultado, 12))
