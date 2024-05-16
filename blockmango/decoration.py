import requests
from constants import BASE_URL_DECORATION, BASE_URL_SHOP, BASE_URL_USER, HEADERS_TEMPLATE

class Decoration:
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

    def see_skins(self, uid):
        endpoint = f"/new/decorations/users/{uid}/classify/all"
        params = {"engineVersion": "10105", "os": "android", "showVip": 1}
        return self._get(BASE_URL_DECORATION, endpoint, params)

    def current_price(self, skin_id, is_suit):
        endpoint = "/decoration/current/price"
        payload = [{"id": skin_id, "isSuit": is_suit}]
        return self._post(BASE_URL_DECORATION, endpoint, json_data=payload)

    def buy_skin(self, diamond, cloth_voucher, paytype):
        endpoint = "/new/shop/decorations/buy"
        params = {"diamond": diamond, "gold": 0, "clothVoucher": cloth_voucher, "payType": paytype}
        return self._post(BASE_URL_SHOP, endpoint, params=params)

    def shop_info(self):
        endpoint = "/user/shop/info"
        return self._get(BASE_URL_USER, endpoint)

    def equip_skin(self, skin_id):
        endpoint = "/decorations/using/new"
        params = {"ids": skin_id}
        return self._post(BASE_URL_DECORATION, endpoint, params=params)
