# Auto-generated full reflection for com.google.firebase.remoteconfig.CustomSignals$Builder
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


class CustomSignalsBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/remoteconfig/CustomSignals$Builder"

    # constructors (signature, is_varargs)
    __javaconstructor__ = []

    # methods (grouped by name; overloads use JavaMultipleMethod)
    build = JavaMethod("()Lcom/google/firebase/remoteconfig/CustomSignals;")
    put = JavaMultipleMethod(
        [
            (
                "(Ljava/lang/String;Ljava/lang/String;)Lcom/google/firebase/remoteconfig/CustomSignals$Builder;",
                False,
                False,
            ),
            (
                "(Ljava/lang/String;J)Lcom/google/firebase/remoteconfig/CustomSignals$Builder;",
                False,
                False,
            ),
            (
                "(Ljava/lang/String;D)Lcom/google/firebase/remoteconfig/CustomSignals$Builder;",
                False,
                False,
            ),
        ]
    )
