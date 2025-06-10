from jnius import JavaClass, MetaJavaClass, JavaStaticMethod, JavaStaticField
from sjfirebase import package_path

__all__ = ("SJFirebaseAuthEmail", "EmailAuthProvider")


class SJFirebaseAuthEmail(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseAuthEmail"
    get_instance = JavaStaticMethod("()Lcom/google/firebase/auth/FirebaseAuth;")
    check_user_signed_in = JavaStaticMethod("()Z")


class EmailAuthProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"com/google/firebase/auth/EmailAuthProvider"
    PROVIDER_ID = JavaStaticField("Ljava/lang/String;")
    EMAIL_LINK_SIGN_IN_METHOD = JavaStaticField("Ljava/lang/String;")
    EMAIL_PASSWORD_SIGN_IN_METHOD = JavaStaticField("Ljava/lang/String;")
    getCredential = JavaStaticMethod(
        "(Ljava/lang/String;Ljava/lang/String;)"
        "Lcom/google/firebase/auth/AuthCredential;"
    )
    getCredentialWithLink = JavaStaticMethod(
        "(Ljava/lang/String;Ljava/lang/String;)"
        "Lcom/google/firebase/auth/AuthCredential;"
    )