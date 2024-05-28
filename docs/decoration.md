# 🎨 Decoration Class Documentation

This documentation provides details on the `Decoration` class which is part of the `blockmango` module. The class interacts with a decoration management API, allowing various operations such as fetching skins, checking current prices, buying decorations, and more.

## 📦 Installation

To install the `blockmango` module, use the following command:

```sh
pip install blockmango
```

## 🚀 Usage

To use the `Decoration` class, import it from the `blockmango` module:

```python
import blockmango
from blockmango import Decoration
```

### 🔑 Initialization

```python
decoration = Decoration(user_id="your_user_id", access_token="your_access_token")
```

## 📚 Methods

### 🖼️ skins
Fetches the skins available for a user.

```python
decoration.skins(uid="user_id")
```

### 💰 current_price
Gets the current price of a skin.

```python
decoration.current_price(skin_id="skin_id", is_suit=True)
```

### 🛒 buy
Buys a decoration.

```python
decoration.buy(diamond=100, cloth_voucher=5, paytype="pay_type")
```

### 🏪 shop_info
Gets the shop information of the user.

```python
decoration.shop_info()
```

### 🎭 equip
Equips a decoration.

```python
decoration.equip(skin_id="skin_id")
```

## 🛠️ Example

```python
import blockmango
from blockmango import Decoration

# Initialize Decoration instance
decoration = Decoration(user_id="your_user_id", access_token="your_access_token")

# Fetch skins for a user
skins = decoration.skins(uid="user_id")
print(skins)

# Get current price of a skin
price = decoration.current_price(skin_id="skin_id", is_suit=True)
print(price)

# Buy a decoration
buy_response = decoration.buy(diamond=100, cloth_voucher=5, paytype="diamond")
print(buy_response)

# Get shop information
shop_info = decoration.shop_info()
print(shop_info)

# Equip a decoration
equip_response = decoration.equip(skin_id="skin_id")
print(equip_response)
```

This `README.md` provides an overview of the `Decoration` class methods and usage examples. For more detailed usage, refer to the method definitions and parameters listed above.
