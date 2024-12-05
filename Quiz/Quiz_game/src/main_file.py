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
        ques_dict[key]=value
    elif "." in line:
        opt,val = line.split(".",1)
        opt = opt.strip()
        val = val.strip()
        options_dict[opt]=val
        ques_dict['Options']=options_dict

