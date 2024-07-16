from jnius import PythonJavaClass, java_method

__all__ = ("EventListener", "OnProgressListener")


class EventListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/firestore/EventListener"]
    __javacontext__ = "app"

    def __init__(self, on_event):
        self.on_event = on_event

    @java_method("(Ljava/lang/Object;Lcom/google/firebase/firestore/FirebaseFirestoreException;)V")
    def onEvent(self, value, error):
        self.on_event(value, error)


class OnProgressListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/firestore/OnProgressListener"]
    __javacontext__ = "app"

    def __init__(self, on_progress):
        self.on_progress = on_progress

    @java_method("(Ljava/lang/Object;)V")
    def onProgress(self, snapshot):
        self.on_progress(snapshot)
