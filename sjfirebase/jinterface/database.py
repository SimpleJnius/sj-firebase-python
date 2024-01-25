from jnius import PythonJavaClass, java_method

__all__ = ("ValueEventListener", "ChildEventListener")


class ValueEventListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/database/ValueEventListener"]
    __javacontext__ = "app"

    def __init__(self, on_data_change, on_cancelled):
        super().__init__()
        self.on_data_change = on_data_change
        self.on_cancelled = on_cancelled

    @java_method('(Lcom/google/firebase/database/DataSnapshot;)V')
    def onDataChange(self, snapshot):
        self.on_data_change(snapshot)

    @java_method('(Lcom/google/firebase/database/DatabaseError;)V')
    def onCancelled(self, error):
        self.on_cancelled(error)


class CompletionListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/database/DatabaseReference$CompletionListener"]
    __javacontext__ = "app"

    def __init__(self, on_complete):
        super().__init__()
        self.on_complete = on_complete

    @java_method('(Lcom/google/firebase/database/DatabaseError;'
                 'Lcom/google/firebase/database/DatabaseReference)V')
    def onComplete(self, error, ref):
        self.on_complete(error, ref)


class ChildEventListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/database/ChildEventListener"]
    __javacontext__ = "app"

    def __init__(self, **kwargs):
        self.on_cancelled = kwargs.get("on_cancelled", lambda _: None)
        self.on_child_added = kwargs.get("on_child_added", lambda *_: None)
        self.on_child_moved = kwargs.get("on_child_moved", lambda *_: None)
        self.on_child_changed = kwargs.get("on_child_changed", lambda *_: None)
        self.on_child_removed = kwargs.get("on_child_removed", lambda _: None)

    @java_method('(Lcom/google/firebase/database/DatabaseError;)V')
    def onCancelled(self, error):
        self.on_cancelled(error)

    @java_method("(Lcom/google/firebase/database/DataSnapshot;Ljava/lang/String;)V")
    def onChildAdded(self, snapshot, previous_child_name):
        self.on_child_added(snapshot, previous_child_name)

    @java_method("(Lcom/google/firebase/database/DataSnapshot;Ljava/lang/String;)V")
    def onChildChanged(self, snapshot, previous_child_name):
        self.on_child_changed(snapshot, previous_child_name)

    @java_method("(Lcom/google/firebase/database/DataSnapshot;Ljava/lang/String;)V")
    def onChildMoved(self, snapshot, previous_child_name):
        self.on_child_moved(snapshot, previous_child_name)

    @java_method("(Lcom/google/firebase/database/DataSnapshot;)V")
    def onChildRemoved(self, snapshot):
        self.on_child_removed(snapshot)


class TransactionHandler(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/database/Transaction$Handler"]
    __javacontext__ = "app"

    def __init__(self, do_transaction, on_complete):
        super().__init__()
        self.do_transaction = do_transaction
        self.on_complete = on_complete

    @java_method("(Lcom/google/firebase/database/MutableData;)"
                 "Lcom/google/firebase/database/Transaction$Result")
    def doTransaction(self, current_data):
        self.do_transaction(current_data)

    @java_method('(Lcom/google/firebase/database/DatabaseError;'
                 'Lcom/google/firebase/database/DataSnapshot)V')
    def onComplete(self, error, current_data):
        self.on_complete(error, current_data)
