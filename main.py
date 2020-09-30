import time
import speech_recognition as sr
import keyboard


def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)

        if text.startswith("command "):
            command = text.strip("command ")
            print(f"COMMAND: {command}")

            if command == "penis":
                for _ in range(10):
                    keyboard.write(f"penis\n")
            elif command.startswith("repeat"):
                split = command.split(" ")
                number = split[-2]
                try:
                    number = int(number)
                    text_to_send = " ".join(split[1:-2])
                    for _ in range(number):
                        keyboard.write(f"{text_to_send}\nI'm not thinking I'll give it you"
                                       f"")
                    print(f"REPEAT ({number}): {text_to_send}")
                except ValueError:
                    print("Didnt match")
        else:
            keyboard.write(f"{text}\n")
            print(f"TEXT: {text}")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

while True:
    time.sleep(0.1)
