from jnius import JavaClass, MetaJavaClass, JavaMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseAuthEmail", )


class SJFirebaseAuthEmail(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseAuthEmail"
    get_instance = JavaMethod("()Lcom/google/firebase/auth/FirebaseAuth;")
    get_uid = JavaMethod("()Ljava/lang/String;")
    check_user_signed_in = JavaMethod("()Z")
    create_user_with_email_and_password = JavaMethod(
        "(Ljava/lang/String;Ljava/lang/String;Lcom/google/android/gms/tasks/OnCompleteListener;)V"
    )
    sign_in_with_email_and_password = JavaMethod(
        "(Ljava/lang/String;Ljava/lang/String;Lcom/google/android/gms/tasks/OnCompleteListener;)V"
    )
