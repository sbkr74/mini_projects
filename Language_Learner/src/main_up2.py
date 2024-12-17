import random

# Your provided list of dictionaries with an added "occurrence" field
adjectives_synonyms = [
    {"english": "happy", "advanced_english": "joyful", "occurrence": 0},
    {"english": "sad", "advanced_english": "sorrowful", "occurrence": 0},
    {"english": "angry", "advanced_english": "irate", "occurrence": 0},
    {"english": "big", "advanced_english": "large", "occurrence": 0},
    {"english": "small", "advanced_english": "tiny", "occurrence": 0},
    {"english": "beautiful", "advanced_english": "lovely", "occurrence": 0},
    {"english": "ugly", "advanced_english": "unattractive", "occurrence": 0},
    {"english": "good", "advanced_english": "great", "occurrence": 0},
    {"english": "bad", "advanced_english": "terrible", "occurrence": 0},
    {"english": "smart", "advanced_english": "intelligent", "occurrence": 0},
    {"english": "stupid", "advanced_english": "foolish", "occurrence": 0},
    {"english": "strong", "advanced_english": "powerful", "occurrence": 0},
    {"english": "weak", "advanced_english": "frail", "occurrence": 0},
    {"english": "fast", "advanced_english": "quick", "occurrence": 0},
    {"english": "slow", "advanced_english": "sluggish", "occurrence": 0},
    {"english": "hot", "advanced_english": "warm", "occurrence": 0},
    {"english": "cold", "advanced_english": "chilly", "occurrence": 0},
    {"english": "rich", "advanced_english": "wealthy", "occurrence": 0},
    {"english": "poor", "advanced_english": "destitute", "occurrence": 0},
    {"english": "old", "advanced_english": "aged", "occurrence": 0},
    {"english": "young", "advanced_english": "youthful", "occurrence": 0},
    {"english": "bright", "advanced_english": "luminous", "occurrence": 0},
    {"english": "dark", "advanced_english": "dim", "occurrence": 0},
    {"english": "easy", "advanced_english": "simple", "occurrence": 0},
    {"english": "hard", "advanced_english": "difficult", "occurrence": 0},
    {"english": "clean", "advanced_english": "spotless", "occurrence": 0},
    {"english": "dirty", "advanced_english": "grimy", "occurrence": 0},
    {"english": "kind", "advanced_english": "generous", "occurrence": 0},
    {"english": "mean", "advanced_english": "cruel", "occurrence": 0},
    {"english": "friendly", "advanced_english": "cordial", "occurrence": 0}
]

def get_random_items(data, num_items):
    """Select random unique items from the list avoiding repetition."""
    # Filter items where occurrence is 0 (not yet selected)
    available_items = [item for item in data if item["occurrence"] == 0]
    
    # Reset occurrences if not enough items are left
    if len(available_items) < num_items:
        for item in data:
            item["occurrence"] = 0
        available_items = data  # All items are available again
    
    # Randomly select the required number of items
    selected_items = random.sample(available_items, num_items)
    
    # Update occurrence for selected items
    for item in selected_items:
        item["occurrence"] = 1
    
    return selected_items

# Main program
if __name__ == "__main__":
    for i in range(2):  # Run 5 times for testing
        print(f"\nRun {i+1}:")
        random_items = get_random_items(adjectives_synonyms, 5)
        score = 0
        for item in random_items:
            print(f"English: {item['english']}, Advanced: {item['advanced_english']}")
            print(f"What is Synonyms for {item['english']} ?")
            user_answer = input("Your Answer: ")
            if user_answer == item['advanced_english']:
                print("Correct\n")
                score+=1
            else:
                print(f"Idiot! Wrong Answer. Correct Answer: {item['advanced_english']}\n")
        print("Total Score:",score)