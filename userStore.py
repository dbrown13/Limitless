#userStore
_userName = ''

def set_user(name):
    global _userName
    _userName = name

def get_user():
    return _userName