from linter.helpers import pascal_case_to_snake_case, snake_case_to_pascal_case


def test_pascal_case_to_snake_case_successfully_converts_pascal_to_snake() -> None:
    input = 'TestPascalStr'
    expected_output = 'test_pascal_str'
    assert pascal_case_to_snake_case(input) == expected_output


def test_pascal_case_to_snake_case_successfully_converts_snake_to_snake() -> None:
    input = 'test_snake_str'
    expected_output = 'test_snake_str'
    assert pascal_case_to_snake_case(input) == expected_output


def test_pascal_case_to_snake_case_successfully_converts_hybrid_to_snake() -> None:
    input = 'test_hybridStr'
    expected_output = 'test_hybrid_str'
    assert pascal_case_to_snake_case(input) == expected_output


def test_pascal_case_to_snake_case_does_not_strip_symbols() -> None:
    input = 'test_snake_str***'
    expected_output = 'test_snake_str***'
    assert pascal_case_to_snake_case(input) == expected_output


def test_snake_case_to_pascal_case_successfully_converts_snake_to_pascal() -> None:
    input = 'test_snake_str'
    expected_output = 'TestSnakeStr'
    assert snake_case_to_pascal_case(input) == expected_output


# def test_snake_case_to_pascal_case_successfully_converts_pascal_to_pascal() -> None:
#     input = 'TestPascalStr'
#     expected_output = 'TestPascalStr'
#     assert snake_case_to_pascal_case(input) == expected_output


# def test_snake_case_to_pascal_case_successfully_converts_hybrid_to_pascal() -> None:
#     input = 'test_hybridStr'
#     expected_output = 'TestHybridStr'
#     assert snake_case_to_pascal_case(input) == expected_output


# def test_snake_case_to_pascal_case_does_not_strip_symbols() -> None:
#     input = 'TestPascalStr***'
#     expected_output = 'TestPascalStr***'
#     assert snake_case_to_pascal_case(input) == expected_output
