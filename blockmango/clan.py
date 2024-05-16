import requests
import json

class Clan:
    def __init__(self, user_id, access_token):
        self.user_id = user_id
        self.access_token = access_token
        self.headers = {
            "userId": user_id,
            "Access-Token": access_token,
            "User-Agent": "okhttp/3.12.1"
        }

    def userclan(self):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/base"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def joinclan(self, clan_id):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member"
        json_data = {"clanId": clan_id, "msg": ""}
        response = requests.post(url, headers=self.headers, json=json_data)
        return self._handle_response(response)

    def leaveclan(self, clan_id):
        url = f"http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member?clanId={clan_id}"
        response = requests.delete(url, headers=self.headers)
        return self._handle_response(response)

    def searchclan(self, clan_name, page_no=0, page_size=20):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/blurry/info"
        params = {"clanName": clan_name, "pageNo": page_no, "pageSize": page_size}
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def infoclanId(self, clan_id):
        url = "http://modsgs.sandboxol.com/clan/api/v2/clan/tribe"
        params = {"clanId": clan_id}
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def inviteclan(self, friend_ids, message=""):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member/invite"
        json_data = {"friendIds": friend_ids, "msg": message}
        response = requests.post(url, headers=self.headers, json=json_data)
        return self._handle_response(response)

    def agreementuser(self, other_id):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member/agreement"
        params = {"otherId": other_id}
        response = requests.put(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def rejectuser(self, other_id):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member/rejection"
        params = {"otherId": other_id}
        response = requests.put(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def mutemember(self, member_id, minutes):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/mute/member"
        params = {"memberId": member_id, "minute": minutes}
        response = requests.post(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def unmutemember(self, member_id):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/mute/member"
        params = {"memberId": member_id}
        response = requests.delete(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def muteall(self):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/mute"
        params = {"muteStatus": 1}
        response = requests.put(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def unmuteall(self):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/mute"
        params = {"muteStatus": 0}
        response = requests.put(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def removemember(self, member_ids):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member/remove/batch"
        json_data = member_ids
        response = requests.delete(url, headers=self.headers, json=json_data)
        return self._handle_response(response)

    def editclan(self, clan_id, currency=0, details="", head_pic="", name="", tags=None):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe"
        json_data = {
            "clanId": clan_id,
            "currency": currency,
            "details": details,
            "headPic": head_pic,
            "name": name,
            "tags": tags if tags else []
        }
        response = requests.put(url, headers=self.headers, json=json_data)
        return self._handle_response(response)

    def add_remove_elders(self, type_, elder_ids):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/members"
        params = {"type": type_, "otherIds": elder_ids}
        response = requests.put(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def authentication(self, type):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/free/verification"
        params = {"freeVerify": 1 if type == "on" else 0}
        response = requests.put(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def clanbuy(self, decoration_id):
        url = f"http://modsgs.sandboxol.com/clan/api/v1/clan/decorations/purchase?decorationId={decoration_id}"
        response = requests.put(url, headers=self.headers)
        return self._handle_response(response)

    def teamtaskaccept(self, task_id):
        url = f"http://modsgs.sandboxol.com/clan/api/v1/clan/tasks/accept?id={task_id}&type=0"
        response = requests.put(url, headers=self.headers)
        return self._handle_response(response)

    def selftaskrefresh(self):
        url = "http://modsgs.sandboxol.com/clan/api/v3/clan/personal/tasks?type=1"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def selftaskaccept(self, task_id):
        url = f"http://modsgs.sandboxol.com/clan/api/v1/clan/tasks/accept?id={task_id}&type=1"
        response = requests.put(url, headers=self.headers)
        return self._handle_response(response)

    def teamtaskclaim(self, task_id):
        url = f"http://modsgs.sandboxol.com/clan/api/v1/clan/tasks?id={task_id}&type=0"
        response = requests.put(url, headers=self.headers)
        return self._handle_response(response)

    def selftaskclaim(self, task_id):
        url = f"http://modsgs.sandboxol.com/clan/api/v1/clan/tasks?id={task_id}&type=1"
        response = requests.put(url, headers=self.headers)
        return self._handle_response(response)

    def clannotice(self, content):
        url = "http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/bulletin"
        json_data = {"content": content}
        response = requests.post(url, headers=self.headers, json=json_data)
        return self._handle_response(response)

    def transferchief(self, new_chief_id):
        url = f"http://modsgs.sandboxol.com/clan/api/v1/clan/tribe/member?otherId={new_chief_id}&type=3"
        response = requests.put(url, headers=self.headers)
        return self._handle_response(response)

    def createclan(self, clan_id=0, currency=2, details="", head_pic="", name="", tags=None):
        url = "http://modsgs.sandboxol.com/clan/api/v3/clan/tribe"
        json_data = {
            "clanId": clan_id,
            "currency": currency,
            "details": details,
            "headPic": head_pic,
            "name": name,
            "tags": tags if tags else []
        }
        response = requests.post(url, headers=self.headers, json=json_data)
        return self._handle_response(response)

    def dissolveclan(self, clan_id):
        url = f"http://modsgs.sandboxol.com/clan/api/v1/clan/tribe?clanId={clan_id}"
        response = requests.delete(url, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
