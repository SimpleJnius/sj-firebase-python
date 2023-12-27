from jnius import JavaClass, MetaJavaClass, JavaStaticMethod, JavaField
from sjfirebase import package_path

__all__ = ("ActionCodeSettings", )


class ActionCodeSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"com/google/firebase/auth/ActionCodeSettings"
    newBuilder = JavaStaticMethod("()Lcom/google/firebase/auth/ActionCodeSettings$Builder;")
