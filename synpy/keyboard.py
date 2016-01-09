from .windows import *


class Keyboard:
    def press(self, key):
        key_press(key)
        return self


def key_press(key):
    key_down(key)
    key_up(key)


def key_down(key):
    ip = INPUT()
    ip.type = INPUT_KEYBOARD
    ip.ki.wVk = _get_key(key)

    SendInput(1, pointer(ip), sizeof(ip))


def key_up(key):
    ip = INPUT()
    ip.type = INPUT_KEYBOARD
    ip.ki.wVk = _get_key(key)
    ip.ki.dwFlags = KEYEVENTF_KEYUP

    SendInput(1, pointer(ip), sizeof(ip))


def _get_key(key):
    if type(key) == str:
        key = WORD(ord(key.upper()))

    return key
