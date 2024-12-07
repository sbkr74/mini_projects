import os
file_path = os.path.join("Quiz","Quiz_game","files","set1.txt")

with open(file_path,"r") as file:
    content = file.readlines()
    
ques_dict = {}
options_dict = {}
ques_list = []
for line in content:
    if ":" in line and not line.startswith("Answer"):
        if ques_dict:
            ques_list.append(ques_dict)
            ques_dict= {}
            options_dict = {}
        key,value = line.split(":",1)
        key = key.strip()
        value = value.strip()
        ques_dict["Question"]=value  

    elif line.startswith("Answer"):
        _,answer = line.split(":",1)
        answer = answer.strip()
        ques_dict["Answer"] = answer

    elif "." in line:
        opt,val = line.split(".",1)
        opt = opt.strip()
        val = val.strip()
        options_dict[opt]=val
        ques_dict['Options']=options_dict
       
    
if ques_dict:
    ques_list.append(ques_dict)

score = 0
total = 0
for quest in ques_list:
    total+=1
    print(quest["Question"])
    for opt,val in quest["Options"].items():
        print(opt,val)
    choice = input("Enter Your Choice: (A,B,C or D):-> ").upper()
    if choice == quest["Answer"][0]:
        print("Hooray! Correct Answer...\n")
        score+=1
    else:
        print("Looser!!! Wrong Answer. Correct answer: ",quest["Answer"],"\n")
print("Final Score:",score,"/",total)
