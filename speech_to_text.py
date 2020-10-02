import speech_recognition as sr
import keyboard
import gui
import appdirs as ad
import os
import io
import json

print("""
 ____                                  __          __               ______                __             
/\  _`\                               /\ \        /\ \__           /\__  _\              /\ \__          
\ \,\L\_\  _____      __     __    ___\ \ \___    \ \ ,_\   ___    \/_/\ \/    __   __  _\ \ ,_\         
 \/_\__ \ /\ '__`\  /'__`\ /'__`\ /'___\ \  _ `\   \ \ \/  / __`\     \ \ \  /'__`\/\ \/'\\\ \ \/         
   /\ \L\ \ \ \L\ \/\  __//\  __//\ \__/\ \ \ \ \   \ \ \_/\ \L\ \     \ \ \/\  __/\/>  </ \ \ \_        
   \ `\____\ \ ,__/\ \____\ \____\ \____\\\ \_\ \_\   \ \__\ \____/      \ \_\ \____\/\_/\_\ \ \__\       
    \/_____/\ \ \/  \/____/\/____/\/____/ \/_/\/_/    \/__/\/___/        \/_/\/____/\//\/_/  \/__/       
             \ \_\                                                                                       
              \/_/                                                                                       
 __                  __  __                  ______             ___                 __                   
/\ \                /\ \/\ \                /\__  _\          /'___\ __          __/\ \__                
\ \ \____  __  __   \ \ `\\\ \     __   __  _\/_/\ \/     ___ /\ \__//\_\    ___ /\_\ \ ,_\    __         
 \ \ '__`\/\ \/\ \   \ \ , ` \  /'__`\/\ \/'\  \ \ \   /' _ `\ \ ,__\/\ \ /' _ `\/\ \ \ \/  /'__`\       
  \ \ \L\ \ \ \_\ \   \ \ \`\ \/\  __/\/>  </   \_\ \__/\ \/\ \ \ \_/\ \ \/\ \/\ \ \ \ \ \_/\  __/       
   \ \_,__/\/`____ \   \ \_\ \_\ \____\/\_/\_\  /\_____\ \_\ \_\ \_\  \ \_\ \_\ \_\ \_\ \__\ \____\      
    \/___/  `/___/> \   \/_/\/_/\/____/\//\/_/  \/_____/\/_/\/_/\/_/   \/_/\/_/\/_/\/_/\/__/\/____/      
               /\___/                                                                                    
               \/__/                                                                                     
""")

# Setup appdirs
app_name = "speech-to-text"
app_author = "nexinfinite"
settings_directory = ad.user_data_dir(app_name, app_author)
is_folder = os.path.isdir(settings_directory)
if not is_folder:
    os.makedirs(settings_directory)
    print("CREATING SETTINGS FOLDER")

# Setting up the json file
setting_file_path = settings_directory + "\\settings.json"
is_file = os.path.isfile(setting_file_path)
if is_file and os.access(setting_file_path, os.R_OK):
    print("OPENED SETTINGS FILE")
else:
    with io.open(os.path.join(settings_directory, 'settings.json'), 'w') as db_file:
        new_file_json = [
            {
                "name": "type_text",
                "value": True
            },
            {
                "name": "repeat",
                "value": True
            }
        ]
        db_file.write(json.dumps(new_file_json, indent=2))
    print("CREATED SETTING FILE")

# creating variables
running = None
with open(setting_file_path) as f:
    settings_json = json.load(f)
    f.close()


def start():
    global running

    print("Starting...")
    running = True
    print("Started!")

    def callback(recognizer, audio):
        if not running:
            stop_listening(wait_for_stop=False)
            return
        try:
            text = recognizer.recognize_google(audio, language="en-us")

            check_text(text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(m, callback)


def check_text(text):
    if text.startswith("command "):
        command = text.strip("command ")
        print("COMMAND: {}".format(command))

        if command == "penis":
            for _ in range(10):
                keyboard.write("penis\n")

        elif command.startswith("repeat"):
            repeat_setting = get_setting("repeat")
            if not repeat_setting:
                return
            split = command.split(" ")
            number = split[-2]
            try:
                number = int(number)
                text_to_send = " ".join(split[1:-2])
                for _ in range(number):
                    keyboard.write("{}\n".format(text_to_send))
                print("REPEAT ({}): {}".format(number, text_to_send))
            except ValueError:
                print("REPEAT: Didn't match")

        elif command.startswith("italics"):
            text_to_send = command.strip("italics ")
            keyboard.write("*{}*\n".format(text_to_send))
            print("ITALICS: {}".format(text_to_send))
    else:
        type_text_setting = get_setting("type_text")
        if type_text_setting:
            keyboard.write("{}\n".format(text))
        print("TEXT: {}".format(text))
        if len(text) > 30:
            split = text[0:29].split(" ")
            text = str(" ".join(split[0:-1])) + "..."
        gui.update_text(text.capitalize())


def stop():
    global running
    print("Stopping...")
    running = False
    print("Stopped!")


def get_setting(setting_name):
    for setting in settings_json:
        if setting["name"] == setting_name:
            return setting['value']
    return False


def save_setting(setting_name, value):
    for setting in settings_json:
        if setting['name'] == setting_name:
            setting['value'] = value
            with open(setting_file_path, "w") as file:
                json.dump(settings_json, file)
            print("SAVED SETTING: {} - {}".format(setting_name, value))
            return True
    return False

