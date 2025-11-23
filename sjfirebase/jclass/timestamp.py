# Auto-generated full reflection for com.google.firebase.Timestamp
# Source: javap -s output

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod,
    JavaStaticMethod,
    JavaStaticField,
    JavaMultipleMethod,
)


class Timestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/Timestamp"

    # constructors (signature, is_varargs)
    __javaconstructor__ = [
        ("(JI)V", False),
        ("(Ljava/util/Date;)V", False),
        ("(Ljava/time/Instant;)V", False),
    ]

    # static fields
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    Companion = JavaStaticField("Lcom/google/firebase/Timestamp$Companion;")

    # methods (grouped by name; overloads use JavaMultipleMethod)
    compareTo = JavaMultipleMethod(
        [
            ("(Lcom/google/firebase/Timestamp;)I", False, False),
            ("(Ljava/lang/Object;)I", False, False),
        ]
    )
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getNanoseconds = JavaMethod("()I")
    getSeconds = JavaMethod("()J")
    hashCode = JavaMethod("()I")
    now = JavaStaticMethod("()Lcom/google/firebase/Timestamp;")
    toDate = JavaMethod("()Ljava/util/Date;")
    toInstant = JavaMethod("()Ljava/time/Instant;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
