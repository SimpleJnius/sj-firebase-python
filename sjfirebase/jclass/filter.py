from jnius import JavaClass, MetaJavaClass, JavaStaticMethod, JavaMultipleMethod
from sjfirebase import package_path

__all__ = ("Filter", )


class Filter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/firestore/Filter"
    equalTo = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    notEqualTo = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    greaterThan = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    greaterThanOrEqualTo = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    lessThan = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    lessThanOrEqualTo = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    arrayContains = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/lang/Object;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    arrayContainsAny = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/util/List;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/util/List;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    inArray = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/util/List;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/util/List;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    notInArray = JavaMultipleMethod([
        ("(Ljava/lang/String;Ljava/util/List;)Lcom/google/firebase/firestore/Filter;", True, False),
        ("(Lcom/google/firebase/firestore/FieldPath;Ljava/util/List;)Lcom/google/firebase/firestore/Filter;",
         True, False),
    ])
    or_ = locals()["or"] = JavaStaticMethod(
        "([Lcom/google/firebase/firestore/Filter;)Lcom/google/firebase/firestore/Filter;")
    and_ = locals()["and"] = JavaStaticMethod(
        "([Lcom/google/firebase/firestore/Filter;)Lcom/google/firebase/firestore/Filter;")
