import requests


class HttpGetClient(object):
    """
    Utility that provides a http get client for the joke server.
    """
    BASE_URL = "https://official-joke-api.appspot.com"

    def __init__(self, api):
        """
        :param api: string path of the api/end-point that needs to be called on the server
        """
        self.url = self.BASE_URL + api
        self.response = requests.get(self.url)

    def get_status(self):
        """
        returns http status code for the api
        :return: int return code
        """
        return self.response.status_code

    def get_json_response(self):
        """
        returns json response for the api
        :return: json list
        """
        return self.response.json()

    def get_text_response(self):
        """
        returns text response for the api
        :return: string
        """
        return self.response.text
