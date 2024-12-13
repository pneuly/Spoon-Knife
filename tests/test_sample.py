from src.sample import add, subtract, print_path

def test_add(sample_numbers):
    print_path()
    result = add(sample_numbers["a"], sample_numbers["b"])
    assert result == 15

def test_subtract(sample_numbers):
    result = subtract(sample_numbers["a"], sample_numbers["b"])
    assert result == 5
