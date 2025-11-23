from jnius import PythonJavaClass, java_method


class ConfigUpdateListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/remoteconfig/ConfigUpdateListener"]
    __javacontext__ = "app"  # optional, only needed if required by your environment

    def __init__(self, on_update, on_error):
        super().__init__()
        self.on_update = on_update
        self.on_error = on_error

    @java_method("(Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigException;)V")
    def onError(self, error):
        self.on_error(error)

    @java_method("(Lcom/google/firebase/remoteconfig/ConfigUpdate;)V")
    def onUpdate(self, config_update):
        self.on_update(config_update)
