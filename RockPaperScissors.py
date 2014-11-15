from random import randint

def user_moves():
    user_legit = false
    while user_legit = false
    user_move = input ("What is your move?")
    if user_move == "rock" or user_move == "paper" or user_move == "scissors":
        user_legit = true
    else:
        user_legit = false
def cpu_moves():
    cpu_num = randint(1,3)
    cpu_move = None
    if cpu_num == 1:
        cpu_move = "rock"
    elif cpu_num == 2:
        cpu_move = "paper"
    elif cpu_num == 3:
        cpu_move = "scissors"
