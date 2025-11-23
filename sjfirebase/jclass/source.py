__all__ = ("Source",)

from jnius import JavaClass, MetaJavaClass, JavaStaticField, JavaStaticMethod


class Source(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/firestore/Source"
    CACHE = JavaStaticField("Lcom/google/firebase/firestore/Source;")
    SERVER = JavaStaticField("Lcom/google/firebase/firestore/Source;")
    DEFAULT = JavaStaticField("Lcom/google/firebase/firestore/Source;")
    values = JavaStaticMethod(f"()[Lcom/google/firebase/firestore/Source;")
    valueOf = JavaStaticMethod(f"(Ljava/lang/String;)Lcom/google/firebase/firestore/Source;")
