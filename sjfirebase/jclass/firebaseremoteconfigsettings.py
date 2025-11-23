# Auto-generated full reflection for com.google.firebase.remoteconfig.FirebaseRemoteConfigSettings
# Source: javap -s output

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod,
    JavaStaticMethod,
    JavaField,
    JavaStaticField,
    JavaMultipleMethod,
)


class FirebaseRemoteConfigSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings"

    # constructors (signature, is_varargs)
    __javaconstructor__ = [
        (
            "(Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$Builder;"
            "Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$1;)V",
            False,
        ),
    ]

    # methods (grouped by name; overloads use JavaMultipleMethod)
    getFetchTimeoutInSeconds = JavaMethod("()J")
    getMinimumFetchIntervalInSeconds = JavaMethod("()J")
    toBuilder = JavaMethod(
        "()Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$Builder;"
    )

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = (
            "com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$Builder"
        )

        # methods (grouped by name; overloads use JavaMultipleMethod)
        build = JavaMethod(
            "()Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigSettings;"
        )
        getFetchTimeoutInSeconds = JavaMethod("()J")
        getMinimumFetchIntervalInSeconds = JavaMethod("()J")
        setFetchTimeoutInSeconds = JavaMethod(
            "(J)Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$Builder;"
        )
        setMinimumFetchIntervalInSeconds = JavaMethod(
            "(J)Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$Builder;"
        )
