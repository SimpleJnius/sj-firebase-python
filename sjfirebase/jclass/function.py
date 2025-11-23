from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod, JavaField, JavaMethod

__all__ = ("FirebaseFunctions", "HttpsCallableOptions")


class FirebaseFunctions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/functions/FirebaseFunctions"
    getInstance = JavaMultipleMethod(
        [
            (
                "(Lcom/google/firebase/FirebaseApp;Ljava/lang/String;)Lcom/google/firebase/functions/FirebaseFunctions;",
                True,
                False,
            ),
            (
                "(Lcom/google/firebase/FirebaseApp;)Lcom/google/firebase/functions/FirebaseFunctions;",
                True,
                False,
            ),
            (
                "(Ljava/lang/String;)Lcom/google/firebase/functions/FirebaseFunctions;",
                True,
                False,
            ),
            ("()Lcom/google/firebase/functions/FirebaseFunctions;", True, False),
        ]
    )
    getHttpsCallable = JavaMultipleMethod(
        [
            (
                "(Ljava/lang/String;)Lcom/google/firebase/functions/HttpsCallableReference;",
                False,
                False,
            ),
            (
                "(Ljava/net/URL;)Lcom/google/firebase/functions/HttpsCallableReference;",
                False,
                False,
            ),
            (
                "(Ljava/lang/String;Lcom/google/firebase/functions/HttpsCallableOptions;)"
                "Lcom/google/firebase/functions/HttpsCallableReference;",
                False,
                False,
            ),
            (
                "(Ljava/net/URL;Lcom/google/firebase/functions/HttpsCallableOptions;)"
                "Lcom/google/firebase/functions/HttpsCallableReference;",
                False,
                False,
            ),
        ]
    )


class HttpsCallableOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/functions/HttpsCallableOptions"

    # constructors (signature, is_varargs)
    __javaconstructor__ = [
        ("(ZLkotlin/jvm/internal/DefaultConstructorMarker;)V", False),
    ]

    # instance fields
    limitedUseAppCheckTokens = JavaField("Z")

    # methods (grouped by name; overloads use JavaMultipleMethod)
    getLimitedUseAppCheckTokens = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/firebase/functions/HttpsCallableOptions$Builder"

        # instance fields
        limitedUseAppCheckTokens = JavaField("Z")

        # methods (grouped by name; overloads use JavaMultipleMethod)
        build = JavaMethod("()Lcom/google/firebase/functions/HttpsCallableOptions;")
        getLimitedUseAppCheckTokens = JavaMethod("()Z")
        setLimitedUseAppCheckTokens = JavaMethod(
            "(Z)Lcom/google/firebase/functions/HttpsCallableOptions$Builder;"
        )
