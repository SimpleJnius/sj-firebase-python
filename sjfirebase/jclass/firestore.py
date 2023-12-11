from jnius import JavaClass, MetaJavaClass, JavaMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseFirestore", )


class SJFirebaseFirestore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseFirestore"
    get_db = JavaMethod("()Lcom/google/firebase/firestore/FirebaseFirestore;")
