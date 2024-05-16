import requests
import json

class Friends:
    def __init__(self, user_id, access_token):
        self.user_id = user_id
        self.access_token = access_token
        self.headers = {
            "userId": user_id,
            "Access-Token": access_token,
            "User-Agent": "okhttp/3.12.1"
        }

    def delete_friend(self, friend_id):
        url = "http://modsgs.sandboxol.com/friend/api/v1/friends"
        params = {"friendId": friend_id}
        response = requests.delete(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def friend_request(self, friend_id, msg):
        url = "http://modsgs.sandboxol.com/friend/api/v1/friends"
        payload = {"friendId": friend_id,"msg": msg, "type": 1}
        headers = self.headers.copy()
        headers["Content-Type"] = "application/json"
        response = requests.post(url, headers=headers, json=payload)
        return self._handle_response(response)
        
    def friend_popularity(self, friend_id):
   	 url = f"http://modsgs.sandboxol.com/friend/api/v1/popularity/{friend_id}"
   	 response = requests.get(url, headers=self.headers)
   	 return self._handle_response(response)
   	 
    def friend_info(self, friend_id):
    	url = f"http://modsgs.sandboxol.com/friend/api/v3/friends/{friend_id}"
    	response = requests.get(url, headers=self.headers)
    	return self._handle_response(response)
    	
    def friend_decoration(self, friend_id):
    	url = f"http://modsgs.sandboxol.com/decoration/api/v1/decorations-v2/{friend_id}/using"
    	response = requests.get(url, headers=self.headers)
    	return self._handle_response(response)
    	
    def add_popularity(self, friend_id):
    	url = "http://modsgs.sandboxol.com/friend/api/v1/popularity"
    	params = {"friendId": friend_id}
    	response = requests.post(url, headers=self.headers)
    	return self._handle_response(response)
    	
    def friend_list(self):
    	url = "http://modsgs.sandboxol.com/friend/api/v2/friends/status"
    	headers = self.headers.copy()
    	headers["language"] = "en_US"
    	response = requests.get(url, headers=headers)
    	return self._handle_response(response)
    	
    def friend_nickname(self, friend_id, alias):
    	url = "http://modsgs.sandboxol.com/friend/api/v1/friends/{friend_id}/alias"
    	params = {"alias": alias}
    	response = requests.post(url, headers=self.headers, params=params)
    	return self._handle_response(response)
    	
    def friend_approve(self, friend_id):
    	url = "http://modsgs.sandboxol.com/friend/api/v1/friends/{friend_id}/agreement"
    	response = requests.put(url, headers=self.headers)
    	return self._handle_response(response)
    	
    def friend_blacklist(self, friend_id):
    	url = "http://modsgs.sandboxol.com/friend/api/v1/friends/black"
    	params = {"friendId": friend_id}
    	response = requests.delete(url, headers=self.headers)
    	return self._handle_response(response)
    	
    def reject_all(self):
    	url = "http://modsgs.sandboxol.com/friend/api/v1/friends/requests/approve-all"
    	response = requests.post(url, headers=self.headers)
    	return self._handle_response(response)
    	
    def approve_all(self):
    	url = "http://modsgs.sandboxol.com/friend/api/v1/friends/requests/reject-all"
    	response = requests.post(url, headers=self.headers)
    	return self._handle_response(response)

    def friend_reject(self, friend_id):
    	url = "http://modsgs.sandboxol.com/friend/api/v1/friends/{friend_id}/rejection"
    	response = requests.put(url, headers=self.headers)
    	return self._handle_response(response)
    	
    def _handle_response(self, response):
        return response.json()
