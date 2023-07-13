import threading

class WorkerThread(threading.Thread):

    """Base class for workers."""

    def __init__(self):
        super(WorkerThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def getThreadId(self):
        return self.ident
