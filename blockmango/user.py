from .http import HTTPMixin


BASE_URL_USER = "http://modsgs.sandboxol.com/user/api/v1"
BASE_URL_ROUTE = "http://route.sandboxol.com/user/api"


class User(HTTPMixin):
  __slots__ = ("headers",)

  def __init__(self, user_id, access_token):
    self.headers = { "userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1" }

  def get_user_info(self):
    return self._get(f"{BASE_URL_USER}/v2/user/details/info", headers=self.headers)

  def set_birthday(self, birthday):
    endpoint = f"{BASE_URL_USER}/v1/user/info"
    json_data = { "birthday": birthday }
    return self._put(endpoint, headers=self.headers, json_data=json_data)

  def login(self, device_id, device_sign, password, userId):
    endpoint = f"{BASE_URL_ROUTE}/v1/app/login"
    headers = { **self.headers, "bmg-sign": device_sign, "bmg-device-id": device_id }
    json_data = { "password": password, "uid": userId }
    return self._post(endpoint, headers=headers, json_data=json_data)

  def change_name(self, new_name, old_name):
    endpoint = f"{BASE_URL_USER}/v3/user/nickName"
    params = { "newName": new_name, "oldName": old_name }
    return self._put(endpoint, headers=self.headers, params=params)

  def change_details(self, new_details):
    endpoint = f"{BASE_URL_USER}/v1/user/info"
    json_data = { "details": new_details }
    return self._put(endpoint, headers=self.headers, json_data=json_data)

  def change_pfp(self, pfp_url):
    endpoint = f"{BASE_URL_USER}/v1/user/info"
    json_data = { "picUrl": pfp_url }
    return self._put(endpoint, headers=self.headers, json_data=json_data)

  def modify_password(self, old_password, new_password):
    endpoint = f"{BASE_URL_USER}/v1/user/password/modify"
    json_data = {"confirmPassword": "", "newPassword": new_password, "oldPassword": old_password}
    return self._post(endpoint, headers=self.headers, json_data=json_data)

  def bind_email(self, email, verify_code):
    endpoint = f"{BASE_URL_USER}/v1/users/bind/email"
    json_data = { "email": email, "verifyCode": verify_code }
    return self._post(endpoint, headers=self.headers, json_data=json_data)

  def unbind_email(self, verify_code, email):
    endpoint = f"{BASE_URL_USER}/v2/users/{self.headers['userId']}/emails"
    params = { "email": email, "verifyCode": verify_code }
    return self._delete(endpoint, headers=self.headers, params=params)