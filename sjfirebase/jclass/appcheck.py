# Auto-generated full reflection for com.google.firebase.appcheck.FirebaseAppCheck
# Source: javap -s output

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod,
    JavaMultipleMethod,
    JavaStaticMethod,
)


class FirebaseAppCheck(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/appcheck/FirebaseAppCheck"

    # methods (grouped by name; overloads use JavaMultipleMethod)
    addAppCheckListener = JavaMethod(
        "(Lcom/google/firebase/appcheck/FirebaseAppCheck$AppCheckListener;)V"
    )
    getAppCheckToken = JavaMethod("(Z)Lcom/google/android/gms/tasks/Task;")
    getInstance = JavaMultipleMethod(
        [
            ("()Lcom/google/firebase/appcheck/FirebaseAppCheck;", True, False),
            (
                "(Lcom/google/firebase/FirebaseApp;)Lcom/google/firebase/appcheck/FirebaseAppCheck;",
                True,
                False,
            ),
        ]
    )
    getLimitedUseAppCheckToken = JavaMethod("()Lcom/google/android/gms/tasks/Task;")
    installAppCheckProviderFactory = JavaMultipleMethod(
        [
            ("(Lcom/google/firebase/appcheck/AppCheckProviderFactory;)V", False, False),
            (
                "(Lcom/google/firebase/appcheck/AppCheckProviderFactory;Z)V",
                False,
                False,
            ),
        ]
    )
    removeAppCheckListener = JavaMethod(
        "(Lcom/google/firebase/appcheck/FirebaseAppCheck$AppCheckListener;)V"
    )
    setTokenAutoRefreshEnabled = JavaMethod("(Z)V")


class PlayIntegrityAppCheckProviderFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory"

    # methods (grouped by name; overloads use JavaMultipleMethod)
    create = JavaMethod(
        "(Lcom/google/firebase/FirebaseApp;)Lcom/google/firebase/appcheck/AppCheckProvider;"
    )
    getInstance = JavaStaticMethod(
        "()Lcom/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory;"
    )
