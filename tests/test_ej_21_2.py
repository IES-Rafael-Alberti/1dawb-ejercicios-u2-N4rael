import pytest
from src.ej_21_2 import testPass

@pytest.mark.parametrize(
    "input, expected",
    [
        ("contraseña", "1"),
        ("CoNtrASeñA", "1"),
        ("contrAseña", "1"),
        ("1234", "2"),
        ("thecakeisalie", "2"),
        ("coca cola", "2")
    ]
)

def test_testPass(input, expected):
    assert testPass(input) == expected
