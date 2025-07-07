import requests

class HttpClient:
    def __init__(self, headers: dict):
        self.headers = headers

    def get(self, url: str) -> str:
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.text
