# tests/test_potenciachavez.py

# Importante: Le decimos al test dónde encontrar tu función
from funciones.potenciachavez import potencia_chavez

# Creamos el test para esa función
def test_potencia_chavez():
  assert potencia_chavez(2, 3) == 8
  assert potencia_chavez(5, 0) == 1
  assert potencia_chavez(3, 1) == 3