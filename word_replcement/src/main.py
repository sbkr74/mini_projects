def replace_word(word_to_replace,word_replacement):
    msg = "Hi Everyone. This is system generated message using python just to test word_replacement (Hi Hi Hi)"
    new_msg = msg.replace(word_to_replace,word_replacement)
    return new_msg

if __name__ =="__main__":
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word you wanna change to: ")
    msg=replace_word(word_to_replace,word_replacement)
    print(msg)