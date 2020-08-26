from src.backend import Backend


def test_answer():
    backend = Backend()
    assert backend.get() == 5

