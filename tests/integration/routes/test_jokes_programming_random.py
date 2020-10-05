import pytest
from tests.integration.utils.httpclient import HttpGetClient


@pytest.fixture
def jokes_random():
    return HttpGetClient("/jokes/programming/random")


def test_get_random_joke(jokes_random):
    """
    Validate that the returned Joke is of type "programming"
    """
    print("GET jokes/programming/random output : \n" + jokes_random.get_text_response())
    assert 200 == jokes_random.get_status()
    assert len(jokes_random.get_json_response()) == 1
    assert 'programming' == jokes_random.get_json_response()[0]['type']
