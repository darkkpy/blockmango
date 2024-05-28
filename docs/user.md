# 👤 User Class Documentation

This documentation provides details on the `User` class which is part of the `blockmango` module. The class interacts with a user management API, allowing various operations such as fetching user info, changing user details, modifying passwords, and more.

## 📦 Installation

To install the `blockmango` module, use the following command:

```sh
pip install blockmango
```

## 🚀 Usage

To use the `User` class, import it from the `blockmango` module:

```python
import blockmango
from blockmango import User
```

### 🔑 Initialization

```python
user = User(user_id="your_user_id", access_token="your_access_token")
```

## 📚 Methods

### ℹ️ get_user_info
Gets detailed information about the user.

```python
user.get_user_info()
```

### 🎂 set_birthday
Sets the user's birthday.

```python
user.set_birthday(birthday="yyyy-mm-dd")
```

### 🔒 login
Logs in the user.

```python
user.login(device_id="device_id", device_sign="device_signature", password="password", userId="user_id")
```

### ✏️ change_name
Changes the user's name.

```python
user.change_name(new_name="New Name", old_name="Old Name")
```

### 📝 change_details
Changes the user's details.

```python
user.change_details(new_details="New details")
```

### 🖼️ change_pfp
Changes the user's profile picture.

```python
user.change_pfp(pfp_url="image_url")
```

### 🔑 modify_password
Modifies the user's password.

```python
user.modify_password(old_password="old_password", new_password="new_password")
```

### 📧 bind_email
Binds an email to the user's account.

```python
user.bind_email(email="email_address", verify_code="verification_code")
```

### 📧 unbind_email
Unbinds an email from the user's account.

```python
user.unbind_email(verify_code="verification_code", email="email_address")
```

This `README.md` provides an overview of the `User` class methods and usage examples. For more detailed usage, refer to the method definitions and parameters listed above.
