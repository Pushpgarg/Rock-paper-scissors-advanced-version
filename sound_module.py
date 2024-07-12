import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from playsound import playsound


class SoundManager:
    
    def play_sound(self, file, block=True):
        try:
            playsound(file, block=block)
        except:
            return

    def text_to_speech(self, text,speed=1):
        '''Generate speech from text'''
        speech = gTTS(text=text, lang="en")
        source_location = final_location = "./sounds/sound.mp3"
        speech.save(source_location)
        audio = AudioSegment.from_file("./sounds/sound.mp3", format="mp3")
        if(speed != 1):
            audio = audio.speedup(playback_speed=speed)
        audio = audio + 10
        audio.export(final_location, format="mp3")

        self.play_sound("./sounds/sound.mp3", True)

    def speech_to_text(self):
        '''return list to words spoken by you'''
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak something...")
            audio_data = recognizer.listen(source)
        try:
            text = (recognizer.recognize_google(audio_data)).split()
            return text
        except:
            return None

