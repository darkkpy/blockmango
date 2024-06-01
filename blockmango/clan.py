# clan.py
from .http import HTTPMixin
from .config import BASE_URL_CLAN, BASE_URL_CLAN_V2, BASE_URL_CLAN_V3

class Clan(HTTPMixin):
    __slots__ = ("headers",)
    base_url_clan = BASE_URL_CLAN
    base_url_clan_v2 = BASE_URL_CLAN_V2
    base_url_clan_v3 = BASE_URL_CLAN_V3

    def __init__(self, user_id, access_token):
        self.headers = {"userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1", "language": "en_US"}

    def user_clan(self):
        return self._get(f"{self.base_url_clan}/tribe/base", headers=self.headers)

    def join(self, clan_id):
        return self._post(f"{self.base_url_clan}/tribe/member", headers=self.headers, json={"clanId": clan_id, "msg": ""})

    def leave(self, clan_id):
        return self._delete(f"{self.base_url_clan}/tribe/member", headers=self.headers, params={"clanId": clan_id})

    def search(self, clan_name, page_no=0, page_size=20):
        return self._get(f"{self.base_url_clan}/tribe/blurry/info", headers=self.headers, params={"clanName": clan_name, "pageNo": page_no, "pageSize": page_size})

    def info(self, clan_id):
        return self._get(f"{self.base_url_clan_v2}/tribe", headers=self.headers, params={"clanId": clan_id})

    def invite(self, friend_ids, message=""):
        return self._post(f"{self.base_url_clan}/tribe/member/invite", headers=self.headers, json={"friendIds": friend_ids, "msg": message})

    def agreement_user(self, other_id):
        return self._put(f"{self.base_url_clan}/tribe/member/agreement", headers=self.headers, params={"otherId": other_id})

    def reject_user(self, other_id):
        return self._put(f"{self.base_url_clan}/tribe/member/rejection", headers=self.headers, params={"otherId": other_id})

    def mute_member(self, member_id, minutes):
        return self._post(f"{self.base_url_clan}/tribe/mute/member", headers=self.headers, params={"memberId": member_id, "minute": minutes})

    def unmute_member(self, member_id):
        return self._delete(f"{self.base_url_clan}/tribe/mute/member", headers=self.headers, params={"memberId": member_id})

    def mute_all(self):
        return self._put(f"{self.base_url_clan}/tribe/mute", headers=self.headers, params={"muteStatus": 1})

    def unmute_all(self):
        return self._put(f"{self.base_url_clan}/tribe/mute", headers=self.headers, params={"muteStatus": 0})

    def remove_member(self, member_ids):
        return self._delete(f"{self.base_url_clan}/tribe/member/remove/batch", headers=self.headers, json=member_ids)

    def edit(self, clan_id, currency=0, details="", head_pic="", name="", tags=None):
        return self._put(f"{self.base_url_clan}/tribe", headers=self.headers, json={"clanId": clan_id, "currency": currency, "details": details, "headPic": head_pic, "name": name, "tags": tags or []})

    def edit_elders(self, type_, elder_ids):
        return self._put(f"{self.base_url_clan}/tribe/members", headers=self.headers, params={"type": type_, "otherIds": elder_ids})

    def authentication(self, type_):
        return self._put(f"{self.base_url_clan}/free/verification", headers=self.headers, params={"freeVerify": 1 if type_ == "on" else 0})

    def buy_decoration(self, decoration_id):
        return self._put(f"{self.base_url_clan}/decorations/purchase", headers=self.headers, params={"decorationId": decoration_id})

    def task_accept(self, task_id, is_team_task):
        return self._put(f"{self.base_url_clan}/tasks/accept", headers=self.headers, params={"id": task_id, "type": 0 if is_team_task else 1})

    def self_task_refresh(self):
        return self._get(f"{self.base_url_clan_v3}/personal/tasks", headers=self.headers, params={"type": 1})

    def task_claim(self, task_id, is_team_task):
        return self._put(f"{self.base_url_clan}/tasks", headers=self.headers, params={"id": task_id, "type": 0 if is_team_task else 1})

    def notice(self, content):
        return self._post(f"{self.base_url_clan}/tribe/bulletin", headers=self.headers, json={"content": content})

    def transfer_chief(self, new_chief_id):
        return self._put(f"{self.base_url_clan}/tribe/member", headers=self.headers, params={"otherId": new_chief_id, "type": 3})

    def create(self, clan_id=0, currency=2, details="", head_pic="", name="", tags=None):
        return self._post(f"{self.base_url_clan_v3}/tribe", headers=self.headers, json={"clanId": clan_id, "currency": currency, "details": details, "headPic": head_pic, "name": name, "tags": tags or []})

    def dissolve(self, clan_id):
        return self._delete(f"{self.base_url_clan}/tribe", headers=self.headers, params={"clanId": clan_id})
