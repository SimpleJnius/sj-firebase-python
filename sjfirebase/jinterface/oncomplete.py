from jnius import PythonJavaClass, java_method

__all__ = ("OnCompleteListener", )


class OnCompleteListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/android/gms/tasks/OnCompleteListener"]
    __javacontext__ = "app"

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method('(Lcom/google/android/gms/tasks/Task;)V')
    def onComplete(self, task):
        self.callback(task.isSuccessful())
