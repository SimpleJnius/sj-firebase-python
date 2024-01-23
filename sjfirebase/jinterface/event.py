from jnius import PythonJavaClass, java_method

__all__ = ("ValueEventListener",)


class ValueEventListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/database/ValueEventListener"]
    __javacontext__ = "app"

    def __init__(self, data_change_callback, cancel_callback):
        super().__init__()
        self.data_change_callback = data_change_callback
        self.cancel_callback = cancel_callback

    @java_method('(com/google/firebase/database/DataSnapshot;)V')
    def onDataChange(self, snapshot):
        self.data_change_callback(snapshot)

    @java_method('(com/google/firebase/database/DatabaseError;)V')
    def onCancelled(self, error):
        self.cancel_callback(error)
