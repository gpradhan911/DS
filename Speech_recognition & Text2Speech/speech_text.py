import sys
import speech_recognition as sr
import pyaudio
import time

# from pkg_resources import non_empty_lines
# from speech_recognition import Recognizer

r = sr.Recognizer()
recording_duration = 20
base_path = "/Users/gyanapradhan/Desktop/Datasets/"
OUTPUT_FILE = base_path+"/SText_output.txt"
starting_time= time.time()

def main():
    '''
    can listen to Microphone or from a audio file .wav .mpeg
    '''
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say something!")
        while (time.time() - starting_time) < recording_duration:
            try:
                audio = r.listen(source,timeout=6,phrase_time_limit=10)
                text = r.recognize_google(audio)

                # text = r.transcribe_speech(audio)
                save_file(text)
                my_print(text)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except Exception as e:
                print("Unexpected error:pl try again",{e})
                time.sleep(1)

def my_print(name):
    print(name)

'''recognize_google() method modularization issue with mac i386'''
# def transcribe_speech(audio):
#     try:
#         text=r.recognize_google(audio)
#         timestamp=time.time()
#         return timestamp + text
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#     except Exception as e:
#         print("Could not request results; {0}".format(e))
#         return None


def save_file(text):
    if text:
        with open(OUTPUT_FILE,"w") as f:
            f.write (text +"\n")






if __name__ == "__main__":
    main()