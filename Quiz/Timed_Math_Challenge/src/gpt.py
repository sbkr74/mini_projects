import random
import time
import threading

# Constants
OPERATOR = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 10
TOTAL_QUEST = 30

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)
    expr = str(left) + operator + str(right)
    answer = eval(expr)
    return expr, answer

def countdown_timer(seconds, stop_event):
    while seconds and not stop_event.is_set():
        mins, secs = divmod(seconds, 60)
        print(f"Timer: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    if not stop_event.is_set():
        print("\nTime's up!")

# Main program
attempt = 0
input("Press Enter to start!")
print("-------------------------------")
start_time = time.time()

for i in range(TOTAL_QUEST):
    expr, ans = generate_problem()
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=countdown_timer, args=(10, stop_event))
    timer_thread.start()

    usr_in = None
    time_up = False

    while not stop_event.is_set():
        print(f"Question#{i+1}: {expr}=")  # Display question on a separate line
        usr_in = input()
        if usr_in.strip() == str(ans):
            stop_event.set()  # Stop the timer thread
            break
        else:
            print("Incorrect answer, try again!")

    if not stop_event.is_set():  # If the timer ends
        time_up = True
        stop_event.set()

    timer_thread.join()  # Wait for the timer thread to finish

    if time_up:
        print(f"\nTime's up! The correct answer was {ans}.\n")
    else:
        print("Correct!\n")

    attempt += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("-------------------------------")
print(f"Nice Work! You completed in {attempt} attempts in {total_time} seconds.")
