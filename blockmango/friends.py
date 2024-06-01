#Upgraded friends.py
from .http import HTTPMixin
from .config import BASE_URL_FRIEND, BASE_URL_DECORATION

class Friends(HTTPMixin):
    __slots__ = ("headers",)
    base_url_friend = BASE_URL_FRIEND
    base_url_decoration = BASE_URL_DECORATION

    def __init__(self, user_id, access_token):
        self.headers = {"userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1", "language": "en_US"}

    def delete_friend(self, friend_id):
        return self._make_request('DELETE', f"{self.base_url_friend}/friends", headers=self.headers, params={"friendId": friend_id})

    def request(self, friend_id, msg):
        payload = {"friendId": friend_id, "msg": msg, "type": 1}
        return self._make_request('POST', f"{self.base_url_friend}/friends", headers=self.headers, json_data=payload)  

    def popularity(self, friend_id):
        return self._make_request('GET', f"{self.base_url_friend}/popularity/{friend_id}", headers=self.headers)

    def info(self, friend_id):
        return self._make_request('GET', f"{self.base_url_friend}/friends/{friend_id}", headers=self.headers)

    def decoration(self, friend_id):
        return self._make_request('GET', f"{self.base_url_decoration}/decorations-v2/{friend_id}/using", headers=self.headers)

    def add_popularity(self, friend_id):
        return self._make_request('POST', f"{self.base_url_friend}/popularity", headers=self.headers, params={"friendId": friend_id})

    def friend_list(self):
        headers = {"language": "en_US", **self.headers}
        return self._make_request('GET', f"{self.base_url_friend}/friends/status", headers=headers)

    def nickname(self, friend_id, alias):
        return self._make_request('POST', f"{self.base_url_friend}/friends/{friend_id}/alias", headers=self.headers, params={"alias": alias})

    def friend_approve(self, friend_id):
        return self._make_request('PUT', f"{self.base_url_friend}/friends/{friend_id}/agreement", headers=self.headers)

    def friend_blacklist(self, friend_id):
        return self._make_request('DELETE', f"{self.base_url_friend}/friends/black", headers=self.headers, params={"friendId": friend_id})

    def reject_all(self):
        return self._make_request('POST', f"{self.base_url_friend}/friends/requests/reject-all", headers=self.headers)

    def approve_all(self):
        return self._make_request('POST', f"{self.base_url_friend}/friends/requests/approve-all", headers=self.headers)

    def friend_reject(self, friend_id):
        return self._make_request('PUT', f"{self.base_url_friend}/friends/{friend_id}/rejection", headers=self.headers)
