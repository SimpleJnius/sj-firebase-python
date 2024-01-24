from typing import Callable

from jnius import PythonJavaClass, java_method

__all__ = ("AuthStateListener", "IdTokenListener")


class AuthStateListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/auth/FirebaseAuth$AuthStateListener"]
    __javacontext__ = "app"

    def __init__(self, callback):
        self.callback = callback

    @java_method("(Lcom/google/firebase/auth/FirebaseAuth;)V")
    def onAuthStateChanged(self, auth):
        self.callback(auth)


class IdTokenListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/auth/FirebaseAuth$IdTokenListener"]
    __javacontext__ = "app"

    def __init__(self, callback):
        self.callback = callback

    @java_method("(Lcom/google/firebase/auth/FirebaseAuth;)V")
    def onIdTokenChanged(self, auth):
        self.callback(auth)
