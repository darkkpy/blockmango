from .http import HTTPMixin
from .config import BASE_URL_USER, BASE_URL_ROUTE, BASE_URL_USER_INFO

class User(HTTPMixin):
    __slots__ = ("headers",)
    base_url = BASE_URL_USER

    def __init__(self, user_id, access_token):
        self.headers = {"userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1", "language": "en_US"}

    def get_user_info(self):
        return self._make_request('GET', f"{self.base_url}/v2/user/details/info", headers=self.headers)

    def set_birthday(self, birthday):
        return self._make_request('PUT', f"{BASE_URL_USER}/user/info", headers=self.headers, json_data={"birthday": birthday})

    def login(self, device_id, device_sign, password, userId):
        headers = {**self.headers, "bmg-sign": device_sign, "bmg-device-id": device_id}
        return self._make_request('POST', f"{BASE_URL_ROUTE}/v1/app/login", headers=headers, json_data={"password": password, "uid": userId})

    def change_name(self, new_name, old_name):
        return self._make_request('PUT', f"{BASE_URL_USER_INFO}/v3/user/nickName", headers=self.headers, params={"newName": new_name, "oldName": old_name})

    def change_details(self, new_details):
        return self._make_request('PUT', f"{BASE_URL_USER_INFO}/v1/user/info", headers=self.headers, json_data={"details": new_details})

    def change_pfp(self, pfp_url):
        return self._make_request('PUT', f"{BASE_URL_USER}/user/info", headers=self.headers, json_data={"picUrl": pfp_url})

    def modify_password(self, old_password, new_password):
        return self._make_request('POST', f"{BASE_URL_USER}/user/password/modify", headers=self.headers, json_data={"confirmPassword": "", "newPassword": new_password, "oldPassword": old_password})

    def bind_email(self, email, verify_code):
        return self._make_request('POST', f"{BASE_URL_USER}/users/bind/email", headers=self.headers, json_data={"email": email, "verifyCode": verify_code})

    def unbind_email(self, verify_code, email):
        return self._make_request('DELETE', f"{BASE_URL_USER_INFO}/v2/users/{self.headers['userId']}/emails", headers=self.headers, params={"email": email, "verifyCode": verify_code}) 
