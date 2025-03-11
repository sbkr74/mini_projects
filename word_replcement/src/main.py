def replace_word(word_to_replace,word_replacement):
    msg = "Hi Everyone. This is system generated message using python just to test word_replacement (Hi Hi Hi)"
    
    words = msg.split(" ")
    for i in range(len(words)):
        if words[i] == word_to_replace:
            words[i] = word_replacement
        
    new_msg = " ".join(words)

    return new_msg

if __name__ =="__main__":
    word_to_replace = input("Enter the word to replace: ").strip()
    word_replacement = input("Enter the word you wanna change to: ").strip()
    msg=replace_word(word_to_replace,word_replacement)
    print(msg)