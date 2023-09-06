# flashcards.py
# import file
import json

# read json file
def read_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        return data
    
# checks whether input is correct or incorrect
def check_answer(r_answer, input):
    global score
    # case sensitivity
    if r_answer.lower() == input.lower():
        score += 1
        return True
    else:
        return False

# message display
def display_message(checked_answer, r_answer):
    if checked_answer:
        print(f"Correct! Your current score is {score}/{total}")
    else:
        print("Incorrect! The correct answer was", r_answer)
        print(f"Current score: {score}/{total}")
    
def full_results(score, total):
    if score == total:
        print(f"Amazing!! You scored: {score} out of {total} correct!")
    elif score < total / 2:
        print(f"You scored {score} out of {total} correct! You need to study! ")
    else:
        print(f"Good work! You scored {score} out of {total} correct!")

# display starting and ending message
def end_msg():
    if game_initialized:
        print(f"Welcome to Guess the Capitals! Can you correctly guess each one? Let's play!")
    else:
        print(f"Thank you for playing!")

def Guess_the_Capitals():
    global score, total, game_initialized 
    data = read_json('me-capitals.json')  
    game_initialized = True  
    total = len(data["cards"])
    score = 0

    end_msg()
    for i in data["cards"]:
        guess = input(i["q"] + " > ")
        checked_answer = check_answer(i['a'], guess)
        display_message(checked_answer, i['a'])

    full_results(score, total)
    game_load = False
    end_msg()

# run the gmae.
Guess_the_Capitals()