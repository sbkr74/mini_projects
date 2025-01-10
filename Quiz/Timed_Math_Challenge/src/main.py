import random
import time

# NOTE: UPPERCASE VAR NAME IS USED FOR CONSTANT
OPERATOR = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 20
TOTAL_QUEST = 10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATOR)
    expr = str(left) + operator + str(right)
    answer = eval(expr)
    return expr,answer

attempt = 1
input("Press Enter to start!")
print("-------------------------------")
start_time = time.time()
for i in range(TOTAL_QUEST):
    expr,ans = generate_problem()

    while True:
        usr_in = input("Question#"+str(i+1)+": "+expr+"= ")
        if usr_in==str(ans):
            break
        attempt+=1
end_time = time.time()
total_time = round(end_time-start_time,2)
print("-------------------------------")   
print(f"Nice Work! you have completed in {attempt} attempt in {total_time} seconds.")