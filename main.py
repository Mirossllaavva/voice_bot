import speech_recognition as sr #Підкключаєио модуль для розпізновання мови
import subprocess
import webbrowser 
import intelect
from groq import Groq
import gtts
import os

#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
recogniser = sr.Recognizer() #створюємо розпізновач
def listening_voice(): #функція для прослуховування аудіо
    with sr.Microphone() as sourse: #підключення до мікрофону, як до істочнику
        print("Слухаю")
        audio =  recogniser.listen(sourse) #зберігаємо аудіо 
    return audio #повертаємо аудіо
def voice_in_text(audio): #функція для перетворення аудіо на текст
    try:
        text = recogniser.recognize_google(audio, language = "uk-UK") #Розпізнаємо текст та зберігаємо
        print(text)
        return text
    except:
        pass
def answer_bot(text):
    if text:
        if "привіт" in text.lower():
            print("привіт")
        
            
        # if "привіт" in text.lower():
        #     print("Привіт. Чим я можу допомогти?")
        # if "2 + 2" in text.lower():
        #     print("4")
        # if "німеччини" in text.lower():
        #     print("Берлін")
        elif "калькулятор" in text.lower():
            subprocess.call(["calc"])
        elif "гугл" in text.lower() or "google" in text.lower():
            subprocess.call(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
        elif "класрум" in text.lower() or "classroom" in text.lower():
            webbrowser.open("https://classroom.google.com/u/0/h?hl=ruhttps://classroom.google.com/u/0/h?hl=ru")
        # if "cутінки" in text.lower():
        #     webbrowser.open(f'https://music.youtube.com/search?q={text.lower()[7:]}')
        # elif "youtube" or "ютуб" in text.lower():
        #     webbrowser.open("https://music.youtube.com/")
        # elif "github" or "гитхаб" in text.lower():
        #     webbrowser.open("https://github.com/")
        elif "перекладач" in text.lower():
            webbrowser.open("https://www.multitran.com/")
            
        elif "календарь" in text.lower():
            subprocess.call(["calendar"])
        elif "калькулятор" in text.lower():
            subprocess.call(["calculator"])
        elif "камера" in text.lower():
            subprocess.call(["camera"])
        if "друг" in text:
            print(1)
            result = intelect.generator(text)
            language = "uk"
            speech = gtts.gTTS(text = result, lang = language, slow = False)
            speech.save("output.mp3")
            os.system("output.mp3")
            print(result)


    
def main():
    result_audio = listening_voice()
    result_text = voice_in_text(result_audio)
    answer_bot(result_text)
if __name__ == "__main__":
    main()
