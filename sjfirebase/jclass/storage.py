from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseStorage", )


class SJFirebaseStorage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseStorage"
    get_instance = JavaMultipleMethod(
        [
            "()Lcom/google/firebase/storage/FirebaseStorage;",
            "(Ljava/lang/String;)Lcom/google/firebase/storage/FirebaseStorage;",
            "(Lcom/google/firebase/FirebaseApp;)Lcom/google/firebase/storage/FirebaseStorage;",
            "(Lcom/google/firebase/FirebaseApp;Ljava/lang/String;)Lcom/google/firebase/storage/FirebaseStorage;"
        ]
    )
