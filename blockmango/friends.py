import requests
from constants import BASE_URL_FRIEND, BASE_URL_DECORATION, HEADERS_TEMPLATE

class Friends:
    def __init__(self, user_id, access_token):
        self.headers = {
            **HEADERS_TEMPLATE,
            "userId": user_id,
            "Access-Token": access_token
        }

    def _handle_response(self, response):
        return response.json()

    def _get(self, base_url, endpoint, params=None):
        response = requests.get(f"{base_url}{endpoint}", headers=self.headers, params=params)
        return self._handle_response(response)

    def _post(self, base_url, endpoint, json_data=None, params=None):
        response = requests.post(f"{base_url}{endpoint}", headers=self.headers, json=json_data, params=params)
        return self._handle_response(response)

    def _delete(self, base_url, endpoint, params=None):
        response = requests.delete(f"{base_url}{endpoint}", headers=self.headers, params=params)
        return self._handle_response(response)

    def _put(self, base_url, endpoint, json_data=None, params=None):
        response = requests.put(f"{base_url}{endpoint}", headers=self.headers, json=json_data, params=params)
        return self._handle_response(response)

    def delete_friend(self, friend_id):
        endpoint = "/friends"
        params = {"friendId": friend_id}
        return self._delete(BASE_URL_FRIEND, endpoint, params)

    def friend_request(self, friend_id, msg):
        endpoint = "/friends"
        payload = {"friendId": friend_id, "msg": msg, "type": 1}
        headers = self.headers.copy()
        headers["Content-Type"] = "application/json"
        response = requests.post(f"{BASE_URL_FRIEND}{endpoint}", headers=headers, json=payload)
        return self._handle_response(response)

    def friend_popularity(self, friend_id):
        endpoint = f"/popularity/{friend_id}"
        return self._get(BASE_URL_FRIEND, endpoint)

    def friend_info(self, friend_id):
        endpoint = f"/friends/{friend_id}"
        return self._get(BASE_URL_FRIEND, endpoint)

    def friend_decoration(self, friend_id):
        endpoint = f"/decorations-v2/{friend_id}/using"
        return self._get(BASE_URL_DECORATION, endpoint)

    def add_popularity(self, friend_id):
        endpoint = "/popularity"
        params = {"friendId": friend_id}
        return self._post(BASE_URL_FRIEND, endpoint, params=params)

    def friend_list(self):
        endpoint = "/friends/status"
        headers = self.headers.copy()
        headers["language"] = "en_US"
        response = requests.get(f"{BASE_URL_FRIEND}{endpoint}", headers=headers)
        return self._handle_response(response)

    def friend_nickname(self, friend_id, alias):
        endpoint = f"/friends/{friend_id}/alias"
        params = {"alias": alias}
        return self._post(BASE_URL_FRIEND, endpoint, params=params)

    def friend_approve(self, friend_id):
        endpoint = f"/friends/{friend_id}/agreement"
        return self._put(BASE_URL_FRIEND, endpoint)

    def friend_blacklist(self, friend_id):
        endpoint = "/friends/black"
        params = {"friendId": friend_id}
        return self._delete(BASE_URL_FRIEND, endpoint, params)

    def reject_all(self):
        endpoint = "/friends/requests/approve-all"
        return self._post(BASE_URL_FRIEND, endpoint)

    def approve_all(self):
        endpoint = "/friends/requests/reject-all"
        return self._post(BASE_URL_FRIEND, endpoint)

    def friend_reject(self, friend_id):
        endpoint = f"/friends/{friend_id}/rejection"
        return self._put(BASE_URL_FRIEND, endpoint)
