from funciones.raiz_cuadrada_delgado import raiz_cuadrada_delgado

def test_raiz_cuadrada_delgado():
    assert raiz_cuadrada_delgado(9) == 3
    assert raiz_cuadrada_delgado(0) == 0
    assert raiz_cuadrada_delgado(-4) is None
