# Hotkeys for typing commonly used punctuation marks
# Background: Every time I want to type the Chinese punctuation mark "、" (enumeration comma),
# I have to press the apostrophe key ('), then press "down", and then select the second punctuation mark.
# I wanted to use a key combination to quickly input some commonly used Chinese punctuation marks.
# That led to the creation of this script.
# Original code:https://stackoverflow.com/questions/54139609/using-python-to-create-a-hotkey-that-enters-text
#
# 快捷鍵打出常用的標點符號
# 源起：每次想要打出中文標點符號的頓號「、」，都要按一下「‘」，再按「下」，再選擇第二個標點
# 想要用快速鍵組合快速輸入某些常用的中文標點符號
# 產生了這個程式碼
# 原始程式碼：https://stackoverflow.com/questions/54139609/using-python-to-create-a-hotkey-that-enters-text
#
# v2_202504221540
# delete unused shift+p in COMBINATIONS
#
# v1_202504221530
# command+’ =>、


from pynput import keyboard
from pynput.keyboard import Key, Controller

kbd = Controller()

#COMBINATIONS = [
#        {keyboard.Key.shift, keyboard.KeyCode(char="p")},
#        {keyboard.Key.shift, keyboard.KeyCode(char="P")}
#        ]

COMBINATIONS = [
        {keyboard.Key.cmd, keyboard.KeyCode(char="'")}
        ]

current = set()

def execute():
    print("Dectected HotKey") #goes into the console window

    #if combination is shift+p
    #it should “hitting" backspace to remove the "P",
    #must be unnecessary if we use some other modifier (Alt, Ctrl)
    #kbd.press(Key.backspace)
    #kbd.release(Key.backspace)

    kbd.type('、') #goes into the active app window

def on_press(key):
    if any ([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()