import requests
from constants import BASE_URL_USER, BASE_URL_ROUTE, HEADERS_TEMPLATE

class User:
    def __init__(self, user_id, access_token):
        self.headers = {
            **HEADERS_TEMPLATE,
            "userId": user_id,
            "Access-Token": access_token
        }

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()

    def _get(self, base_url, endpoint, params=None):
        response = requests.get(f"{base_url}{endpoint}", headers=self.headers, params=params)
        return self._handle_response(response)

    def _post(self, base_url, endpoint, json_data=None, params=None):
        response = requests.post(f"{base_url}{endpoint}", headers=self.headers, json=json_data, params=params)
        return self._handle_response(response)

    def _put(self, base_url, endpoint, json_data=None, params=None):
        response = requests.put(f"{base_url}{endpoint}", headers=self.headers, json=json_data, params=params)
        return self._handle_response(response)

    def _delete(self, base_url, endpoint, params=None):
        response = requests.delete(f"{base_url}{endpoint}", headers=self.headers, params=params)
        return self._handle_response(response)

    def get_user_info(self):
        endpoint = "/v2/user/details/info"
        return self._get(BASE_URL_USER, endpoint)

    def birthday(self, birthday):
        endpoint = "/v1/user/info"
        json_data = {"birthday": birthday}
        return self._put(BASE_URL_USER, endpoint, json_data=json_data)

    def login(self, device_id, device_sign, password, userId):
        endpoint = "/v1/app/login"
        headers = {
            **self.headers,
            "bmg-sign": device_sign,
            "bmg-device-id": device_id
        }
        json_data = {"password": password, "uid": userId}
        response = requests.post(f"{BASE_URL_ROUTE}{endpoint}", headers=headers, json=json_data)
        return self._handle_response(response)

    def change_name(self, new_name):
        endpoint = "/v3/user/nickName"
        params = {"newName": new_name, "oldName": "darkk.py"}
        return self._put(BASE_URL_USER, endpoint, params=params)

    def change_details(self, new_details):
        endpoint = "/v1/user/info"
        json_data = {"details": new_details}
        return self._put(BASE_URL_USER, endpoint, json_data=json_data)

    def change_pfp(self, pfp_url):
        endpoint = "/v1/user/info"
        json_data = {"picUrl": pfp_url}
        return self._put(BASE_URL_USER, endpoint, json_data=json_data)

    def modify_password(self, old_password, new_password):
        endpoint = "/v1/user/password/modify"
        json_data = {"confirmPassword": "", "newPassword": new_password, "oldPassword": old_password}
        return self._post(BASE_URL_USER, endpoint, json_data=json_data)

    def bind_email(self, email, verify_code):
        endpoint = "/v1/users/bind/email"
        json_data = {"email": email, "verifyCode": verify_code}
        return self._post(BASE_URL_USER, endpoint, json_data=json_data)

    def unbind_email(self, verify_code, email):
        endpoint = f"/v2/users/{self.headers['userId']}/emails"
        params = {"email": email, "verifyCode": verify_code}
        return self._delete(BASE_URL_USER, endpoint, params=params)
