import requests
from constants import BASE_URL_GROUP, BASE_URL_GROUP_V2, HEADERS_TEMPLATE

class Group:
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

    def create_group(self, member_ids):
        endpoint = "/msg/group/chat"
        json_data = {"cost": 0, "currency": 1, "memberIds": member_ids, "userId": self.headers["userId"]}
        return self._post(BASE_URL_GROUP_V2, endpoint, json_data=json_data)

    def allow_invite(self, group_id, group_name, invite_status):
        endpoint = "/msg/group/chat/modify"
        json_data = {"groupId": group_id, "groupName": group_name, "inviteStatus": invite_status, "inviterId": self.headers["userId"]}
        return self._put(BASE_URL_GROUP, endpoint, json_data=json_data)

    def edit_group(self, group_id, group_name, group_notice, invite_status, notice_pics):
        endpoint = "/msg/group/chat/modify"
        json_data = {"groupId": group_id, "groupName": group_name, "groupNotice": group_notice, "inviteStatus": invite_status, "inviterId": self.headers["userId"], "noticePic": notice_pics}
        return self._put(BASE_URL_GROUP, endpoint, json_data=json_data)

    def group_admin(self, group_id, member_id, operation_type):
        endpoint = "/msg/group/chat/member"
        json_data = {"groupId": group_id, "inviterId": self.headers["userId"], "memberIds": [member_id], "operationType": operation_type}
        return self._put(BASE_URL_GROUP, endpoint, json_data=json_data)

    def group_mute(self, group_id, member_id, minutes):
        endpoint = "/msg/group/chat/forbidden/member"
        json_data = {"groupId": group_id, "memberId": member_id, "minutes": minutes}
        return self._post(BASE_URL_GROUP, endpoint, json_data=json_data)

    def group_invite(self, group_id, member_ids):
        endpoint = "/msg/group/chat/invite"
        json_data = {"groupId": group_id, "memberIds": member_ids}
        return self._post(BASE_URL_GROUP, endpoint, json_data=json_data)

    def group_kick(self, group_id, group_name, member_ids):
        endpoint = "/msg/group/chat/kickOut"
        json_data = {"groupId": group_id, "groupName": group_name, "inviterId": self.headers["userId"], "memberIds": member_ids}
        return self._put(BASE_URL_GROUP, endpoint, json_data=json_data)

    def group_approve_disapprove(self, group_id, operate_id, j_type):
        endpoint = "/msg/group/chat/agreement"
        json_data = {"groupId": group_id, "operateId": operate_id, "type": j_type, "userId": self.headers["userId"]}
        return self._put(BASE_URL_GROUP, endpoint, json_data=json_data)

    def group_quit(self, group_id, group_name):
        endpoint = "/msg/group/chat/quit"
        params = {"groupId": group_id, "groupName": group_name}
        return self._put(BASE_URL_GROUP, endpoint, params=params)

    def group_apply(self, group_id, msg):
        endpoint = "/msg/group/chat/apply"
        params = {"groupId": group_id, "msg": msg}
        return self._post(BASE_URL_GROUP, endpoint, params=params)

    def group_owner(self, group_id, new_owner):
        endpoint = "/msg/group/chat/transfer"
        json_data = {"groupId": group_id, "inviterId": self.headers["userId"], "userId": new_owner}
        return self._put(BASE_URL_GROUP, endpoint, json_data=json_data)
