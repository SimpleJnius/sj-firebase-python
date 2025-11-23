from jnius import JavaClass, MetaJavaClass, JavaStaticField, JavaStaticMethod

__all__ = ("QueryDirection",)


class QueryDirection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"com/google/firebase/firestore/Query$Direction"
    ASCENDING = JavaStaticField("Lcom/google/firebase/firestore/Query$Direction;")
    DESCENDING = JavaStaticField("Lcom/google/firebase/firestore/Query$Direction;")
    values = JavaStaticMethod(f"()[Lcom/google/firebase/firestore/Query$Direction;")
    valueOf = JavaStaticMethod(f"(Ljava/lang/String;)Lcom/google/firebase/firestore/Query$Direction;")
