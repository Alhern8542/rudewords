import string
test_words = ["crap", "darn!", "Heck!!!", "jerk...", "idiot?", "butt", "devil"]

def bleeper(word):
    # Write code to replace rude words with asterisks
    new_word = []
    for character in word:
        if character not in string.punctuation:
            new_word.append("*")
        else:
            new_word.append(character)
    return "".join(new_word)

for word in test_words:
    print(bleeper(word))
