from jnius import JavaClass, MetaJavaClass, JavaStaticMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseAuthPhone", )


class SJFirebaseAuthPhone(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseAuthPhone"
    get_instance = JavaStaticMethod("()Lcom/google/firebase/auth/FirebaseAuth;")
    startPhoneNumberVerification = JavaStaticMethod(
        "(Ljava/lang/String;"
        "Ljava/lang/Long;"
        "Landroid/app/Activity;"
        "Lcom/google/firebase/auth/PhoneAuthProvider$OnVerificationStateChangedCallbacks;)V"
    )
    resendVerificationCode = JavaStaticMethod(
        "(Ljava/lang/String;"
        "Ljava/lang/Long;Landroid/app/Activity;"
        "Lcom/google/firebase/auth/PhoneAuthProvider$OnVerificationStateChangedCallbacks;"
        "Lcom/google/firebase/auth/PhoneAuthProvider$ForceResendingToken;)V"
    )
    verifyPhoneNumberWithCode = JavaStaticMethod(
        "(Ljava/lang/String;Ljava/lang/String;)Lcom/google/firebase/auth/PhoneAuthCredential;"
    )
