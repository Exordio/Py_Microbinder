import keyboard as kd
import time
import configparser
import os

configFile = "config.ini"

def load_Config():
    global Config
    if os.path.exists(configFile):
        Config = configparser.ConfigParser()
        Config.read(configFile)
        print("Config file successfully loaded.")
        return True
    else:
        with open(configFile, "w", encoding="utf8") as f:
            f.write("[HOTKEYS_BUTTONS]\nHOTKEY_1 = tab+1\nHOTKEY_2 = tab + 2\nHOTKEY_3 = tab + 3\nHOTKEY_4 = tab + 4\nHOTKEY_5 = tab + 5\nHOTKEY_6 = tab + 6\n"
                    "[HOTKEYS_VALUES]\nHOTKEY_1_VALUE = /home base\nHOTKEY_2_VALUE = /home gas\nHOTKEY_3_VALUE = /home home\nHOTKEY_4_VALUE = /home ferma\nHOTKEY_5_VALUE = /warp thedeathwalker\nHOTKEY_6_VALUE = /warp glaxor\n")
        print("Config file successfully created!")
        return False


def launch_Macros(hotkey_Value):
    time.sleep(0.5)
    chat_key = "t"
    kd.press_and_release(chat_key)
    time.sleep(0.2)

    for char in hotkey_Value:
        kd.press_and_release(char)

    kd.press_and_release('enter')


if load_Config() != False:
    print("Chat binder is start : )")
    x = dict(Config.items('HOTKEYS_BUTTONS'))
    y = dict(Config.items('HOTKEYS_VALUES'))
    for i in range(len(list(x.values()))):
        kd.add_hotkey(list(x.values())[i], launch_Macros, args=[list(y.values())[i]])
    kd.wait('ctrl + z')
else:
    print("Exit, restart program now")





