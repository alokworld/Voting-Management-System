import hashlib

class Passkey:
    _p="xyz"
    def __init__(self):
        self.encrypted=hashlib.sha256(Passkey._p.encode()).hexdigest()
