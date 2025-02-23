__all__ = ("SJFirebaseFirestore", "Source")

from jnius import JavaClass, MetaJavaClass, JavaStaticMethod, JavaMultipleMethod
from sjfirebase import package_path

_Source_package = "com/google/firebase/firestore/Source"
_Source_signature = "Lcom/google/firebase/firestore/Source;"
_FieldValue_package = "com/google/firebase/firestore/FieldValue"


class SJFirebaseFirestore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseFirestore"
    get_db = JavaStaticMethod("()Lcom/google/firebase/firestore/FirebaseFirestore;")


class Source(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = _Source_package
    CACHE = JavaStaticMethod(_Source_signature)
    SERVER = JavaStaticMethod(_Source_signature)
    DEFAULT = JavaStaticMethod(_Source_signature)
    values = JavaStaticMethod(f"()[{_Source_signature}")
    valueOf = JavaStaticMethod(f"(Ljava/lang/String;){_Source_signature}")


class FieldValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = _FieldValue_package
    delete = JavaStaticMethod(f"(){_FieldValue_package};")
    serverTimestamp = JavaStaticMethod(f"(){_FieldValue_package};")
    arrayUnion = JavaStaticMethod(f"([Ljava/lang/Object;){_FieldValue_package};")
    arrayRemove = JavaStaticMethod(f"([Ljava/lang/Object;){_FieldValue_package};")
    increment = JavaMultipleMethod([
        (f"(J){_FieldValue_package};", True, False),
        (f"(D){_FieldValue_package};", True, False)
    ])

