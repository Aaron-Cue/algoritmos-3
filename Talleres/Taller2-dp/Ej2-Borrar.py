n = int(input())
str = input()

# dict <letra, indices>
indices = {}
for indice, letra in enumerate(str):
  if letra not in indices:
    indices[letra] = []
  indices[letra].append(indice)


def cantidad_operaciones(s):
  dp = []
  for i in range(n):
    dp.append([0] * n)

  #casos base
  for i in range(n):
    dp[i][i] = 1
    

  # demas substrings
  for len_str in range(2, n+1):   
    # para cada desde    
    for d in range(0, n - len_str + 1):  
      # hasta
      h = d + len_str - 1         


      cant_min = 1 + dp[d+1][h] 

   
      # para cada indice que tiene la misma letra
      for k in indices[s[d]]:
        # si esta en rango
        if d < k <= h:
          # si es contigua =>  desde = k
          if k == d+1: 
            minim = min(cant_min, dp[k][h])
            cant_min = minim
          #no contigua 
          else:
            minim = min(cant_min, dp[d+1][k-1] + dp[k][h])
            cant_min = minim
          
      dp[d][h] = cant_min

  cantidad_ops = dp[0][n-1]
  
  return cantidad_ops

    
  


print(cantidad_operaciones(str))
