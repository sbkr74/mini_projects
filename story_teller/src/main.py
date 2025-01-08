import random
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

answers = {"adjective": ("daring", "sunny", "foggy", "thrilling", "unforgettable"),
        "terrain": ("forest", "canyon", "mountain"),
        "weather condition": ("drizzle", "gusty winds", "clear skies", "rainy"),
        "adventurous activity": ("trekking", "rafting", "ziplining", "skydiving","paragliding", "bungee jumping", "mountain climbing"),
        "gear": ("rope", "helmet", "raft","Ice Axe"),
        "noun": ("waterfall", "cliff","valley"),
        "plural noun": ("backpack","gears","suits","attachemnts"),
        "name of person 1": ("Shubham","Sumit","Aman"),
        "name of person 2": ("Biruly","Himanshu","Prince"),
        "name of person 3": ("Bittu","Suman","chunnu","krishna"),
        "emotion": ("excited", "nervous", "accomplished","excited","exhaustion")
        }

# Function to get a random value from a specific key
def get_random_value(key):
    if key in answers:
        return random.choice(answers[key])
    else:
        return f"Key '{key}' not found in the dictionary."
    
for word in words:
    word_rep = word.replace("[","").replace("]","")
    story = story.replace(word,get_random_value(word_rep))

print(story)