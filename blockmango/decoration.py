# decoration.py
from .http import HTTPMixin
from .config import BASE_URL_DECORATION, BASE_URL_SHOP

class Decoration(HTTPMixin):
    __slots__ = ("headers",)
    base_url = BASE_URL_DECORATION

    def __init__(self, user_id, access_token):
        self.headers = {"userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1", "language": "en_US"}

    def skins(self, uid):
        params = {"engineVersion": "10105", "os": "android", "showVip": 1}
        return self._get(f"{self.base_url}/new/decorations/users/{uid}/classify/all", headers=self.headers, params=params)

    def current_price(self, skin_id, is_suit):
        payload = [{"id": skin_id, "isSuit": is_suit}]
        return self._post(f"{self.base_url}/decoration/current/price", headers=self.headers, json=payload)

    def buy(self, diamond, cloth_voucher, paytype):
        params = {"diamond": diamond, "gold": 0, "clothVoucher": cloth_voucher, "payType": paytype}
        return self._post(f"{BASE_URL_SHOP}/new/shop/decorations/buy", headers=self.headers, params=params)

    def shop_info(self):
        return self._get(f"{BASE_URL_USER}/user/shop/info", headers=self.headers)

    def equip(self, skin_id):
        params = {"ids": skin_id}
        return self._post(f"{BASE_URL_DECORATION}/decorations/using/new", headers=self.headers, params=params)
