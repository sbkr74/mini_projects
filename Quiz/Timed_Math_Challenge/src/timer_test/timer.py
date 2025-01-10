import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
        print(seconds)

    print("Time's up!")

# Example: Countdown from 10 seconds
countdown_timer(10)
