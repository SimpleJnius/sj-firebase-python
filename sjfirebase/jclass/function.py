from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod

__all__ = ("FirebaseFunctions", )


class FirebaseFunctions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/functions/FirebaseFunctions"
    getInstance = JavaMultipleMethod([
        (
            "(Lcom/google/firebase/FirebaseApp;Ljava/lang/String;)Lcom/google/firebase/functions/FirebaseFunctions;",
            True, False
        ),
        ("(Lcom/google/firebase/FirebaseApp;)Lcom/google/firebase/functions/FirebaseFunctions;", True, False),
        ("(Ljava/lang/String;)Lcom/google/firebase/functions/FirebaseFunctions;", True, False),
        ("()Lcom/google/firebase/functions/FirebaseFunctions;", True, False),
    ])
    getHttpsCallable = JavaMultipleMethod([
        ("(Ljava/lang/String;)Lcom/google/firebase/functions/HttpsCallableReference;", False, False),
        ("(Ljava/net/URL;)Lcom/google/firebase/functions/HttpsCallableReference;", False, False),
        ("(Ljava/lang/String;Lcom/google/firebase/functions/HttpsCallableOptions;)"
         "Lcom/google/firebase/functions/HttpsCallableReference;", False, False),
        ("(Ljava/net/URL;Lcom/google/firebase/functions/HttpsCallableOptions;)"
         "Lcom/google/firebase/functions/HttpsCallableReference;", False, False),
    ])
