n = int(input())
valores = list(map(int, input().split(" ")))
palabras = []

for i in range(n):
  palabras.append(input())
  

def estan_ordenadas(palabras):
  res = True
  for i in range(0, len(palabras) - 1):
    if palabras[i] > palabras[i+1]:
      res = False
  return res


def menor_costo_palabras(palabras, valores, n):
  # verificar caso base: si sin dar vuelta nada, esta ord => retornar 0
  if (estan_ordenadas(palabras)):
    return 0
  
  palabras_reverse = [] 
  for palabra in palabras:
    palabras_reverse.append(palabra[::-1])
  
  menor_costo = float('inf')

  
  # dp_estr[i][0] -> menor costo hasta i si no invierto
  # dp_estr[i][1] -> menor costo hasta i si invierto
  dp_estr = []
  for _ in range(n):
    dp_estr.append([menor_costo, menor_costo])

  # caso base -> primera palabra
  dp_estr[0][0] = 0            
  dp_estr[0][1] = valores[0]  

  # para las demas palabras
  for i in range(1, n):
    
    # caso no invertidas
    # comparar con anterior sin invertir
    if palabras[i] >= palabras[i-1]:
      dp_estr[i][0] = min(dp_estr[i][0], dp_estr[i-1][0])
      
    # comparar con anterior invirtiendo
    if palabras[i] >= palabras_reverse[i-1]:
      dp_estr[i][0] = min(dp_estr[i][0], dp_estr[i-1][1])


    # caso invertidas
    if palabras_reverse[i] >= palabras[i-1]:
      dp_estr[i][1] = min(dp_estr[i][1], dp_estr[i-1][0] + valores[i])

    if palabras_reverse[i] >= palabras_reverse[i-1]:
      dp_estr[i][1] = min(dp_estr[i][1], dp_estr[i-1][1] + valores[i])

  res = min(dp_estr[n-1][0], dp_estr[n-1][1])

  if res >= menor_costo:
    return -1
  else:
    return res
  
print(menor_costo_palabras(palabras, valores, n))
