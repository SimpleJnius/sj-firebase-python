from jnius import JavaClass, MetaJavaClass, JavaStaticMethod, autoclass
from sjfirebase import package_path

__all__ = ("SJFirebaseUser",)


class SJFirebaseUser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseUser"
    get_current_user = JavaStaticMethod("()Lcom/google/firebase/auth/FirebaseUser;")
    profile_change_request_builder = JavaStaticMethod("()Lcom/google/firebase/auth/UserProfileChangeRequest$Builder;")
