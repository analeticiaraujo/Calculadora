from calculadora import Calculadora

def test_soma():
    calc = Calculadora()
    assert calc.soma(3, 4) == 7

def test_subtracao():
    calc = Calculadora()
    assert calc.subtracao(3, 4) == -1

def test_multiplicacao():
    calc = Calculadora()
    assert calc.multiplicacao(3, 4) == 12

def test_divisao():
    calc = Calculadora()
    assert calc.divisao(8, 4) == 2

def test_exponencial():
    calc = Calculadora()
    assert calc.exponencial(4, 2) == 16

def test_divisaoresto():
    calc = Calculadora()
    assert calc.divisaoresto(4, 3) == 1
