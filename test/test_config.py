from src.config import Config


def test_config_api_returns_correct_url():
    assert Config().api_url() == "https://jsonplaceholder.typicode.com"
