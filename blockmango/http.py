import requests

class HTTPMixin:
    __slots__ = ()

    def _make_request(self, method, url, headers, json_data=None, params=None):
        methods = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete,
        }

        if method not in methods:
            raise ValueError(f"Invalid HTTP method: {method}")

        response = methods[method](url=url, headers=headers, json=json_data, params=params)
        return self._handle_response(response)

    def _handle_response(self, response):
        headers = response.headers

        if "Content-Type" not in headers:
            return {"error": "Content-Type is not present in the response", "code": 400}

        if not headers["Content-Type"].startswith("application/json"):
            return {"error": "Content-Type of the response wasn't application/json", "code": 415}

        return response.json()
