__all__ = ("VerificationStateChangeCallback",)

from jnius import PythonJavaClass, java_method


class VerificationStateChangeCallback(PythonJavaClass):
    __javainterfaces__ = ["com/simplejnius/sjfirebase/callback/VerificationStateChangeCallback"]
    __javacontext__ = "app"

    def __init__(self, on_code_sent, on_verification_completed, on_verification_failed):
        self.on_code_sent = on_code_sent
        self.on_verification_completed = on_verification_completed
        self.on_verification_failed = on_verification_failed

    @java_method("(Ljava/lang/String;Lcom/google/firebase/auth/PhoneAuthProvider$ForceResendingToken;)V")
    def onCodeSent(self, verification_id, token):
        self.on_code_sent(verification_id, token)

    @java_method("(Lcom/google/firebase/auth/PhoneAuthCredential;)V")
    def onVerificationCompleted(self, credentials):
        self.on_verification_completed(credentials)

    @java_method("(Lcom/google/firebase/FirebaseException;)V")
    def onVerificationFailed(self, exception):
        self.on_verification_failed(exception)
