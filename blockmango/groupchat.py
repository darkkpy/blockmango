from .http import HTTPMixin


BASE_URL_GROUP = "http://modsgs.sandboxol.com/msg/api/v1"
BASE_URL_GROUP_V2 = "http://modsgs.sandboxol.com/msg/api/v2"


class Group(HTTPMixin):
  __slots__ = ("headers",)
  
  def __init__(self, user_id, access_token):
    self.headers = { "userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1" }

  def create(self, member_ids):
    endpoint = f"{BASE_URL_GROUP_V2}/msg/group/chat"
    json_data = { "cost": 0, "currency": 1, "memberIds": member_ids, "userId": self.headers["userId"] }
    return self._post(endpoint, headers=self.headers, json_data=json_data)

  def allow_invite(self, group_id, group_name, invite_status):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/modify"
    json_data = { "groupId": group_id, "groupName": group_name, "inviteStatus": invite_status, "inviterId": self.headers["userId"] }
    return self._put(endpoint, headers=self.headers, json_data=json_data)

  def edit(self, group_id, group_name, group_notice, invite_status, notice_pics):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/modify"
    json_data = { "groupId": group_id, "groupName": group_name, "groupNotice": group_notice, "inviteStatus": invite_status, "inviterId": self.headers["userId"], "noticePic": notice_pics }
    return self._put(endpoint, headers=self.headers, json_data=json_data)

  def admin(self, group_id, member_id, operation_type):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/member"
    json_data = { "groupId": group_id, "inviterId": self.headers["userId"], "memberIds": [member_id], "operationType": operation_type }
    return self._put(endpoint, headers=self.headers, json_data=json_data)

  def mute(self, group_id, member_id, minutes):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/forbidden/member"
    json_data = { "groupId": group_id, "memberId": member_id, "minutes": minutes }
    return self._post(endpoint, headers=self.headers, json_data=json_data)

  def invite(self, group_id, member_ids):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/invite"
    json_data = { "groupId": group_id, "memberIds": member_ids }
    return self._post(endpoint, headers=self.headers, json_data=json_data)

  def kick(self, group_id, group_name, member_ids):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/kickOut"
    json_data = { "groupId": group_id, "groupName": group_name, "inviterId": self.headers["userId"], "memberIds": member_ids }
    return self._put(endpoint, headers=self.headers, json_data=json_data)

  def approve_or_disapprove(self, group_id, operate_id, j_type):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/agreement"
    json_data = { "groupId": group_id, "operateId": operate_id, "type": j_type, "userId": self.headers["userId"] }
    return self._put(endpoint, headers=self.headers, json_data=json_data)

  def quit(self, group_id, group_name):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/quit"
    params = { "groupId": group_id, "groupName": group_name }
    return self._put(endpoint, headers=self.headers, params=params)

  def apply(self, group_id, msg):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/apply"
    params = { "groupId": group_id, "msg": msg }
    return self._post(endpoint, headers=self.headers, params=params)

  def transfer(self, group_id, new_owner):
    endpoint = f"{BASE_URL_GROUP}/msg/group/chat/transfer"
    json_data = { "groupId": group_id, "inviterId": self.headers["userId"], "userId": new_owner }
    return self._put(endpoint, headers=self.headers, json_data=json_data)