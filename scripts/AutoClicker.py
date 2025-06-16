import pynput
import time
import threading

from pynput.mouse import Button, Controller

from pynput.keyboard import Listener, KeyCode, Key

delay = 0.001
button = Button.left
key = KeyCode.from_char('a')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        
    def start_clicking(self): 
            self.running = True
    
    def stop_clicking(self): 
            self.running = False
    
    def exit(self): 
            self.stop_clicking() 
            self.program_running = False
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
class ClickKey(threading.Thread):
    def __init__(self, key):
        super(ClickKey, self).__init__()
        self.key = key
        self.delay = delay
        self.running = False
        self.program_running = True
    def start_clicking(self):
        self.running = True
    def stop_clicking(self):
        self.running = False
    def exit(self):
        self.stop_clicking()
        self.program_running = False
    def run(self):
        while self.program_running:
            while self.running:
                with pynput.keyboard.Controller() as keyboard:
                    keyboard.press(self.key)
                    time.sleep(self.delay)
                    keyboard.release(self.key)
            time.sleep(0.1)
            
class SafeKeyCode(object):
    def __getattr__(self, name):
        return getattr(Key, name, KeyCode(vk=-1, char=name))
    
    
virtual_key = SafeKeyCode()


class BaseKeySymbols(object):
    F12 = virtual_key.f12
    CAPS_LOCK = virtual_key.caps_lock
    
    
start_stop_key = BaseKeySymbols().CAPS_LOCK
stop_key = BaseKeySymbols().CAPS_LOCK
mouse = Controller()
keyboard = pynput.keyboard.Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
keyboard_thread = ClickKey(key)
keyboard_thread.start()


def on_press(key): 
    
    if key == start_stop_key: 
        if click_thread.running: 
            click_thread.stop_clicking() 
        else: 
            click_thread.start_clicking() 
              
    elif key == stop_key: 
        click_thread.exit() 
        listener.stop() 
  
  
with Listener(on_press=on_press) as listener: 
    listener.join()