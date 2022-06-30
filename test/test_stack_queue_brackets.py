import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets

data_set = [
    ('{}', True),
    ('{}(){}', True),
    ('()[[Extra Characters]]', True),
    ('(){}[[]]', True),
    ('{}{Code}[Fellows](())', True),
    ('{(})', False),
    ('(](', False),
    ('[({}]', False),
    ('{', False),
    (')', False),
    ('}', False),
]


@pytest.mark.parametrize("string, boo", data_set)
def test_Stack_pop(string, boo):
    value = validate_brackets(string)
    assert value == boo


