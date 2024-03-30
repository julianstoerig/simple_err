from simple_err.trying import trying, wrap_in_trying, trying_genexpr
import operator as op
import math


def test_ok_case():
    res = trying(lambda: 5/5)
    assert res == 1.0


def test_err_case():
    res = trying(lambda: 5/0)
    assert isinstance(res, ZeroDivisionError)


def test_trying_wrapper_ok_case():
    wrapped = wrap_in_trying(op.truediv)

    assert wrapped(5, 5) == 1
    
    
def test_trying_wrapper_zero_div():
    wrapped = wrap_in_trying(op.truediv)

    assert isinstance(wrapped(5, 0), ZeroDivisionError)


def test_trying_wrapper_value_error():
    wrapped = wrap_in_trying(math.sqrt)

    assert wrapped(0) == 0
    assert isinstance(wrapped(-1), ValueError)


def test_trying_key_error():
    k = {0: 15}
    assert isinstance(trying_genexpr(
        (k[1] for _ in (0,))
    ), KeyError)
