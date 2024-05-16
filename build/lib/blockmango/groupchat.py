import requests
import json

class Group:
    def __init__(self, user_id, access_token):
        self.user_id = user_id
        self.access_token = access_token
        self.headers = {"userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1"}

    def create_group(self, member_ids):
        url = "http://modsgs.sandboxol.com/msg/api/v2/msg/group/chat"
        response = requests.post(url, headers=self.headers, json={"cost": 0, "currency": 1, "memberIds": member_ids, "userId": self.user_id})
        return self._handle_response(response)
        
    def allow_invite(self, group_id, group_name, invite_status):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/modify"
        response = requests.put(url, headers=self.headers, json={"groupId": group_id, "groupName": group_name, "inviteStatus": invite_status, "inviterId": self.user_id})
        return self._handle_response(response)
        
    def edit_group(self, group_id, group_name, group_notice, invite_status, notice_pics):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/modify"
        response = requests.put(url, headers=self.headers, json={"groupId": group_id, "groupName": group_name, "groupNotice": group_notice, "inviteStatus": invite_status, "inviterId": self.user_id, "noticePic": notice_pics})
        return self._handle_response(response)
        
    def group_admin(self, group_id, member_id, operation_type):    
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/member"
        response = requests.put(url, headers=self.headers, json={"groupId": group_id, "inviterId": self.user_id, "memberIds": [member_id], "operationType": operation_type})
        return self._handle_response(response)
        
    def group_mute(self, group_id, member_id, minutes):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/forbidden/member"
        response = requests.post(url, headers=self.headers, json={"groupId": group_id, "memberId": member_id, "minutes": minutes})
        return self._handle_response(response)
    
    def group_invite(self, group_id, member_ids):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/invite"
        response = requests.post(url, headers=self.headers, json={"groupId": group_id, "memberIds": member_ids})
        return self._handle_response(response)
        
    def group_kick(self, group_id, group_name, member_ids):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/kickOut"
        response = requests.put(url, headers=self.headers, json={"groupId": group_id, "groupName": group_name, "inviterId": self.user_id, "memberIds": member_ids})
        return self._handle_response(response)

    def group_approve_disapprove(self, group_id, operate_id, j_type):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/agreement"
        response = requests.put(url, headers=self.headers, json={"groupId": group_id, "operateId": operate_id, "type": j_type, "userId": self.user_id})
        return self._handle_response(response)
        
    def group_quit(self, group_id, group_name):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/quit"
        response = requests.put(url, headers=self.headers, params={"groupId": group_id, "groupName": group_name})
        return self._handle_response(response)
        
    def group_apply(self, group_id, msg):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/apply"
        response = requests.post(url, headers=self.headers, params={"groupId": group_id, "msg": msg})
        return self._handle_response(response)
        
    def group_owner(self, group_id, new_owner):
        url = "http://modsgs.sandboxol.com/msg/api/v1/msg/group/chat/transfer"
        response = requests.put(url, headers=self.headers, json={"groupId": group_id, "inviterId": self.user_id, "userId": new_owner})
        return self._handle_response(response)

    def _handle_response(self, response):
        return response.json() 
