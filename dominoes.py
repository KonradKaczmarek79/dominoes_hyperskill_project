import random
from game_interface import GameInterface

def prepare_stock_pieces_init():
    stock_pieces_result = []
    for i in range(7):
        for j in range(7):
            temp_list = [i, j]
            random.shuffle(temp_list)
            if temp_list not in stock_pieces_result and temp_list[::-1] not in stock_pieces_result:
                stock_pieces_result.append(temp_list)

    random.shuffle(stock_pieces_result)

    return stock_pieces_result


def draw_dominoes(all_pieces: list, how_many=7):
    result = []
    for x in range(how_many):
        index = random.randint(0, len(all_pieces)-1)
        result.append(all_pieces.pop(index))

    return result


def is_required_piece_in_list(list_to_check:list) -> bool:
    if [5, 5] in list_to_check:
        return True
    elif [6, 6] in list_to_check:
        return True
    else:
        return False


def add_domino_to_snake_init(player: list, sub_list: list, snake: list):
    index = player.index(sub_list)
    value = player.pop(index)
    snake.append(value)


def check_who_starts(computer_list: list, user_list: list, snake: list) -> str:
    if [6, 6] in computer_list:
        add_domino_to_snake_init(computer_list, [6, 6], snake)
        return "computer"
    elif [6, 6] in user_list:
        add_domino_to_snake_init(user_list, [6, 6], snake)
        return "player"
    elif [5, 5] in computer_list:
        add_domino_to_snake_init(computer_list, [5, 5], snake)
        return "computer"
    elif [5, 5] in user_list:
        add_domino_to_snake_init(user_list, [5, 5], snake)
        return "player"
    return ""


def make_str_with_player_domino(user_list: list) -> str:
    temp_str = ""
    for num, value in enumerate(user_list):
        temp_str += f"{num + 1}:{value}\n"

    return temp_str


next_status = {
    "computer": ("player", "Status: It's your turn to make a move. Enter your command."),
    "player": ("computer",  "Status: Computer is about to make a move. Press Enter to continue..."),
}


stock_pieces = prepare_stock_pieces_init()
computer = []
user = []
domino_snake = []
who_begins = None


while not who_begins:
    stock_pieces += computer
    stock_pieces += user
    computer = draw_dominoes(stock_pieces)
    user = draw_dominoes(stock_pieces)

    who_begins = check_who_starts(computer, user, domino_snake)

status = next_status[who_begins][0]

# print(f"Stock pieces: {stock_pieces}")
# print(f"Computer pieces: {computer}")
# print(f"Player pieces: {user}")
# print(f"Domino snake: {domino_snake}")
# print(f"Status: {status}")

print(GameInterface(len(stock_pieces), len(computer), domino_snake, make_str_with_player_domino(user)).__str__())
print(next_status[who_begins][1])