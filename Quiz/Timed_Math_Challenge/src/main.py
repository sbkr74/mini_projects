import random
import time
import threading

# NOTE: UPPERCASE VAR NAME IS USED FOR CONSTANT
OPERATOR = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 10
TOTAL_QUEST = 30

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATOR)
    expr = str(left) + operator + str(right)
    answer = eval(expr)
    return expr,answer

def countdown_timer(seconds, stop_event):
    while seconds and not stop_event.is_set():
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Pause for 1 second
        seconds -= 1

    if not stop_event.is_set():
        print("\nTime's up!")

attempt = 1
input("Press Enter to start!")
print("-------------------------------")
start_time = time.time()

for i in range(TOTAL_QUEST):
    expr,ans = generate_problem()
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=countdown_timer, args=(10, stop_event))
    timer_thread.start()

    usr_in = None
    while not stop_event.is_set():
        usr_in = input("\t Question#" + str(i+1) + ": " + expr + "= ")
        if usr_in.strip() == str(ans):
            stop_event.set()  # Stop the timer thread
            break

    timer_thread.join()  # Wait for the timer thread to finish
    if not usr_in or not stop_event.is_set():  # If the timer ran out
        print(f"\nYou ran out of time! The correct answer was {ans}.")
        break

    attempt += 1

end_time = time.time()
total_time = round(end_time-start_time,2)
print("-------------------------------")   
print(f"Nice Work! you have completed in {attempt} attempt in {total_time} seconds.")