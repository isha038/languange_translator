#Importing all the required modules
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

#Creating Recogniser() class object
recog1 = spr.Recognizer()

#Creating microphone instance
mc = spr.Microphone()


#Capture Voice
with mc as source:
    print("Start with 'Hello' to initiate the translation")
    recog1.adjust_for_ambient_noise(source, duration = 0.4)
    audio = recog1.listen(source)
    MyText = recog1.recognize_google(audio)
    MyText = MyText.lower()

#Initializing the recorder with hello
if 'hello' in MyText:
    #Translator method 
    translator = Translator()

    from_lang = 'en'

    to_lang = "ne"

    with mc as source:
        print("Speak a sentence")
        recog1.adjust_for_ambient_noise(source, duration = 0.4)
        #Storing the speech into audio varaible
        audio = recog1.listen(source)
        #Using recognize.google() method to convert audio into text
        get_sentence = recog1.recognize_google(audio)

        #Using try and except to improve efficiency
        try:
            #Printing speech which needs to be translated
            print("Phrase to be translated:"+ get_sentence) 
            #Using translate() mwthod , three arguments 1) sentence to be translated
            #2} source language and 3} destination language
            text_to_translate = translator.translate(get_sentence, src= from_lang, dest = to_lang)
            #Storing the translated text in text variable
            text = text_to_translate.text

            #Using gTTS() method to speak the translated 
            #to speak the translated text 
            speak = gTTS(text=text, lang=to_lang, slow= False)

            #Using save() method to save the translated speech into voice.mps
            speak.save("voice.mp3")

            #Using OS module to run the translated voice
            os.system("start voice.mp3")

        except spr.UnknownValueError:
            print("Unable to understand the input")

        except spr.RequestError as e:
            print("Unable to provide required output".format(e))

