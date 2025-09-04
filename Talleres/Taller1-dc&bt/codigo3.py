n, l, r = map(int, input().split(' '))
 
def kantUnos(n, l, r):
  if n == 0:
    return 0
  if n == 1:
    if l <=1 and r>=1:
      return 1
    else:
      return 0
    
  tam = calc_tam(n // 2)
  cant_1s = 0
  
  # izq
  if l <= tam:
    if r <= tam: 
      cant_1s += kantUnos(n // 2, l, r)
    else:
      cant_1s += kantUnos(n // 2, l, tam)

  if l <= tam + 1 and r >= tam + 1:
    if n % 2 == 1:
      cant_1s += 1
    else:
      cant_1s += 0 

  # der
  if r > tam + 1:
    new_l = l - (tam + 1)
    new_r = r - (tam + 1)

    if new_l < 1:
      new_l = 1
    if new_r > tam:
      new_r = tam

    cant_1s += kantUnos(n // 2, new_l, new_r)

  return cant_1s


def calc_tam(n):
  if n > 1:
    return 2* calc_tam(n // 2) + 1
  else:
    return 1
 

res = kantUnos(n, l, r)
 
print(res)


