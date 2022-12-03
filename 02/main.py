from enum import Enum

class Options(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
class Outcomes(Enum):
    WIN = 1
    DRAW = 2
    LOSS = 3
    
option_score = {
    Options.ROCK: 1,
    Options.PAPER: 2,
    Options.SCISSORS: 3
}

opponent_options = {
    'A': Options.ROCK,
    'B': Options.PAPER,
    'C': Options.SCISSORS
}

my_options = {
    'X': Options.ROCK,
    'Y': Options.PAPER,
    'Z': Options.SCISSORS
}

option_outcome = {
    'X': Outcomes.LOSS,
    'Y': Outcomes.DRAW,
    'Z': Outcomes.WIN
}


def calculate_score(option):
    match option:
        case Options.ROCK:
            if (opponent_option == Options.PAPER):
                return loss
            elif (opponent_option == Options.ROCK):
                return draw
            else:
                return win
        case Options.PAPER:
            if (opponent_option == Options.SCISSORS):
                return loss
            elif (opponent_option == Options.PAPER):
                return draw
            else:
                return win
        case Options.SCISSORS:
            if (opponent_option == Options.ROCK):
                return loss
            elif (opponent_option == Options.SCISSORS):
                return draw
            else:
                return win
                


win = 6
draw = 3
loss = 0

file = open("./02/input.txt", "r")

lines = file.readlines()

total_score = 0

for line in lines:
    round = line.split(" ")
    opponent_option = opponent_options[round[0].replace("\n", "")]
    
    # my_option = my_options[round[1].replace("\n", "")]
    # total_score = total_score + option_score[my_option] + calculate_score(my_option)
    
    outcome = option_outcome[round[1].replace("\n", "")]
    my_option = Options.PAPER
    
    match (opponent_option):
        case Options.ROCK:
            if (outcome == Outcomes.WIN):
                my_option = Options.PAPER
            elif (outcome == Outcomes.LOSS):
                my_option = Options.SCISSORS
            else:
                my_option = Options.ROCK
        case Options.PAPER:
            if (outcome == Outcomes.WIN):
                my_option = Options.SCISSORS
            elif (outcome == Outcomes.LOSS):
                my_option = Options.ROCK
            else:
                my_option = Options.PAPER
        case Options.SCISSORS:
            if (outcome == Outcomes.WIN):
                my_option = Options.ROCK
            elif (outcome == Outcomes.LOSS):
                my_option = Options.PAPER
            else:
                my_option = Options.SCISSORS
    
    round_choice = option_score[my_option]
    round_score = calculate_score(my_option)
    total_score = total_score + round_choice + round_score
    
print(total_score)