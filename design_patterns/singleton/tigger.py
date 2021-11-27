
class _Tigger:
    def __str__(self):
        return 'i am the only one'

    def roar(self):
        return 'Grrr!!'

_instance = None

def Tigger():
    global _instance
    if _instance is None:
        return _instance
    else:
        _instance = _Tigger()
        return _instance