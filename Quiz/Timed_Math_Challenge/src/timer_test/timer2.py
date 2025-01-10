import threading
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"\r{timer} ", end="", flush=True)  # Print on the same line
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")  # Notify when time is up

def get_user_input(prompt):
    user_input = input(prompt)
    print(f"\nYou entered: {user_input}")

# Number of seconds for the countdown
timer_seconds = 10

# Input question setup
question_number = 1
expression = "5 + 3"  # Example expression

# Create threads for the countdown and user input
timer_thread = threading.Thread(target=countdown_timer, args=(timer_seconds,))
input_thread = threading.Thread(target=get_user_input, args=(f"Question#{question_number}: {expression} = ",))

# Start both threads
timer_thread.start()
input_thread.start()

# Wait for both threads to finish
timer_thread.join()
input_thread.join()
