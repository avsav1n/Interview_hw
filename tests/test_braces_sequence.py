import os
import sys
sys.path.append(os.getcwd())

import pytest

import main


@pytest.mark.parametrize(
        'sequence', ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}'])
def test_braces_sequence_positive(sequence):
    res_func = main.check_braces_sequence(sequence)
    assert res_func == 'Сбалансированно'

@pytest.mark.parametrize(
        'sequence', ['}{}', '{{[(])]}}', '[[{())}]'])
def test_braces_sequence_negative(sequence):
    res_func = main.check_braces_sequence(sequence)
    assert res_func == 'Несбалансированно'
