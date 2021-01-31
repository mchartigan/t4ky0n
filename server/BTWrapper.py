from bluedot import BlueDot
import os

class BTWrapper(BlueDot):
    """
    Bluetooth wrapper for the Pi Zero W server
    Easy interface for the modified BlueDot package
    """

    def __init__(self):
        super().__init__(command_callback=self.respond)
        super().color("red")
        super().set_when_pressed(self.shutdown)

    def respond(self, message):
        """
        Process message from client

        :param String message:
            Stripped message from Android client

        Processes and responds to message through send()
        """
        print(f"Message received: \"{message}\"")
        if message == "hi":
            print("hey")

    def shutdown():
        """
        Shut down any *nix-based system (requires root / sudoers privilege)
        """
        os.system("sudo poweroff")


if __name__ == "__main__":
    device = BTWrapper()
