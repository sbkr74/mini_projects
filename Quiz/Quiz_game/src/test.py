import os

file_path = os.path.join("Quiz", "Quiz_game", "files", "set1.txt")

with open(file_path, "r") as file:
    content = file.readlines()

# Initialize variables
questions_list = []  # List to store all questions
ques_dict = {}  # Dictionary to store a single question
options_dict = {}  # Dictionary to store options

for line in content:
    line = line.strip()  # Remove leading/trailing whitespace

    if ":" in line and not line.startswith("Answer"):
        # If a new question starts, save the previous question
        if ques_dict:
            ques_dict["Options"] = options_dict  # Add options to the question
            questions_list.append(ques_dict)  # Append the current question to the list
            ques_dict = {}  # Reset for the next question
            options_dict = {}  # Reset options for the next question

        # Extract question
        key, value = line.split(":", 1)
        ques_dict["Question"] = value.strip()
    
    elif line.startswith("Answer"):
        _,answer = line.split(":",1)
        answer = answer.strip()
        ques_dict["Answer"] = answer
        
    elif "." in line:
        # Add options to the options dictionary
        opt, val = line.split(".", 1)
        options_dict[opt.strip()] = val.strip()
    

    

# Add the last question to the list (if it exists)
if ques_dict:
    ques_dict["Options"] = options_dict
    questions_list.append(ques_dict)

# Print the resulting list of questions
print(questions_list)
