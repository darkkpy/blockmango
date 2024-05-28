# 📧 Group Class Documentation

This documentation provides details on the `Group` class which is part of the `blockmango` module. The class interacts with a group management API, allowing various operations such as creating groups, managing group members, sending invitations, and more.

## 📦 Installation

To install the `blockmango` module, use the following command:

```sh
pip install blockmango
```

## 🚀 Usage

To use the `Group` class, import it from the `blockmango` module:

```python
import blockmango
from blockmango import Group
```

### 🔑 Initialization

```python
group = Group(user_id="your_user_id", access_token="your_access_token")
```

## 📚 Methods

### 🛠️ create
Creates a new group.

```python
group.create(member_ids=["member_id1", "member_id2"])
```

### 🚪 allow_invite
Allows or disallows group invitations.

```python
group.allow_invite(group_id="group_id", group_name="Group Name", invite_status=True)
```

### ✏️ edit
Edits group details such as name, notice, and invitation status.

```python
group.edit(group_id="group_id", group_name="Group Name", group_notice="Group Notice", invite_status=True, notice_pics=["pic1.jpg", "pic2.jpg"])
```

### 👮 admin
Assigns or removes admin rights to a member.

```python
group.admin(group_id="group_id", member_id="member_id", operation_type="add")
```

### 🤐 mute
Mutes a group member for a specific duration.

```python
group.mute(group_id="group_id", member_id="member_id", minutes=30)
```

### 💌 invite
Invites members to join a group.

```python
group.invite(group_id="group_id", member_ids=["member_id1", "member_id2"])
```

### 🚪 kick
Kicks members out of a group.

```python
group.kick(group_id="group_id", group_name="Group Name", member_ids=["member_id1", "member_id2"])
```

### ✅ approve_or_disapprove
Approves or disapproves a group application.

```python
group.approve_or_disapprove(group_id="group_id", operate_id="operation_id", j_type="approve")
```

### 🚶 quit
Quits a group.

```python
group.quit(group_id="group_id", group_name="Group Name")
```

### 📝 apply
Applies to join a group with a message.

```python
group.apply(group_id="group_id", msg="Please accept my request.")
```

### 🔄 transfer
Transfers group ownership to another member.

```python
group.transfer(group_id="group_id", new_owner="new_owner_id")
```

This `README.md` provides an overview of the `Group` class methods and usage examples. For more detailed usage, refer to the method definitions and parameters listed above.
