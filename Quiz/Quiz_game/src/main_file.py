import os

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

        if key.startswith(('A','B','C','D')):
            options_dict[key]=value
        else:
            if options_dict:
                ques_dict['Options']=options_dict
                options_dict = {}
            ques_dict[key]=value
    elif line.strip():
        if options_dict:
            ques_dict['Options']=options_dict
            options_dict = {}
if options_dict:
    ques_dict["Options"]=options_dict
print(ques_dict)