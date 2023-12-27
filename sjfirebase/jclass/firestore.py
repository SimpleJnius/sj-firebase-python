from jnius import JavaClass, MetaJavaClass, JavaStaticMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseFirestore", )


class SJFirebaseFirestore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseFirestore"
    get_db = JavaStaticMethod("()Lcom/google/firebase/firestore/FirebaseFirestore;")
