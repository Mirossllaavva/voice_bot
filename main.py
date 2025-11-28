import speech_recognition as sr #Підкключаєио модуль для розпізновання мови
recogniser = sr.Recognizer() #створюємо розпізновач
def listening_voice(): #функція для прослуховування аудіо
    with sr.Microphone() as sourse: #підключення до мікрофону, як до істочнику
        print("Слухаю")
        audio =  recogniser.listen(sourse) #зберігаємо аудіо 
    return audio #повертаємо аудіо
def voice_in_text(audio): #функція для перетворення аудіо на текст
    try:
        text = recogniser.recognize_google(audio) #Розпізнаємо текст та зберігаємо
        print(text)
    except:
        pass
def main():
    result_audio = listening_voice()
    voice_in_text(result_audio)
if __name__ == "__main__":
    main()
