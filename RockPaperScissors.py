from random import randint

user_move = None
cpu_move = None
def user_moves(user_move):
    user_legit = False
    while user_legit == False:
        user_move = input ("What is your move?")
        if user_move == "rock" or user_move == "paper" or user_move == "scissors":
            user_legit = True
        else:
            user_legit = False
def cpu_moves(cpu_move):
    cpu_num = randint(1,3)
    if cpu_num == 1:
        cpu_move = "rock"
    elif cpu_num == 2:
        cpu_move = "paper"
    elif cpu_num == 3:
        cpu_move = "scissors"
game = True
legit = False
while game:
    while legit == False:
        user_moves()
        cpu_moves()
        print (user_move)
        print (cpu_move)
        if user_moves == cpu_moves:
            pass
