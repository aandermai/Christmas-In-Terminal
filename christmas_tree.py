import os
import time
import random

COLORS = {
    1: "\033[32m{}\033[32m", # green
    2: "\033[31m{}\033[32m", # red
    3: "\033[34m{}\033[32m", # blue
    4: "\033[33m{}\033[32m", # yellow
    }

def draw_tree(height: int) -> list[str]:
    tree_lines = []

    for i in range(1, height, 2):
        spaces = " " * height
        stars = "*" * i
        tree_lines.append(spaces + COLORS[1].format(stars))
        height -= 1

    return tree_lines

def add_decorations_to_tree(height: int) -> list[str]:
    decorations = ["@", "0", "%"]
    tree_lines = draw_tree(height)
    decorated_tree = []

    for line in tree_lines:
        chars = list(line)

        for i in range(len(chars)):
            if chars[i] == "*" and random.random() < 0.25:
                chars[i] = (COLORS[random.randint(2, 4)].format(random.choice(decorations)))
                
        decorated_tree.append("".join(chars))

    return decorated_tree

def make_tree_with_phrase(height: int, phrase: str) -> list[str]:
    tree = add_decorations_to_tree(height)
    average = len(tree) // 2

    tree[average] += "     "
    tree[average] += '\033[3m' + COLORS[random.randint(2, 4)].format(phrase)

    return tree

if __name__ == "__main__":
    height = int(input("Введите высоту ёлочки: "))
    phrase = "HAPPY NEW YEAR!"

    while True:
        print('\n\n')
        tree = make_tree_with_phrase(height, phrase)
        
        for line in tree:
            print(line)

        print('\n\n')

        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')