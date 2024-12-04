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
            "prompt":'''I am a three-digit number.
            []My tens digit is five more than my ones digit.
            []My hundreds digit is eight less than my tens digit.
            What number am I?''',
            "options": ["A. 152","B. 194","C. 370","D. 283"],
            "answer":"A"
        }
    ]
    @staticmethod
    def run_quiz(questions):
        score = 0
        for question in questions:
            print("==============================================================================================")
            print(question["prompt"])
            print("---------------------------------------")
            for option in question["options"]:
                print(option)
            choice = input("Enter Your Choice: ")
            if choice.upper() == question["answer"]:
                score+=1
        print("Final Score:",score)

quiz = Quiz()
quiz.run_quiz(Quiz.questions)
