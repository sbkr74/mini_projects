import random
words = [
    {"eng": "happy", "adv": "joyful/cheerful/delighted/ecstatic/content"},
    {"eng": "sad", "adv": "sorrowful/gloomy/melancholy/dejected/mournful"},
    {"eng": "angry", "adv": "irate/furious/enraged/annoyed/resentful"},
    {"eng": "big", "adv": "large/massive/enormous/huge/gigantic"},
    {"eng": "small", "adv": "tiny/minute/miniature/microscopic/petite"},
    {"eng": "beautiful", "adv": "lovely/stunning/gorgeous/elegant/exquisite"},
    {"eng": "ugly", "adv": "unattractive/hideous/unsightly/deformed/repulsive"},
    {"eng": "good", "adv": "great/excellent/superb/outstanding/marvelous"},
    {"eng": "bad", "adv": "terrible/awful/poor/horrible/dreadful"},
    {"eng": "smart", "adv": "intelligent/clever/bright/wise/quick-witted"},
    {"eng": "stupid", "adv": "foolish/dull/ignorant/idiotic/mindless"},
    {"eng": "strong", "adv": "powerful/sturdy/robust/mighty/forceful"},
    {"eng": "weak", "adv": "frail/feeble/delicate/vulnerable/fragile"},
    {"eng": "fast", "adv": "quick/swift/rapid/speedy/brisk"},
    {"eng": "slow", "adv": "sluggish/lethargic/unhurried/lazy/plodding"},
    {"eng": "hot", "adv": "warm/scorching/blazing/boiling/sizzling"},
    {"eng": "cold", "adv": "chilly/freezing/frigid/icy/nippy"},
    {"eng": "rich", "adv": "wealthy/affluent/prosperous/opulent/well-off"},
    {"eng": "poor", "adv": "destitute/impoverished/needy/underprivileged/penniless"},
    {"eng": "old", "adv": "aged/ancient/elderly/antique/timeworn"},
    {"eng": "young", "adv": "youthful/juvenile/fresh/immature/adolescent"},
    {"eng": "bright", "adv": "luminous/radiant/brilliant/shining/vivid"},
    {"eng": "dark", "adv": "dim/gloomy/shadowy/murky/obscure"},
    {"eng": "easy", "adv": "simple/effortless/uncomplicated/straightforward/painless"},
    {"eng": "hard", "adv": "difficult/challenging/tough/arduous/strenuous"},
    {"eng": "clean", "adv": "spotless/pristine/immaculate/sterile/untarnished"},
    {"eng": "dirty", "adv": "grimy/filthy/soiled/messy/stained"},
    {"eng": "kind", "adv": "generous/compassionate/benevolent/thoughtful/altruistic"},
    {"eng": "mean", "adv": "cruel/harsh/malicious/unkind/hostile"},
    {"eng": "friendly", "adv": "cordial/amiable/sociable/affable/welcoming"}
]

def main(words):
    random.shuffle(words)
    score = 0
    count = 0
    for word in words:
        count+=1
        if count>10:
            print("Final Score:",score)
            break
        else:
            print(f"What is Synonyms for {word['eng']} ?")
            user_answer = input("Your Answer: ")
            if user_answer in word['adv'].split('/'):
                print("Correct\n")
                score+=1
            else:
                opt = random.choice(word['adv'].split('/'))
                print(f"Wrong Answer Idiot! Correct Answer is \'{opt}\'\n")
                

main(words)