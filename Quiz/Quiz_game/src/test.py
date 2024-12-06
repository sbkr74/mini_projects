import os

file_path = os.path.join("Quiz", "Quiz_game", "files", "set1.txt")

with open(file_path, "r") as file:
    content = file.readlines()

# Initialize variables
questions_list = []  # List to store all questions
ques_dict = {}  # Dictionary to store a single question
options_dict = {}  # Dictionary to store options
current_question = ""  # To handle multi-line questions
is_question = False  # Flag to track question parsing

for line in content:
    line = line.strip()  # Remove leading/trailing whitespace

    if ":" in line and not line.startswith("Answer"):
        # If a new question starts, save the previous question
        if ques_dict:
            ques_dict["Options"] = options_dict  # Add options to the question
            questions_list.append(ques_dict)  # Append the current question to the list
            ques_dict = {}  # Reset for the next question
            options_dict = {}  # Reset options for the next question

        # Start a new question
        is_question = True
        key, value = line.split(":", 1)
        current_question = value.strip()  # Initialize the question text

    elif is_question and not (line.startswith("A.") or line.startswith("Answer")):
        # Append to the current question if it's a continuation
        current_question += "\n" + line.strip()  # Keep the line breaks

    elif line.startswith("A.") or line.startswith("B.") or line.startswith("C.") or line.startswith("D."):
        # Finalize the question before processing options
        if is_question:
            ques_dict["Question"] = current_question  # Store the multi-line question
            is_question = False

        # Add options to the options dictionary
        opt, val = line.split(".", 1)
        options_dict[opt.strip()] = val.strip()

    elif line.startswith("Answer"):
        # Extract the answer
        _, answer = line.split(":", 1)
        ques_dict["Answer"] = answer.strip()

# Add the last question to the list (if it exists)
if ques_dict:
    ques_dict["Options"] = options_dict
    questions_list.append(ques_dict)

# Print the resulting list of questions
for question in questions_list:
    print(f"Question: {question['Question']}")
    for option, value in question["Options"].items():
        print(f"{option}. {value}")
    print(f"Answer: {question['Answer']}")
    print("\n" + "-"*50)  # Separate questions with a line
