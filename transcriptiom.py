import speech_recognition as sr
recognizer = sr.Recognizer()


audio_file = "#audio file in wav format"

with sr.AudioFile(audio_file) as source:
    print("Listening to the audio...")
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="te-IN")
    print("Transcription in Telugu: ", text)

    with open("telugu_transcription.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("Transcription saved to telugu_transcription.txt")

except sr.RequestError:
    print("Could not request results from Google Speech Recognition service")
except sr.UnknownValueError:
    print("Audio could not be understood")
