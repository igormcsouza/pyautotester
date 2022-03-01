from abc import ABC, abstractclassmethod


class AbstractTrigger(ABC):
    """
    Abstract class for all triggers.
    """

    @abstractclassmethod
    def run(self):
        """
        Abstract method for triggering the test.
        """
        pass
