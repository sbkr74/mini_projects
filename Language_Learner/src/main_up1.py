import random
words = [
    {"eng": "happy", "adv": "joyful"},
    {"eng": "sad", "adv": "sorrowful"},
    {"eng": "angry", "adv": "irate"},
    {"eng": "big", "adv": "large"},
    {"eng": "small", "adv": "tiny"},
    {"eng": "beautiful", "adv": "lovely"},
    {"eng": "ugly", "adv": "unattractive"},
    {"eng": "good", "adv": "great"},
    {"eng": "bad", "adv": "terrible"},
    {"eng": "smart", "adv": "intelligent"},
    {"eng": "stupid", "adv": "foolish"},
    {"eng": "strong", "adv": "powerful"},
    {"eng": "weak", "adv": "frail"},
    {"eng": "fast", "adv": "quick"},
    {"eng": "slow", "adv": "sluggish"},
    {"eng": "hot", "adv": "warm"},
    {"eng": "cold", "adv": "chilly"},
    {"eng": "rich", "adv": "wealthy"},
    {"eng": "poor", "adv": "destitute"},
    {"eng": "old", "adv": "aged"},
    {"eng": "young", "adv": "youthful"},
    {"eng": "bright", "adv": "luminous"},
    {"eng": "dark", "adv": "dim"},
    {"eng": "easy", "adv": "simple"},
    {"eng": "hard", "adv": "difficult"},
    {"eng": "clean", "adv": "spotless"},
    {"eng": "dirty", "adv": "grimy"},
    {"eng": "kind", "adv": "generous"},
    {"eng": "mean", "adv": "cruel"},
    {"eng": "friendly", "adv": "cordial"}
]
def main(words):
    random.shuffle(words)
    score = 0
    count = 0
    for word in words:
        count+=1
        correct_answer = word['adv']
        print(f"What is Synonyms for {word['eng']} ?")
        user_answer = input("Your Answer: ")
        if user_answer == correct_answer:
            print("Correct\n")
            score+=1
        elif count>10:
            print("Score:",score)
            break
        else:
            print(f"Wrong Answer Idiot! \'{correct_answer}\' is correct answer.\n")

main(words)