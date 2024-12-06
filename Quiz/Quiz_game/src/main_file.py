import os
from main import Quiz
file_path = os.path.join("Quiz","Quiz_game","files","set1.txt")

with open(file_path,"r") as file:
    content = file.readlines()
    
ques_dict = {}
options_dict = {}

for line in content:
    if ":" in line:
        key,value = line.split(":",1)
        key = key.strip()
        value = value.strip()
        ques_dict[key]=value
    elif "." in line:
        opt,val = line.split(".",1)
        opt = opt.strip()
        val = val.strip()
        options_dict[opt]=val
        ques_dict['Options']=options_dict
ques_list = [ques_dict]
score = 0
for quest in ques_list:
    print(quest["Question"])
    for opt,val in quest["Options"].items():
        print(opt,val)
    choice = input("Enter Your Choice: (A,B,C or D):-> ").upper()
    if choice == quest["Answer"][0]:
        print("Hooray! Correct Answer...")
        score+=1
    else:
        print("Looser!!! Wrong Answer. Correct answer: ",quest["Answer"])
    print("Final Score:",score)
