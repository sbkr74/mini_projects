def replace_word(word_to_replace, word_replacement):
    msg = "Hi Everyone. This is system generated message using python just to test word_replacement (Hi Hi Hi)"
    
    # Initialize variables
    new_msg = ""
    i = 0
    n = len(msg)
    word_length = len(word_to_replace)
    
    while i < n:
        # Check if the current substring matches the word_to_replace
        if msg[i:i + word_length] == word_to_replace:
            # Check if it's a whole word (bounded by non-alphanumeric characters or start/end of string)
            is_word_start = (i == 0 or not msg[i - 1].isalnum())
            is_word_end = (i + word_length == n or not msg[i + word_length].isalnum())
            
            if is_word_start and is_word_end:
                # Replace the word
                new_msg += word_replacement
                i += word_length
            else:
                # Keep the original substring
                new_msg += msg[i]
                i += 1
        else:
            # Keep the current character
            new_msg += msg[i]
            i += 1
    
    return new_msg

if __name__ =="__main__":
    word_to_replace = input("Enter the word to replace: ").strip()
    word_replacement = input("Enter the word you wanna change to: ").strip()
    msg=replace_word(word_to_replace,word_replacement)
    print(msg)