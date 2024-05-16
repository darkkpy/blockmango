import requests
from constants import BASE_URL, BASE_URL_V2, BASE_URL_V3, HEADERS_TEMPLATE

class Clan:
    def __init__(self, user_id, access_token):
        self.headers = {
            **HEADERS_TEMPLATE,
            "userId": user_id,
            "Access-Token": access_token
        }

    def _handle_response(self, response):
        return response.json()

    def _get(self, endpoint, params=None):
        response = requests.get(f"{BASE_URL}{endpoint}", headers=self.headers, params=params)
        return self._handle_response(response)

    def _post(self, endpoint, json_data=None, params=None):
        response = requests.post(f"{BASE_URL}{endpoint}", headers=self.headers, json=json_data, params=params)
        return self._handle_response(response)

    def _put(self, endpoint, json_data=None, params=None):
        response = requests.put(f"{BASE_URL}{endpoint}", headers=self.headers, json=json_data, params=params)
        return self._handle_response(response)

    def _delete(self, endpoint, json_data=None, params=None):
        response = requests.delete(f"{BASE_URL}{endpoint}", headers=self.headers, json=json_data, params=params)
        return self._handle_response(response)

    def userclan(self):
        return self._get("/tribe/base")

    def joinclan(self, clan_id):
        return self._post("/tribe/member", json_data={"clanId": clan_id, "msg": ""})

    def leaveclan(self, clan_id):
        return self._delete("/tribe/member", params={"clanId": clan_id})

    def searchclan(self, clan_name, page_no=0, page_size=20):
        params = {"clanName": clan_name, "pageNo": page_no, "pageSize": page_size}
        return self._get("/tribe/blurry/info", params=params)

    def infoclanId(self, clan_id):
        response = requests.get(f"{BASE_URL_V2}/tribe", headers=self.headers, params={"clanId": clan_id})
        return self._handle_response(response)

    def inviteclan(self, friend_ids, message=""):
        json_data = {"friendIds": friend_ids, "msg": message}
        return self._post("/tribe/member/invite", json_data=json_data)

    def agreementuser(self, other_id):
        return self._put("/tribe/member/agreement", params={"otherId": other_id})

    def rejectuser(self, other_id):
        return self._put("/tribe/member/rejection", params={"otherId": other_id})

    def mutemember(self, member_id, minutes):
        params = {"memberId": member_id, "minute": minutes}
        return self._post("/tribe/mute/member", params=params)

    def unmutemember(self, member_id):
        return self._delete("/tribe/mute/member", params={"memberId": member_id})

    def muteall(self):
        return self._put("/tribe/mute", params={"muteStatus": 1})

    def unmuteall(self):
        return self._put("/tribe/mute", params={"muteStatus": 0})

    def removemember(self, member_ids):
        return self._delete("/tribe/member/remove/batch", json_data=member_ids)

    def editclan(self, clan_id, currency=0, details="", head_pic="", name="", tags=None):
        json_data = {
            "clanId": clan_id,
            "currency": currency,
            "details": details,
            "headPic": head_pic,
            "name": name,
            "tags": tags or []
        }
        return self._put("/tribe", json_data=json_data)

    def add_remove_elders(self, type_, elder_ids):
        params = {"type": type_, "otherIds": elder_ids}
        return self._put("/tribe/members", params=params)

    def authentication(self, type_):
        params = {"freeVerify": 1 if type_ == "on" else 0}
        return self._put("/free/verification", params=params)

    def clanbuy(self, decoration_id):
        url = f"{BASE_URL}/decorations/purchase"
        response = requests.put(url, headers=self.headers, params={"decorationId": decoration_id})
        return self._handle_response(response)

    def teamtaskaccept(self, task_id):
        url = f"{BASE_URL}/tasks/accept"
        response = requests.put(url, headers=self.headers, params={"id": task_id, "type": 0})
        return self._handle_response(response)

    def selftaskrefresh(self):
        response = requests.get(f"{BASE_URL_V3}/personal/tasks", headers=self.headers, params={"type": 1})
        return self._handle_response(response)

    def selftaskaccept(self, task_id):
        url = f"{BASE_URL}/tasks/accept"
        response = requests.put(url, headers=self.headers, params={"id": task_id, "type": 1})
        return self._handle_response(response)

    def teamtaskclaim(self, task_id):
        url = f"{BASE_URL}/tasks"
        response = requests.put(url, headers=self.headers, params={"id": task_id, "type": 0})
        return self._handle_response(response)

    def selftaskclaim(self, task_id):
        url = f"{BASE_URL}/tasks"
        response = requests.put(url, headers=self.headers, params={"id": task_id, "type": 1})
        return self._handle_response(response)

    def clannotice(self, content):
        json_data = {"content": content}
        return self._post("/tribe/bulletin", json_data=json_data)

    def transferchief(self, new_chief_id):
        url = f"{BASE_URL}/tribe/member"
        response = requests.put(url, headers=self.headers, params={"otherId": new_chief_id, "type": 3})
        return self._handle_response(response)

    def createclan(self, clan_id=0, currency=2, details="", head_pic="", name="", tags=None):
        json_data = {
            "clanId": clan_id,
            "currency": currency,
            "details": details,
            "headPic": head_pic,
            "name": name,
            "tags": tags or []
        }
        response = requests.post(f"{BASE_URL_V3}/tribe", headers=self.headers, json=json_data)
        return self._handle_response(response)

    def dissolveclan(self, clan_id):
        url = f"{BASE_URL}/tribe"
        response = requests.delete(url, headers=self.headers, params={"clanId": clan_id})
        return self._handle_response(response)
