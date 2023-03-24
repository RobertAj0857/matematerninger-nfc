

dice_number = {1,2,3,4,5,6}
dice_operators = {"+","-","*","/"}

game_mode = "all"

def generate_prompt():
    if game_mode == "any":
        print ("any operator allowed")
        prompt = 
    elif game_mode == "plus_minus":
        print("only plus and minus")
    elif game_mode == "div_mul":
        print("only division and multiplication")
    elif game_mode == "random":
        print("choosing operator at random")

def calculate_prompt(prompt):
    if prompt[1] == "+":
        result = prompt[0] + prompt[2]
        return result
    elif prompt[1] == "-":
        result = prompt[0] - prompt[2]
        return result
    elif prompt[1] == "*":
        result = prompt[0] * prompt[2]
        return result
    elif prompt[1] == "/":
        result = prompt[0] / prompt[2]
        return result