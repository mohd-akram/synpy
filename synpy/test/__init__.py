import time
import random

from synpy import Keyboard, Mouse, key_down, key_up, key_press, VK

keyboard = Keyboard()
mouse = Mouse()

keyboard.press('A').press('B').press('C')
mouse.left()
