from jnius import JavaClass, MetaJavaClass, JavaStaticMethod

__all__ = ("Transaction", )


class Transaction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"com/google/firebase/database/Transaction"
    abort = JavaStaticMethod("()Lcom/google/firebase/database/Transaction$Result;")
    success = JavaStaticMethod(
        "(Lcom/google/firebase/database/MutableData;)"
        "Lcom/google/firebase/database/Transaction$Result;"
    )
