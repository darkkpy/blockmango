from .http import HTTPMixin


BASE_URL_FRIEND = "http://modsgs.sandboxol.com/friend/api/v1"
BASE_URL_DECORATION = "http://modsgs.sandboxol.com/decoration/api/v1"


class Friends(HTTPMixin):
  __slots__ = ("headers",)

  def __init__(self, user_id, access_token):
    self.headers = { "userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1" }

  def delete_friend(self, friend_id):
    endpoint = f"{BASE_URL_FRIEND}/friends"
    params = { "friendId": friend_id }
    return self._delete(endpoint, headers=self.headers, params=params)

  def request(self, friend_id, msg):
    endpoint = f"{BASE_URL_FRIEND}/friends"
    payload = { "friendId": friend_id, "msg": msg, "type": 1 }
    headers = { **self.headers, "Content-Type": "application/json" }
    return self._post(endpoint, headers=headers, json_data=payload)

  def popularity(self, friend_id):
    return self._get(f"{BASE_URL_FRIEND}/popularity/{friend_id}", headers=self.headers)

  def info(self, friend_id):
    return self._get(f"{BASE_URL_FRIEND}/friends/{friend_id}", headers=self.headers)

  def decoration(self, friend_id):
    return self._get(f"{BASE_URL_DECORATION}/decorations-v2/{friend_id}/using", headers=self.headers)

  def add_popularity(self, friend_id):
    endpoint = f"{BASE_URL_FRIEND}/popularity"
    params = { "friendId": friend_id }
    return self._post(endpoint, headers=self.headers, params=params)

  def friend_list(self):
    endpoint = f"{BASE_URL_FRIEND}/friends/status"
    headers ={ **self.headers, "language": "en_US" }
    return self._get(endpoint, headers=headers)

  def nickname(self, friend_id, alias):
    endpoint = f"{BASE_URL_FRIEND}/friends/{friend_id}/alias"
    params = { "alias": alias }
    return self._post(endpoint, headers=self.headers, params=params)

  def friend_approve(self, friend_id):
    return self._put(f"{BASE_URL_FRIEND}/friends/{friend_id}/agreement", headers=self.headers)

  def friend_blacklist(self, friend_id):
    endpoint = f"{BASE_URL_FRIEND}/friends/black"
    params = { "friendId": friend_id }
    return self._delete(endpoint, headers=self.headers, params=params)

  def reject_all(self):
    return self._post(f"{BASE_URL_FRIEND}/friends/requests/reject-all", headers=self.headers)

  def approve_all(self):
    return self._post(f"{BASE_URL_FRIEND}/friends/requests/approve-all", headers=self.headers)

  def friend_reject(self, friend_id):
    return self._put(f"{BASE_URL_FRIEND}/friends/{friend_id}/rejection", headers=self.headers)
