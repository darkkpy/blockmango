import requests

class HTTPMixin:
    __slots__ = ()

    @staticmethod
    def _handle_response(response):
        headers = response.headers

        if "Content-Type" not in headers:
            return { "error": "Content-Type is not present in the response", "code": 400 }

        if not headers["Content-Type"].startswith("application/json"):
            return { "error": "Content-Type of the response wasn't application/json", "code": 415 }

        return response.json()

    def _get(self, url, headers, params=None):
        response = requests.get(url=url, headers=headers, params=params)
        return self._handle_response(response)

    def _post(self, url, headers, json_data=None, params=None):
        response = requests.post(url=url, headers=headers, json=json_data, params=params)
        return self._handle_response(response)

    def _put(self, url, headers, json_data=None, params=None):
        response = requests.put(url=url, headers=headers, json=json_data, params=params)
        return self._handle_response(response)

    def _delete(self, url, headers, params=None):
        response = requests.delete(url=url, headers=headers, params=params)
        return self._handle_response(response)
