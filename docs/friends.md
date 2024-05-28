# 👫 Friends Class Documentation

This documentation provides details on the `Friends` class which is part of the `blockmango` module. The class interacts with a friend management API, allowing various operations such as adding friends, deleting friends, managing friend requests, and more.

## 📦 Installation

To install the `blockmango` module, use the following command:

```sh
pip install blockmango
```

## 🚀 Usage

To use the `Friends` class, import it from the `blockmango` module:

```python
import blockmango
from blockmango import Friends
```

### 🔑 Initialization

```python
friends = Friends(user_id="your_user_id", access_token="your_access_token")
```

## 📚 Methods

### 🚫 delete_friend
Deletes a friend from your friend list.

```python
friends.delete_friend(friend_id="friend_id")
```

### 🤝 request
Sends a friend request to another user.

```python
friends.request(friend_id="friend_id", msg="Let's be friends!")
```

### 🌟 popularity
Gets the popularity of a friend.

```python
friends.popularity(friend_id="friend_id")
```

### ℹ️ info
Gets detailed information about a friend.

```python
friends.info(friend_id="friend_id")
```

### 🎨 decoration
Gets decorations used by a friend.

```python
friends.decoration(friend_id="friend_id")
```

### ➕ add_popularity
Adds popularity to a friend.

```python
friends.add_popularity(friend_id="friend_id")
```

### 📜 friend_list
Gets the list of friends.

```python
friends.friend_list()
```

### 📛 nickname
Sets a nickname for a friend.

```python
friends.nickname(friend_id="friend_id", alias="Nickname")
```

### ✅ friend_approve
Approves a friend request.

```python
friends.friend_approve(friend_id="friend_id")
```

### 🚷 friend_blacklist
Adds a friend to the blacklist.

```python
friends.friend_blacklist(friend_id="friend_id")
```

### 🙅 reject_all
Rejects all friend requests.

```python
friends.reject_all()
```

### ✅ approve_all
Approves all pending friend requests.

```python
friends.approve_all()
```

### ❌ friend_reject
Rejects a friend request.

```python
friends.friend_reject(friend_id="friend_id")
```

This `README.md` provides an overview of the `Friends` class methods and usage examples. For more detailed usage, refer to the method definitions and parameters listed above.
