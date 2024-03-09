import random

def get_level():
    while True:
        level = input("Enter the level (1, 2, or 3): ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Please enter 1, 2, or 3.")

def generate_problem(level):
    x = random.randint(0, 10 ** level - 1)
    y = random.randint(0, 10 ** level - 1)
    return x, y, x + y

def solve_problem(x, y, answer):
    for _ in range(3):
        try:
            guess = int(input(f"What is {x} + {y}? "))
            if guess == answer:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"The correct answer is {answer}.")
    return False

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y, answer = generate_problem(level)
        if solve_problem(x, y, answer):
            score += 1

    print(f"Your score is {score}/10.")

if __name__ == "__main__":
    main()
