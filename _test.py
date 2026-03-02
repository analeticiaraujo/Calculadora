from calculadora import Calculadora

c = Calculadora()

def test_soma():
    assert c.soma(3, 4) == 7

def test_subtracao():
    assert c.subtracao(3, 4) == -1

def test_multiplicacao():
    assert c.multiplicacao(3, 4) == 12

def test_divisao():
    assert c.divisao(8, 4) == 2

def test_exponencial():
    assert c.exponencial(4, 2) == 16

def test_divisaoresto():
    assert c.divisaoresto(4, 3) == 1
