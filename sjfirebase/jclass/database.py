from jnius import JavaClass, MetaJavaClass, JavaStaticMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseDatabase", )


class SJFirebaseDatabase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseDatabase"
    get_db = JavaStaticMethod("()Lcom/google/firebase/database/FirebaseDatabase;")
    get_ref = JavaStaticMethod("()Lcom/google/firebase/database/DatabaseReference;")
