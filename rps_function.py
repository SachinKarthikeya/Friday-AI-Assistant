import pyttsx3
import random

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def play_game():
    speak("I am always ready Boss. Let us play!!")
    human_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        speak("Boss, choose Rock, Paper, Scissors or quit.")
        human_choice = input('Choose Rock, Paper, Scissors or quit: ').lower()
        if human_choice == 'quit':
            speak("Okay Boss, see you next time.")
            break

        if human_choice not in choices:
            speak("Boss, it is an invalid choice! Please choose Rock, Paper, or Scissors.")
            print("Boss, it is an invalid choice! Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.randint(0, 2)  # 0: rock, 1: paper, 2: scissors
        computer_pick = choices[computer_choice]
        speak(f"Boss, I have chosen {computer_pick}.")
        print(f'Boss, I have chosen {computer_pick}.')

        if human_choice == 'rock' and computer_pick == 'scissors':
            speak("Excellent choice Boss!! You win this round.")
            print('Excellent choice Boss!! You win this round.')
            human_score += 1
            continue
        if human_choice == 'paper' and computer_pick == 'rock':
            speak("Excellent choice Boss!! You win this round.")
            print('Excellent choice Boss!! You win this round.')
            human_score += 1
            continue
        if human_choice == 'scissors' and computer_pick == 'paper':
            speak("Excellent choice Boss!! You win this round.")
            print('Excellent choice Boss!! You win this round.')
            human_score += 1
            continue
        if human_choice == computer_pick:
            speak("It's a tie Boss!")
            print("It's a tie Boss!")
            continue
        else:
            speak("Bad choice Boss!! I win this round.")
            print('Bad choice Boss!! I win this round.')
            computer_score += 1

    
    speak(f"Boss, You've won {human_score} times. I won {computer_score} times.")
    print(f"Boss, You've won {human_score} times. I won {computer_score} times")

    if human_score > computer_score:
        speak("Congratulations Boss! Well played!!.")
        print("Congratulations Boss! Well played!!.")
    elif human_score == computer_score:
        speak("It's a tie Boss!!")
        print("It's a tie Boss!!")
    else:
        speak("Nice try Boss. Better luck next time.")
        print("Nice try Boss. Better luck next time.")
    speak("Adios Boss!")
    print("Adios Boss!")