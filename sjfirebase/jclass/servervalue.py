from jnius import JavaClass, MetaJavaClass, JavaStaticField, JavaMultipleMethod

__all__ = ("ServerValue", )


class ServerValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"com/google/firebase/database/ServerValue"
    TIMESTAMP = JavaStaticField("Ljava/util/Map;")
    increment = JavaMultipleMethod([
        ("(J)Ljava/lang/Object;", True, False),
        ("(D)Ljava/lang/Object;", True, False)
    ])
