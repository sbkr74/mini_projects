import threading
import time

def countdown_timer(seconds, stop_event):
    print()
    while seconds and not stop_event.is_set():
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"\r{timer} ", end="", flush=True)  # Print on the same line
        time.sleep(1)
        seconds -= 1
    if not stop_event.is_set():
        print("\nTime's up!")  # Notify when time is up
    stop_event.set()  # Signal to stop the program

def get_user_input(prompt, stop_event):
    if not stop_event.is_set():
        user_input = input(prompt)
        if not stop_event.is_set():  # Check if timer hasn't already stopped the program
            print(f"\nYou entered: {user_input}")
        stop_event.set()  # Signal to stop the program

# Shared stop event
stop_event = threading.Event()

# Number of seconds for the countdown
timer_seconds = 10

# Input question setup
question_number = 1
expression = "5 + 3"  # Example expression

# Create threads for the countdown and user input
input_thread = threading.Thread(target=get_user_input, args=(f"Question#{question_number}: {expression} = ", stop_event))
timer_thread = threading.Thread(target=countdown_timer, args=(timer_seconds, stop_event))


# Start both threads
input_thread.start()
time.sleep(1)
timer_thread.start()


# Wait for both threads to finish
timer_thread.join()
input_thread.join()
