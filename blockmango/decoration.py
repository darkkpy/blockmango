from .http import HTTPMixin


BASE_URL_DECORATION = "http://modsgs.sandboxol.com/decoration/api/v1"
BASE_URL_SHOP = "http://modsgs.sandboxol.com/shop/api/v1"
BASE_URL_USER = "http://modsgs.sandboxol.com/user/api/v1"


class Decoration(HTTPMixin):
  __slots__ = ("headers",)

  def __init__(self, user_id, access_token):
    self.headers = { "userId": user_id, "Access-Token": access_token, "User-Agent": "okhttp/3.12.1" }

  def skins(self, uid):
    endpoint = f"{BASE_URL_DECORATION}/new/decorations/users/{uid}/classify/all"
    params = { "engineVersion": "10105", "os": "android", "showVip": 1 }
    return self._get(endpoint, headers=self.headers, params=params)

  def current_price(self, skin_id, is_suit):
    endpoint = f"{BASE_URL_DECORATION}/decoration/current/price"
    payload = [{ "id": skin_id, "isSuit": is_suit }]
    return self._post(endpoint, headers=self.headers, json_data=payload)

  def buy(self, diamond, cloth_voucher, paytype):
    endpoint = f"{BASE_URL_SHOP}/new/shop/decorations/buy"
    params = { "diamond": diamond, "gold": 0, "clothVoucher": cloth_voucher, "payType": paytype }
    return self._post(endpoint, headers=self.headers, params=params)

  def shop_info(self):
    return self._get(f"{BASE_URL_USER}/user/shop/info", headers=self.headers)

  def equip(self, skin_id):
    endpoint = f"{BASE_URL_DECORATION}/decorations/using/new"
    params = { "ids": skin_id }
    return self._post(endpoint, headers=self.headers, params=params)
