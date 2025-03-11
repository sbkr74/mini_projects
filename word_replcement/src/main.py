def replace_word():
    msg = "Hi Everyone. This is system generated message using python just to test word_replacement (Hi Hi Hi)"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word you wanna change to: ")

    new_msg = msg.replace(word_to_replace,word_replacement)
    print(new_msg)

replace_word()