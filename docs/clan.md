# 🏰 Clan Class Documentation

This documentation provides details on the `Clan` class which is part of the `blockmango` module. The class interacts with a clan management API, allowing various operations such as joining a clan, inviting members, muting members, and more.

## 📦 Installation

To install the `blockmango` module, use the following command:

```sh
pip install blockmango
```

## 🚀 Usage

To use the `Clan` class, import it from the `blockmango` module:

```python
import blockmango
from blockmango import Clan
```

### 🔑 Initialization

```python
clan = Clan(user_id="your_user_id", access_token="your_access_token")
```

## 📚 Methods

### 📜 user_clan
Fetches the user's clan information.

```python
clan.user_clan()
```

### ➕ join
Joins a clan by ID.

```python
clan.join(clan_id="clan_id")
```

### ➖ leave
Leaves a clan by ID.

```python
clan.leave(clan_id="clan_id")
```

### 🔍 search
Searches for clans by name.

```python
clan.search(clan_name="clan_name", page_no=0, page_size=20)
```

### ℹ️ info
Gets information about a specific clan by ID.

```python
clan.info(clan_id="clan_id")
```

### 📩 invite
Invites friends to the clan.

```python
clan.invite(friend_ids=["friend_id1", "friend_id2"], message="Join my clan!")
```

### ✅ agreement_user
Agrees to a user's clan request.

```python
clan.agreement_user(other_id="user_id")
```

### ❌ reject_user
Rejects a user's clan request.

```python
clan.reject_user(other_id="user_id")
```

### 🔇 mute_member
Mutes a clan member for a specified duration in minutes.

```python
clan.mute_member(member_id="member_id", minutes=30)
```

### 🔊 unmute_member
Unmutes a clan member.

```python
clan.unmute_member(member_id="member_id")
```

### 🔇 mute_all
Mutes all members in the clan.

```python
clan.mute_all()
```

### 🔊 unmute_all
Unmutes all members in the clan.

```python
clan.unmute_all()
```

### 🗑️ remove_member
Removes members from the clan.

```python
clan.remove_member(member_ids=["member_id1", "member_id2"])
```

### 🛠️ edit
Edits the clan details.

```python
clan.edit(clan_id="clan_id", currency=0, details="New details", head_pic="new_pic_url", name="New Name", tags=["tag1", "tag2"])
```

### 🧓 edit_elders
Edits the clan elders.

```python
clan.edit_elders(type_="elder_type", elder_ids=["elder_id1", "elder_id2"])
```

### 🔐 authentication
Sets clan authentication.

```python
clan.authentication(type_="on")  # or "off"
```

### 🛍️ buy_decoration
Buys a clan decoration.

```python
clan.buy_decoration(decoration_id="decoration_id")
```

### ✅ task_accept
Accepts a clan task.

```python
clan.task_accept(task_id="task_id", is_team_task=True)
```

### 🔄 self_task_refresh
Refreshes personal clan tasks.

```python
clan.self_task_refresh()
```

### 🎉 task_claim
Claims a completed clan task.

```python
clan.task_claim(task_id="task_id", is_team_task=True)
```

### 📢 notice
Posts a clan notice.

```python
clan.notice(content="Clan meeting at 8 PM!")
```

### 👑 transfer_chief
Transfers clan chief role to another member.

```python
clan.transfer_chief(new_chief_id="new_chief_id")
```

### 🏗️ create
Creates a new clan.

```python
clan.create(clan_id=0, currency=2, details="Clan details", head_pic="pic_url", name="Clan Name", tags=["tag1", "tag2"])
```

### ❌ dissolve
Dissolves the clan.

```python
clan.dissolve(clan_id="clan_id")
```

## 🛠️ Example

```python
import blockmango
from blockmango import Clan

# Initialize Clan instance
clan = Clan(user_id="your_user_id", access_token="your_access_token")

# Join a clan
clan.join(clan_id="clan_id")

# Search for clans
result = clan.search(clan_name="ExampleClan")
print(result)
```

This `README.md` provides an overview of the `Clan` class methods and usage examples. For more detailed usage, refer to the method definitions and parameters listed above.
