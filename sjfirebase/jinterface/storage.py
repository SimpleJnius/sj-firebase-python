from jnius import PythonJavaClass, java_method

__all__ = ("OnProgressListener", "OnPausedListener")


class OnProgressListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/storage/OnProgressListener"]
    __javacontext__ = "app"

    def __init__(self, on_progress):
        self.on_progress = on_progress

    @java_method("(Ljava/lang/Object;)V")
    def onProgress(self, snapshot):
        self.on_progress(snapshot)


class OnPausedListener(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/storage/OnPausedListener"]
    __javacontext__ = "app"

    def __init__(self, on_paused):
        self.on_paused = on_paused

    @java_method("(Ljava/lang/Object;)V")
    def onPaused(self, snapshot):
        self.on_paused(snapshot)


class StreamDownloadTaskStreamProcessor(PythonJavaClass):
    __javainterfaces__ = ["com/google/firebase/storage/StreamDownloadTask$StreamProcessor"]
    __javacontext__ = "app"

    def __init__(self, do_in_background):
        self.do_in_background = do_in_background

    @java_method("(Lcom/google/firebase/storage/StreamDownloadTask$TaskSnapshot;"
                 "Ljava/io/InputStream;)V")
    def doInBackground(self, state, stream):
        self.do_in_background(state, stream)
