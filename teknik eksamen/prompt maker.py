import random

dice_number = {1,2,3,4,5,6}
dice_operators = {"+","-","*","/"}

game_mode = input("Bestem Game Mode: ")

print(game_mode)

def generate_prompt():
    if game_mode == "any":
        print ("any operator allowed")
        # prompt = 
    elif game_mode == "plus_minus":
        print("only plus and minus")
        prompt[1] = dice_operators[random(0,1)]
    elif game_mode == "div_mul":
        print("only division and multiplication")
        prompt[1] = dice_operators[random(2,3)]
    elif game_mode == "random":
        print("choosing operator at random")
        prompt[1] = dice_operators[random(0,3)]

def calculate_prompt(prompt):
    if prompt[1] == dice_operators[0]:
        result = prompt[0] + prompt[2]
        return result
    elif prompt[1] == dice_operators[1]:
        result = prompt[0] - prompt[2]
        return result
    elif prompt[1] == dice_operators[2]:
        result = prompt[0] * prompt[2]
        return result
    elif prompt[1] == dice_operators[3]:
        result = prompt[0] / prompt[2]
        return result