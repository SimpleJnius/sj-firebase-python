from jnius import JavaClass, MetaJavaClass, JavaStaticMethod, JavaMultipleMethod

__all__ = ("FieldValue", )


class FieldValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"com/google/firebase/firestore/FieldValue"
    delete = JavaStaticMethod("()Lcom/google/firebase/firestore/FieldValue;")
    serverTimestamp = JavaStaticMethod("()Lcom/google/firebase/firestore/FieldValue;")
    arrayUnion = JavaStaticMethod("([Ljava/lang/Object;)Lcom/google/firebase/firestore/FieldValue;")
    arrayRemove = JavaStaticMethod("([Ljava/lang/Object;)Lcom/google/firebase/firestore/FieldValue;")
    increment = JavaMultipleMethod([
        ("(J)Lcom/google/firebase/firestore/FieldValue;", True, False),
        ("(D)Lcom/google/firebase/firestore/FieldValue;", True, False),
    ])
