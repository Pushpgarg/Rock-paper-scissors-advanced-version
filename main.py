# importing standard module
import os
import random
import time
import joblib
vectorizer = joblib.load('vectorizer.pkl')
classifier = joblib.load('model.pkl')

# importing from custom made files
from TextProcessing import TextPreprocessing
from art import logo, win, lose, tie
from sound_module import SoundManager

clear = lambda: os.system("clear" if os.name == "posix" else "cls")
clear()
options = ("rock", "paper", "scissors")

sound_functions = SoundManager()
text_processor = TextPreprocessing()



def declare_result(result):
    if result=="win":
        print(win)
        sound_functions.text_to_speech("you win the game")
    elif result == "lose":
        print(lose)
        sound_functions.text_to_speech("you lose the game")
    else:
        print(tie)
        sound_functions.text_to_speech("its a tie")

def player_choosing():
    print("speak what you choose rock , paper or scissors:-")
    sound_functions.text_to_speech("speak what you choose rock , paper or scissors:-")
    player_words = sound_functions.speech_to_text()

    print(player_words)
    if player_words == None:
        print("unable to capture your voice")
        player_choose = input("choose rock , paper or scissors").lower()
        if(player_choose not in options):
            player_choosing()
        else:
            return player_choose
    else:
        for word in player_words:
            if word.lower() in ("rock", "paper", "scissors"):
                return word.lower()
        else:
            print(
                f"we get {player_words} as input from you pls choose rock , paper or scissors"
            )
            player_choosing()


def ask_to_play():
    print("do you want to play")
    sound_functions.text_to_speech("do you want to play")
    user_voice_input = sound_functions.speech_to_text()
    if user_voice_input == None:
        print("unable to capture your voice")
        # here inout is taken from the user which is preprocessed --> vectorized --> classsified
        want_to_play = classifier.predict(vectorizer.transform(text_processor.text_processing(input("do you want to play : ").lower())))
        if want_to_play == "yes":
            return True
        else:
            return False
        
    else:
        want_to_play = classifier.predict(vectorizer.transform(text_processor.text_processing(" ".join(user_voice_input))))
        if want_to_play == "yes":
            return True
        else:
            return False


def check_results(computer_choose, player_choose):

    print(f"you have chosen : {player_choose}")
    print(f"computer has chosen : {computer_choose}")
    if computer_choose == player_choose:
        declare_result("tie")
        return
    if computer_choose == "rock":
        declare_result("lose") if (player_choose == "scissors") else declare_result("win")
    elif computer_choose == "paper":
        declare_result("lose") if (player_choose == "rock") else declare_result("win")
    elif computer_choose == "scissors":
        declare_result("lose") if (player_choose == "paper") else declare_result("win")


# continuous running of game using infinite loop and functions
while True:
    want_to_play = ask_to_play()
    if want_to_play == False:
        break
    else:
        clear()
        print(logo)
        computer_choose = random.choice(options)
        player_choose = player_choosing()
        check_results(computer_choose, player_choose)
