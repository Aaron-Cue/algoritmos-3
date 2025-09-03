def es_l_lindo(s, l='a'):
  if (len(s) == 1 and s[0] == l):
    return True
  
  medio = len(s) // 2
  
  if (len(s) > 1 and fullL(s[:medio], l) and es_l_lindo(s[medio:], chr(ord(l) + 1))):
    return True
  
  if (len(s) > 1 and fullL(s[medio:], l) and es_l_lindo(s[:medio], chr(ord(l) + 1))):
    return True
  
  return False
  
def fullL(str, l): 
  for i in str:
    if i != l:
      return False
  return True


def min_cant_movimientos(s, l='a'):
  if (es_l_lindo(s, l)):
    return 0
  if len(s) == 1:
    return 1
  
  # divido en 2
  medio = len(s) // 2
  s_izq = s[:medio] 
  s_der = s[medio:]
  sig_char = chr(ord(l) + 1)
  # hago fullL cada mitad contando los movs que hice
  
  # y llamo a esta funcion con esa mitad pero con l+1
  
  cantIzq = cant_mov_para_fullL(s_izq, l) + min_cant_movimientos(s_der, sig_char)
  cantDer = cant_mov_para_fullL(s_der, l) + min_cant_movimientos(s_izq, sig_char)
  
  ### devolver la minima cantidad de todos los caminos que hice  
  return min(cantIzq, cantDer)


def cant_mov_para_fullL(s, l):
  movs = 0
  for i in s:
    if i != l:
      movs += 1
  return movs


# cant casos analizar
# por cada caso, se dara 2 lineas: 
# 1: int -> |s| 
# 2: s

# print(min_cant_movimientos('aaaadcbb', 'a')) # 0
# print(min_cant_movimientos('bbaaceaa', 'a')) # 4
# print(min_cant_movimientos('jkghasdf', 'a')) # 7
# print(min_cant_movimientos('x', 'a')) # 1
# print(min_cant_movimientos('da', 'a')) # 1
# print(min_cant_movimientos('ccddaabb', 'a')) # 5

n = int(input())
for i in range(n):
  long = int(input())
  str = input()
  print(min_cant_movimientos(str, 'a'))
