import requests
import json

class User:
    def __init__(self, user_id, access_token):
        self.user_id = user_id
        self.access_token = access_token
        self.headers = {
            "userId": user_id,
            "Access-Token": access_token,
            "User-Agent": "okhttp/3.12.1"
        }

    def get_user_info(self):
        url = "http://modsgs.sandboxol.com/user/api/v2/user/details/info"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)
        
    def birthday(self, birthday):
    	url = "http://modsgs.sandboxol.com/user/api/v1/user/info"
    	json = {"birthday": birthday}
    	response = requests.put(url, json=json, headers = self.headers)
    	return self._handle_response(response)
    	
    def login(self, device_id, device_sign, password, userId):
    	url = "http://route.sandboxol.com/user/api/v1/app/login"
    	headers = {"userId": self.user_id, "Access-Token": self.access_token, "User-Agent": "okhttp/3.12.1", "bmg-sign": device_sign, "bmg-device-id": device_id}
    	
    	json = {"password": password, "uid": userId}
    	response = requests.post(url, headers=headers, json=json)
    	return self._handle_response(response)
    	
    def change_name(self, new_name):
    	url = "http://modsgs.sandboxol.com/user/api/v3/user/nickName"
    	params = {"newName": new_name, "oldName": "darkk.py"}
    	response = requests.put(url, headers=self.headers, params=params)
    	return self._handle_response(response)
    	
    def change_details(self, new_details):
    	url = "http://modsgs.sandboxol.com/user/api/v1/user/info"
    	json = {"details": new_details}
    	response = requests.put(url, headers=self.headers, json=json)
    	return self._handle_response(response)
    	
    def change_pfp(self, pfp_url):
    	url = "http://modsgs.sandboxol.com/user/api/v1/user/info"
    	json = {"picUrl": pfp_url}
    	response = requests.put(url, json=json, headers=self.headers)
    	return self._handle_response(response)
    
    def modify_password(self, oldPassword, newPassword):
    	url = "http://modsgs.sandboxol.com/user/api/v1/user/password/modify"
    	json = {"confirmPassword": "", "newPassword": newPassword, "oldPassword": oldPassword}
    	response = requests.post(url, json=json, headers=self.headers)
    	return self._handle_response(response)
    	
    def bind_email(self, email, verifyCode):
    	url = "http://modsgs.sandboxol.com/user/api/v1/users/bind/email"
    	json = {"email": email, "verifyCode": verifyCode}
    	response = requests.post(url, json=json, headers=self.headers)
    	return self._handle_response(response)
    	
    def unbind_email(self, verifyCode, email):
    	url = f"http://modsgs.sandboxol.com/user/api/v2/users/{self.user_id}/emails"
    	params = {"email": email, "verifyCode": verifyCode}
    	response = requests.delete(url, params=params, headers=self.headers)
    	return self._handle_response(response)
    	
    	
    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else: #i am programming in terminal right now, this if-else statement might be useless, but my terminal doesn't gives me indentations so its hard to fix it. im sorry
            return response.json() 
