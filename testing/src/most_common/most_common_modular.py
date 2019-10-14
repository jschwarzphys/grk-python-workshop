import requests
def most_common_word_in_web_page(words, url, useragent=requests):
    response = useragent.get(url)
    return most_common_words (words, response.text)

def most_common_words (words, text):
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]

if __name__ == '__main__':
    most_common = most_common_word_in_web_page(
         ['python', 'Python', 'programming'],
         'https://python.org/',
         )
    print(most_common)

######################################################################
## testing

def test_with_dummy_classes():
    class TestResponse():
        text = 'aa bbb c'
    class TestUserAgent():
        def get(self, url):
            return TestResponse()
    result = most_common_word_in_web_page(
        ['a', 'b', 'c'],
        'https://python.org/',
        useragent=TestUserAgent()
    )
    assert result == 'b', 'most_common_word_in_web_page tested with dummy classes'

def test_with_mock_objects():
    from unittest.mock import Mock
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'
    result = most_common_word_in_web_page(
         ['a', 'b', 'c'],
         'https://python.org/',
         useragent=mock_requests
    )
    assert result == 'b'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] == 'https://python.org/'

def test_with_patch():
    from unittest.mock import patch, Mock
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'
    with patch('most_common_modular.requests', mock_requests):
         result = most_common_word_in_web_page(
             ['a', 'b', 'c'],
             'https://python.org/'
            )
         assert result == 'b'
         assert mock_requests.get.call_count == 1
         assert mock_requests.get.call_args[0][0] == 'https://python.org/', 'called with right URL'
