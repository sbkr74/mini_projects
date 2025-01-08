import random
import json

with open(r"story_teller\files\story.txt","r") as f:
    story = f.read()

chr_start = "["
chr_end = "]"
start_word = -1
words = set()
for i,char in enumerate(story):
    if char == chr_start:
        start_word = i

    if char == chr_end and start_word != -1:
        word = story[start_word: i+1]
        words.add(word)
        start_word = -1

with open(r"story_teller\files\words.json","r") as file:
    answers = json.load(file)
    
for word in words:
    word_rep = word.replace("[","").replace("]","")
    story = story.replace(word,random.choice(answers[word_rep]))

print(story)