from jnius import JavaClass, MetaJavaClass, JavaMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseDatabase", )


class SJFirebaseDatabase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseDatabase"
    get_db = JavaMethod("()Lcom/google/firebase/database/FirebaseDatabase;")
