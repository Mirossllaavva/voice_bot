import speech_recognition as sr
recogniser = sr.Recognizer()
def listening_voice():
    with sr.Microphone() as sourse:
        print("Слухаю")
        audio =  recogniser.listen(sourse)
    return audio
def voice_in_text(audio):
    try:
        text = recogniser.recognize_google(audio)
        print(text)
    except:
        pass
def main():
    result_audio = listening_voice()
    voice_in_text(result_audio)
if __name__ == "__main__":
    main()
