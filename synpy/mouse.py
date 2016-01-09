from .windows import *


class Mouse:
    def left(self):
        ip = INPUT()
        ip.type = INPUT_MOUSE
        ip.mi.dwFlags = MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP

        SendInput(1, pointer(ip), sizeof(ip))

        return self
