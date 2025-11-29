import speech_recognition as sr #Підкключаєио модуль для розпізновання мови
import subprocess
import webbrowser 
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
    if "привіт" in text.lower():
        print("Привіт. Чим я можу допомогти?")
    if "2 + 2" in text.lower():
        print("4")
    if "німеччини" in text.lower():
        print("Берлін")
    if "калькулятор" in text.lower():
        subprocess.call(["calc"])
    if "гугл" in text.lower() or "google" in text.lower():
        subprocess.call(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
    if "класрум" in text.lower() or "classroom" in text.lower():
        webbrowser.open("https://classroom.google.com/u/0/h?hl=ruhttps://classroom.google.com/u/0/h?hl=ru")
    # if "cутінки" in text.lower():
    #     webbrowser.open(f'https://music.youtube.com/search?q={text.lower()[7:]}')
    if "youTube" or "ютуб" in text.lower():
        webbrowser.open("https://music.youtube.com/")
    
def main():
    result_audio = listening_voice()
    result_text = voice_in_text(result_audio)
    answer_bot(result_text)
if __name__ == "__main__":
    main()
