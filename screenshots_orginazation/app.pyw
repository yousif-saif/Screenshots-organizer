from pynput import keyboard
import pyautogui
import os
from helpers import format_window_title, notfiy_user, write_to_logs
import json

def get_file_name_and_root_app_name(window_title):
    root_app_name = ""

    if '-' in window_title:   
        root_app_name = window_title.split('-')[-1].strip()   

    else:
        words_list = window_title.split()

        root_app_name = window_title if len(words_list) <= 2 else words_list[-1].strip()
        

    if '.' in root_app_name:
        dot_index = root_app_name.index(".")
        root_app_name = root_app_name[:dot_index]

    formated_window_title = window_title if window_title == root_app_name else format_window_title(window_title, root_app_name)
    formated_window_title = window_title if formated_window_title == "" else formated_window_title


    return root_app_name, formated_window_title

images_folders = ""

with open("./settings.json", "r") as settings:
    json_settings = json.load(settings)

    images_folders = json_settings["save_folder"]

def on_press(key):
    if key == keyboard.Key.print_screen:
        try:
            window_title = pyautogui.getActiveWindowTitle()

            root_app_name, file_name = get_file_name_and_root_app_name(window_title)

            image_save_path = images_folders + root_app_name + "\\"

            if root_app_name not in os.listdir(images_folders):
                os.makedirs(image_save_path)

            images = os.listdir(image_save_path)
            
            if file_name + ".png" in images:                 
                file_number = 0
                for image in images:
                    if file_name in image:
                        file_number += 1

                file_name += f" ({file_number})"

            file_name += ".png"

            pyautogui.screenshot(image_save_path + file_name)
            notfiy_user(True)
        
        except Exception as err:
            notfiy_user(False)
            write_to_logs(err)
    

with keyboard.Listener(on_press=on_press) as lister:
    lister.join()
