from calculadora import Calculadora

c = Calculadora()

def test_soma():
    assert c.soma(27, 8) == 35

def test_subtracao():
    assert c.subtracao(27, 8) == 19

def test_multiplicacao():
    assert c.multiplicacao(27, 8) == 216

def test_divisao():
    assert c.divisao(27, 8) == 3.375

def test_exponencial():
    assert c.exponencial(27, 8) == 282429536481

def test_divisaoresto():
    assert c.divisaoresto(27, 8) == 3
