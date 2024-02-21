logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""



easy_level = 10
hard_level = 5

answer = 0

def check_ans(guess, answer, turn):
    if guess > answer:
        print("to high")
        return turn - 1
    elif guess < answer:
        print("too low")
        return turn - 1
    else:
         print("you got it")

def set_difficulty():
    level = int(input("Enter the level"))
    if level == "easy":
        return easy_level
    else:
        return hard_level


def game():
    print(logo)
    answer = randint(1, 100)
    print(answer)
              
    turn= set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turn} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turn = check_answer(guess, answer, turn)
    if turn == 0:
       print("You've run out of guesses, you lose.")
       return
    elif guess != answer:
       print("Guess again.")


game()

