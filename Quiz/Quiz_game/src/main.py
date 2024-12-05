class Quiz:
    questions = [
        {
            "prompt": '''1. Fill the missing numbers in the magic square so that the sum of every row, column, and diagonal equals 15
            _   9   2
            7   _   6
            4   3   _''',
            "options": ["A. 5, 8, 1","B. 6, 5, 4","C. 8, 5, 1","D. 4, 7, 6"],
            "answer": "C"
        },
        {
            "prompt":"2. I am a three-digit number.\n\tMy tens digit is five more than my ones digit.\n\tMy hundreds digit is eight less than my tens digit.\nWhat number am I",
            "options": ["A. 152","B. 194","C. 370","D. 283"],
            "answer":"A"
        },
        {
            "prompt":"3. Which one of the following does not belong?",
            "options":["A. Dog","B. Cat","C. Fish","D. Elephant"],
            "answer":"C"
        },
        {
            "prompt":"4. Which number should replace the question mark?\n\t3, 9, 27, ?, 243",
            "options":["A. 54","B. 81","C. 108","D. 72"],
            "answer":"B"
        },
        {
            "prompt":"5. Which one of the following numbers is the odd one out?",
            "options":["A. 7","B. 11","C. 15","D. 17"],
            "answer":"C"
        }
    ]
    def run_quiz(self,questions):
        score = 0
        for question in questions:
            print("\n==============================================================================================")
            print(question["prompt"])
            print("---------------------------------------")
            for option in question["options"]:
                print(option)
            choice = input("Enter Your Choice: (A,B,C or D):-> ").upper()
            if choice == question["answer"]:
                print("Hooray! Correct Answer...")
                score+=1
            else:
                print("Looser!!! Wrong Answer. Correct answer: ",question["answer"])
        print("Final Score:",score)
if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz(Quiz.questions)
