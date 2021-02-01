from bluedot import BlueDot
import time, sys, os

class BTWrapper(BlueDot):
    """
    Bluetooth wrapper for the Pi Zero W server
    Easy interface for the modified BlueDot package
    """

    def __init__(self):
        super().__init__(command_callback=self.respond)
        self.color = "red"
        self.set_when_pressed(self.shutdown)
        self.name = self.device
        
    def respond(self, message):
        """
        Process message from client

        :param String message:
            Stripped message from Android client

        Processes and responds to message through send()
        """
        print(f"{self.name}# {message}")
        if message.startswith("my name is"):
            self.name = message.split(" ")[-1]
            print("hi " + self.name + "!")
        if message == "hi":
            print("hey")
        if message == "exit" or message == "quit":
            self.quit()

    @staticmethod
    def quit(error=None):
        print("bye :(")
        sys.exit(0) if error is None else sys.exit(error)
            
    @staticmethod
    def shutdown():
        """
        Shut down any *nix-based system (requires root / sudoers privilege)
        """
        os.system("sudo poweroff")


if __name__ == "__main__":
    device = BTWrapper()

    while(True):
        time.sleep(1)
