import time
import speech_recognition as sr
import keyboard


def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language="en-gb")

        if text.startswith("command "):
            command = text.strip("command ")
            print("COMMAND: {}".format(command))

            if command == "penis":
                for _ in range(10):
                    keyboard.write("penis\n")

            elif command.startswith("repeat"):
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
            keyboard.write("{}\n".format(text))
            print("TEXT: {}".format(text))

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
