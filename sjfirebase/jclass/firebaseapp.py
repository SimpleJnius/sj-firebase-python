# Auto-generated full reflection for com.google.firebase.FirebaseApp
# Source: javap -s output

__all__ = ("FirebaseApp",)

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod,
    JavaStaticMethod,
    JavaStaticField,
    JavaMultipleMethod,
)


class FirebaseApp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/FirebaseApp"

    # constructors (signature, is_varargs)
    __javaconstructor__ = [
        (
            "(Landroid/content/Context;Ljava/lang/String;Lcom/google/firebase/FirebaseOptions;)V",
            False,
        ),
    ]

    # static fields
    DEFAULT_APP_NAME = JavaStaticField("Ljava/lang/String;")
    INSTANCES = JavaStaticField("Ljava/util/Map;")

    # methods (grouped by name; overloads use JavaMultipleMethod)
    addBackgroundStateChangeListener = JavaMethod(
        "(Lcom/google/firebase/FirebaseApp$BackgroundStateChangeListener;)V"
    )
    addLifecycleEventListener = JavaMethod(
        "(Lcom/google/firebase/FirebaseAppLifecycleListener;)V"
    )
    clearInstancesForTest = JavaStaticMethod("()V")
    delete = JavaMethod("()V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    get = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")
    getApplicationContext = JavaMethod("()Landroid/content/Context;")
    getApps = JavaStaticMethod("(Landroid/content/Context;)Ljava/util/List;")
    getInstance = JavaMultipleMethod(
        [
            ("()Lcom/google/firebase/FirebaseApp;", True, False),
            ("(Ljava/lang/String;)Lcom/google/firebase/FirebaseApp;", True, False),
        ]
    )
    getName = JavaMethod("()Ljava/lang/String;")
    getOptions = JavaMethod("()Lcom/google/firebase/FirebaseOptions;")
    getPersistenceKey = JavaMultipleMethod(
        [
            ("()Ljava/lang/String;", False, False),
            (
                "(Ljava/lang/String;Lcom/google/firebase/FirebaseOptions;)Ljava/lang/String;",
                True,
                False,
            ),
        ]
    )
    hashCode = JavaMethod("()I")
    initializeAllComponents = JavaMethod("()V")
    initializeApp = JavaMultipleMethod(
        [
            (
                "(Landroid/content/Context;)Lcom/google/firebase/FirebaseApp;",
                True,
                False,
            ),
            (
                "(Landroid/content/Context;Lcom/google/firebase/FirebaseOptions;)Lcom/google/firebase/FirebaseApp;",
                True,
                False,
            ),
            (
                "(Landroid/content/Context;Lcom/google/firebase/FirebaseOptions;Ljava/lang/String;)Lcom/google/firebase/FirebaseApp;",
                True,
                False,
            ),
        ]
    )
    isDataCollectionDefaultEnabled = JavaMethod("()Z")
    isDefaultApp = JavaMethod("()Z")
    removeBackgroundStateChangeListener = JavaMethod(
        "(Lcom/google/firebase/FirebaseApp$BackgroundStateChangeListener;)V"
    )
    removeLifecycleEventListener = JavaMethod(
        "(Lcom/google/firebase/FirebaseAppLifecycleListener;)V"
    )
    setAutomaticResourceManagementEnabled = JavaMethod("(Z)V")
    setDataCollectionDefaultEnabled = JavaMultipleMethod(
        [("(Ljava/lang/Boolean;)V", False, False), ("(Z)V", False, False)]
    )
    toString = JavaMethod("()Ljava/lang/String;")
