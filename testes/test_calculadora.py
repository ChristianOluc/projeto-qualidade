from calculadora import soma, subtracao, multiplicacao, divisao
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_soma():
    assert soma(2, 3) == 5


def test_subtracao():
    assert subtracao(5, 3) == 2


def test_multiplicacao():
    assert multiplicacao(4, 3) == 12


def test_divisao():
    assert divisao(10, 2) == 5


def test_divisao_por_zero():
    try:
        divisao(10, 0)
        assert False
    except ValueError:
        assert True
