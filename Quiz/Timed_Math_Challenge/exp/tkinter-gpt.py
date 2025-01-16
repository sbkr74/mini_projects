import tkinter as tk
import random
import threading
import time

# Constants
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 10
TOTAL_QUESTIONS = 30

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz with Timer")

        # Initialize variables
        self.current_question = 0
        self.attempts = 0
        self.timer_seconds = 10
        self.stop_event = threading.Event()

        # UI Components
        self.label_instruction = tk.Label(root, text="Press Start to Begin!", font=("Arial", 16))
        self.label_instruction.pack(pady=10)

        self.label_question = tk.Label(root, text="", font=("Arial", 18))
        self.label_question.pack(pady=10)

        self.entry_answer = tk.Entry(root, font=("Arial", 14))
        self.entry_answer.pack(pady=10)
        self.entry_answer.bind("<Return>", self.check_answer)

        self.label_timer = tk.Label(root, text="Time Left: 00:00", font=("Arial", 16))
        self.label_timer.pack(pady=10)

        self.label_result = tk.Label(root, text="", font=("Arial", 14), fg="green")
        self.label_result.pack(pady=10)

        self.button_start = tk.Button(root, text="Start", command=self.start_quiz, font=("Arial", 14))
        self.button_start.pack(pady=20)

    def generate_problem(self):
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        operator = random.choice(OPERATORS)
        expr = f"{left} {operator} {right}"
        answer = eval(expr)
        return expr, answer

    def start_timer(self):
        self.timer_seconds = 30
        self.stop_event.clear()
        threading.Thread(target=self.update_timer).start()

    def update_timer(self):
        while self.timer_seconds > 0 and not self.stop_event.is_set():
            mins, secs = divmod(self.timer_seconds, 60)
            self.label_timer.config(text=f"Time Left: {mins:02d}:{secs:02d}")
            time.sleep(1)
            self.timer_seconds -= 1

        if not self.stop_event.is_set():
            self.label_timer.config(text="Time's up!")
            self.show_result(False)

    def start_quiz(self):
        self.current_question = 0
        self.attempts = 0
        self.next_question()

    def next_question(self):
        if self.current_question < TOTAL_QUESTIONS:
            self.current_question += 1
            self.expr, self.answer = self.generate_problem()
            self.label_question.config(text=f"Question #{self.current_question}: {self.expr} = ?")
            self.label_result.config(text="")
            self.entry_answer.delete(0, tk.END)
            self.start_timer()
        else:
            self.end_quiz()

    def check_answer(self, event=None):
        user_input = self.entry_answer.get().strip()
        if user_input == str(self.answer):
            self.attempts += 1
            self.stop_event.set()
            self.label_result.config(text="Correct!", fg="green")
            self.next_question()
        else:
            self.label_result.config(text="Incorrect. Try again!", fg="red")

    def show_result(self, success):
        if success:
            self.label_result.config(text="Correct!", fg="green")
        else:
            self.label_result.config(text=f"Time's up! Correct answer was {self.answer}", fg="red")
        self.next_question()

    def end_quiz(self):
        total_time = round(time.time() - self.start_time, 2)
        self.label_instruction.config(
            text=f"Quiz Completed! {self.attempts}/{TOTAL_QUESTIONS} questions answered correctly in {total_time} seconds.")
        self.label_question.config(text="")
        self.label_timer.config(text="")
        self.entry_answer.pack_forget()
        self.button_start.config(text="Restart", command=self.start_quiz)

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
