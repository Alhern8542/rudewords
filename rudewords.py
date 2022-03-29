import string

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def bleeper(word):
    # Write code to replace rude words with asterisks
    new_word = []
    for character in word:
        if character not in string.punctuation:
            new_word.append("*")
        else:
            new_word.append(character)
    return "".join(new_word)


def check_line(line):
    rude_count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word in rude_words:
            rude_count += 1
            print(f"Found rude word: {word}")
    return rude_count


def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile:
            rude_count += check_line(line)
    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")


if __name__ == "__main__":
    check_file("my_other_story.txt")