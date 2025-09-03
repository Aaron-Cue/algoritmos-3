x, y = input().split()
x = int(x)
y = int(y)

def operacion_1(x): 
  return 2*x

def operacion_2(x): 
  return (10*x) + 1

def backtracking_ops(x, y, sol_parcial):

  if len(sol_parcial) == 0:
    sol_parcial.append(x)
  
  if x == y:
    return sol_parcial
  
  if x > y:
    return False
  
  sol_parcial1 = sol_parcial + [operacion_1(x)]
  sol_parcial2 = sol_parcial + [operacion_2(x)]
  
  res = backtracking_ops(operacion_1(x), y, sol_parcial1)
  if res:
    return res
  
  res = backtracking_ops(operacion_2(x), y, sol_parcial2)
  if res:
    return res
  
  return False


res = backtracking_ops(x, y, [])

if res == False: 
  print('NO')
else:
  print('YES')
  print(len(res))
  print(' '.join(map(str, res)))


