from pyautotester.watcher import WatchChangeTrigger


class MainLoop:
    def __init__(self) -> None:
        self.trigger = WatchChangeTrigger()

    def start_main_loop(self):
        self.trigger.run()


def main():
    loop = MainLoop()
    loop.start_main_loop()
