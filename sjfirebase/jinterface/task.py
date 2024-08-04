from jnius import PythonJavaClass, java_method

__all__ = (
    "OnCompleteListener",
    "OnCanceledListener",
    "OnFailureListener",
    "OnSuccessListener",
    "Continuation"
)


class OnCompleteListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/android/gms/tasks/OnCompleteListener"]
    __javacontext__ = "app"

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method('(Lcom/google/android/gms/tasks/Task;)V')
    def onComplete(self, task):
        self.callback(task)


class OnCanceledListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/android/gms/tasks/OnCanceledListener"]
    __javacontext__ = "app"

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method('()V')
    def onCanceled(self):
        self.callback()


class OnFailureListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/android/gms/tasks/OnFailureListener"]
    __javacontext__ = "app"

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method('(Ljava.lang.Exception;)V')
    def onFailure(self, e):
        self.callback(e)


class OnSuccessListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/android/gms/tasks/OnSuccessListener"]
    __javacontext__ = "app"

    def __init__(self, callback, args=False):
        super().__init__()
        self._args = args
        self.callback = callback

    @java_method('(Ljava/lang/Object;)V')
    def onSuccess(self, obj):
        if self._args:
            self.callback(obj)
        else:
            self.callback()


class Continuation(PythonJavaClass):
    __javainterfaces__ = ["com/google/android/gms/tasks/Continuation"]
    __javacontext__ = "app"

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method('(Lcom/google/android/gms/tasks/Task;)Ljava/lang/Object;')
    def then(self, obj):
        self.callback(obj)
