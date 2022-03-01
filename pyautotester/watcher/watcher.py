"""import time module, Observer, FileSystemEventHandler."""
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from pyautotester.abstract import AbstractTrigger


class Handler(FileSystemEventHandler):
    """Handle changes on current directory."""

    @staticmethod
    def on_any_event(event):
        if event.event_type == "modified" and event.src_path.endswith(".py"):
            os.system("clear", shell=False)  # nosec

            # Event is modified, you can process it now
            os.system("python -m unittest", shell=False)  # nosec
            time.sleep(1)


class WatchChangeTrigger(AbstractTrigger):
    """Main class to watch a directory."""

    # Set the directory on watch
    watchDirectory = "./src"

    def __init__(self):
        """Initialize the observer."""
        self.observer = Observer()

    def run(self):
        """Start the observer."""
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=True
        )
        self.observer.start()
        os.system("clear", shell=False)  # nosec
        print("Observer Started...")

        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped, bye!")

        self.observer.join()
