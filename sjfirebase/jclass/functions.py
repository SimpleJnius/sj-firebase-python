from jnius import JavaClass, MetaJavaClass, JavaStaticMethod
from sjfirebase import package_path

__all__ = ("SJFirebaseFunctions", )


class SJFirebaseFunctions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}SJFirebaseFunctions"
    get_instance = JavaStaticMethod("()Lcom/google/firebase/firestore/FirebaseFunctions;")
