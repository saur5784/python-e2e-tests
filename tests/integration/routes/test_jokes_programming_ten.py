import pytest
from tests.integration.utils.httpclient import HttpGetClient


@pytest.fixture
def jokes_ten():
    return HttpGetClient("/jokes/programming/ten")


def test_get_ten_jokes(jokes_ten):
    """
    Validate that 10 jokes are returned
    """
    print("GET /jokes/programming/ten output : \n" + jokes_ten.get_text_response())
    assert 200 == jokes_ten.get_status()
    assert len(jokes_ten.get_json_response()) == 10


def test_get_ten_programming_jokes(jokes_ten):
    """
    Validate that all jokes are of type "programming"
    """
    print("GET /jokes/programming/ten output : \n" + jokes_ten.get_text_response())
    assert 200 == jokes_ten.get_status()
    assert len(jokes_ten.get_json_response()) > 0
    assert all('programming' == joke['type'] for joke in jokes_ten.get_json_response())
