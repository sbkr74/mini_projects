import time
import random
import threading
import os

def display_solution_and_next_question(question, solution):
    print(f"Time's up! The solution to '{question}' is {solution}.")
    print("Moving to the next question...\n")

def ask_question(question, solution, timer=15):
    answered = threading.Event()

    def timer_function():
        for remaining in range(timer, 0, -1):
            if answered.is_set():
                return
            print(f"\rTime remaining: {remaining}s  ", end=" ")
            time.sleep(1)
        if not answered.is_set():
            display_solution_and_next_question(question, solution)

    timer_thread = threading.Thread(target=timer_function)
    timer_thread.start()

    try:
        print(f"Solve this: {question} = ")  # Display question without overlapping input
        answer = input()  # Take input on a new line
        answered.set()  # Stop the timer if the user answers

        if answer.strip() == str(solution):
            print("Correct!\n")
        else:
            print(f"Wrong. The correct answer is {solution}.\n")
    except Exception as e:
        print(f"An error occurred: {e}")

    timer_thread.join()  # Ensure the timer thread finishes

def main():
    print("Welcome to the Math Quiz Game!")
    print("You have 15 seconds to answer each question. If you run out of time, the solution will be shown.\n")

    questions = [
        ("5 + 7", 12),
        ("12 - 8", 4),
        ("9 * 3", 27),
        ("16 / 4", 4),
        ("7 + 6 * 2", 19),
        ("(8 + 2) * 3", 30),
        ("25 - (3 + 7)", 15),
        ("36 / (2 * 3)", 6)
    ]

    random.shuffle(questions)  # Randomize question order

    for question, solution in questions:
        ask_question(question, solution)

    print("Game over! Thanks for playing.")

if __name__ == "__main__":
    main()
