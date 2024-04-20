from jnius import autoclass
from sjfirebase import package

__all__ = ("SJFirebaseStorage", )


class SJFirebaseStorage:
    @classmethod
    def get_instance(cls, *args):
        return autoclass(f"{package}SJFirebaseStorage").get_instance(*args)
