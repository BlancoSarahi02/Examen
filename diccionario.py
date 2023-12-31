def scooby(n):
  if n < 2: return False
  for i in range(2,int(n/2)+1):
    if n % i == 0: return False
  return True

def nextscooby (n):
  if not scooby(n): return False
  i = 0
  while True:
    i += 1
    if scooby(n+i): return n+i

def manzana(datos):
    mitad = len(datos) // 2
    datos.sort()
    return datos[mitad]

import random

def gen_manzana(n):
  contrasena = ""
  for i in range(1,n):
    contrasena += chr(random.randrange(33,126,1))
  return contrasena

def hip(a,b):
  return ((a**2) + (b**2))**.5
