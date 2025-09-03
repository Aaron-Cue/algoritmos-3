# input -> cant casos de prueba, por cada caso valores n, m y matriz
# output -> YES or NO, si es posible o no camino minimo balanceado

# como busco camino mimino y solo se mueve en 2d, el camino tiene longitud n+m-1
# entonces el camino que busco es de esa longitud y debe ser par

def cambio_aulas(n, m, matriz):
  
  long = n + m - 1

  if long % 2 != 0:
    return "NO"
  
  # minimo y maximo posible hasta cada celda desde la casilla noroeste 
  min_s = [[0]*m for _ in range(n)]
  max_s = [[0]*m for _ in range(n)]

  for i in range(n):
    for j in range(m):
      valor = matriz[i][j]
      
      if i == 0 and j == 0:
        min_s[i][j] = valor # el valor de la celda
        max_s[i][j] = valor # el valor de la celda 
      else:
        min_pos = []
        max_pos = []
        if i > 0:
          min_pos.append(min_s[i-1][j]) # viene de arriba
          max_pos.append(max_s[i-1][j])
        if j > 0:
          min_pos.append(min_s[i][j-1]) # viene de la izq
          max_pos.append(max_s[i][j-1])
        min_s[i][j] = min(min_pos) + valor  # min acumulado
        max_s[i][j] = max(max_pos) + valor  # max acumulado
  
  # si la suma 0 esta dentro del rango posible en la celda final, se puede
  if min_s[n-1][m-1] <= 0 <= max_s[n-1][m-1]:
    return "YES"
  else:
    return "NO"
  
  
  
# lectura y salida
casos = int(input())
for _ in range(casos):
    n, m = map(int, input().split())
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().split()))
        matriz.append(fila)
    print(cambio_aulas(n, m, matriz))
    