#userStore
_userName = ''
_userWeight = 0

def set_user(name):
    global _userName
    _userName = name

def get_user():
    return _userName

def set_weight(weight):
    global _userWeight
    _userWeight = weight

def get_weight():
    return _userWeight