from jnius import JavaClass, MetaJavaClass, JavaStaticMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseAuthEmail", )


class SJFirebaseAuthEmail(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseAuthEmail"
    get_instance = JavaStaticMethod("()Lcom/google/firebase/auth/FirebaseAuth;")
    check_user_signed_in = JavaStaticMethod("()Z")
