import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from playsound import playsound
import os

class SoundManager:

    def play_sound(self, file, block=True):
        """
        Plays a sound file.

        This method uses the `playsound` function to play the audio file specified by `file`.
        The `block` parameter determines whether the method should block execution until the sound has finished playing.

        Parameters:
        - file (str): The path to the sound file to be played.
        - block (bool): If True, the method will block until the sound has finished playing.
          If False, the method will return immediately after starting playback.

        Returns:
        - None: This method does not return a value.

        Raises:
        - Exception: If an error occurs while attempting to play the sound, the method catches the exception and returns silently.
        """
        try:
            playsound(file, block=block)
        except Exception as e:
            print(f"An error occurred while playing sound: {e}")

    def text_to_speech(self, text, language="en", speed=1, volume=0):
        """Converts text to speech and plays the resulting audio.

        This method uses the Google Text-to-Speech (gTTS) library to generate speech from the provided text.
        The generated speech is saved as an MP3 file, which is then modified by adjusting the playback speed and volume.
        Finally, the adjusted audio file is played using the `play_sound` method.

        Parameters:
        - text (str): The text to be converted into speech.
        - language (str): The language for the speech. Default is English ("en").
        - speed (float): The playback speed. Default is 1 (normal speed). Values should be between 0.5 (half speed) and 2 (double speed).
        - volume (int): The volume adjustment in dB. Default is 0 (no change).

        Returns:
        - None: This method does not return a value.

        Raises:
        - Exception: If there is an error during the text-to-speech conversion, audio file modification, or playback, the method will handle it internally.
        """
        if not os.path.exists('./sounds'):
            os.makedirs('./sounds')
        

        speech = gTTS(text=text, lang=language)
        source_location = final_location = "./sounds/sound.mp3"
        speech.save(source_location)

        audio = AudioSegment.from_file(source_location, format="mp3")
        if speed!=1 :
            audio = audio.speedup(playback_speed=speed)
        audio = audio + volume
        audio.export(final_location, format="mp3")

        self.play_sound(final_location, True)


    def speech_to_text(self, timeout=1.5, phrase_time_limit=4):
        """
        Return a list of words spoken, with features to stop recognition
        if there is no speech for a specified timeout and record for a maximum duration.

        Parameters:
        - timeout: The time in seconds to wait for speech before giving up.
        - phrase_time_limit: The maximum time in seconds to record speech.

        Returns:
        - A list of words spoken, or None if recognition fails.
        """
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak something...")
            try:
                audio_data = recognizer.listen(
                    source, timeout=timeout, phrase_time_limit=phrase_time_limit
                )
                text = recognizer.recognize_google(audio_data)
                return text.split()
            except sr.WaitTimeoutError:
                print("No speech detected within the timeout period.")
                return None
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None
