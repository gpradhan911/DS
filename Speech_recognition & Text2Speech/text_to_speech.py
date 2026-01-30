from gtts import gTTS
import os
from playsound import playsound


from pyarrow import output_stream
base_path = "/Users/gyanapradhan/Desktop/Datasets/"
INPUT_FILE = base_path+"/SText2Speech_input.txt"
OUTPUT_FILE = base_path+"/Text_to_speech.mp3"
''' file handle as inedex then pass to readfile'''
file = open(INPUT_FILE, "r")
def readtext(filename):
    try:
        '''traditional file open and read'''
        # with open (filename,"r") as file:
            #text = file.read()
        text= file.read()
        print(text)
        return text
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)


# text = " Today is a chilly winter morning and we have hot sandwiches and mug of coffee to start our day with"
language_code = 'en'

output = gTTS(text= readtext(file), lang=language_code, slow=False)
output.save(OUTPUT_FILE)

'''save and replay'''
# with open(OUTPUT_FILE, 'wb') as file:
#     file.write(output)
file.close()
# os.system("playsound OUTPUT_FILE ")
playsound(OUTPUT_FILE)



